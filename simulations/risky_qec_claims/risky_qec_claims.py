#!/usr/bin/env python3
"""Stress tests for overstrong ACP/QEC claims.

The goal is not to prove the noise-tailoring program. It is to falsify or
weaken tempting claims that would make the program less defensible:

1. Ideal syndrome extraction is not automatically logical crystallization.
2. Positive logical/noise/environment synergy is not automatically a resource.
3. "Use the noisiest qubit first" is not a valid memory-design rule.
4. A productive correction interval appears when monitoring has backaction;
   with ideal syndrome extraction, frequent correction can be best.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import numpy as np


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
SUMMARY_CSV = OUT / "risk_audit_summary.csv"
INTERACTION_CSV = OUT / "interaction_information_tests.csv"
SYNDROME_CSV = OUT / "syndrome_measurement_tests.csv"
MONITORING_CSV = OUT / "monitoring_interval_scan.csv"
NOISIEST_CSV = OUT / "noisiest_qubit_tests.csv"

N_QUBITS = 3
DIM = 2**N_QUBITS
TOTAL_TICKS = 72
MONITORING_TEST_NOISE = 0.02
SYNDROME_TEST_NOISE = 0.08


def entropy_bits(probabilities: Iterable[float]) -> float:
    probs = np.asarray(list(probabilities), dtype=float)
    probs = probs[probs > 0.0]
    if len(probs) == 0:
        return 0.0
    return float(-np.sum(probs * np.log2(probs)))


def write_csv(path: Path, rows: list[dict[str, float | int | str]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


# ---------------------------------------------------------------------------
# Discrete information tests


EventDist = list[tuple[tuple[int, ...], float]]


def projected_distribution(dist: EventDist, indices: tuple[int, ...]) -> dict[tuple[int, ...], float]:
    out: dict[tuple[int, ...], float] = defaultdict(float)
    for event, probability in dist:
        key = tuple(event[index] for index in indices)
        out[key] += probability
    return dict(out)


def entropy_of(dist: EventDist, indices: tuple[int, ...]) -> float:
    return entropy_bits(projected_distribution(dist, indices).values())


def mutual_information(dist: EventDist, xs: tuple[int, ...], ys: tuple[int, ...]) -> float:
    return (
        entropy_of(dist, xs)
        + entropy_of(dist, ys)
        - entropy_of(dist, tuple(sorted(set(xs + ys))))
    )


def conditional_mutual_information(
    dist: EventDist, xs: tuple[int, ...], ys: tuple[int, ...], zs: tuple[int, ...]
) -> float:
    xz = tuple(sorted(set(xs + zs)))
    yz = tuple(sorted(set(ys + zs)))
    xyz = tuple(sorted(set(xs + ys + zs)))
    return entropy_of(dist, xz) + entropy_of(dist, yz) - entropy_of(dist, zs) - entropy_of(dist, xyz)


def clean_bits(value: float) -> float:
    """Remove tiny entropy-arithmetic noise around zero."""

    if abs(value) < 1e-12:
        return 0.0
    return float(value)


def xor_logical_leak_distribution(p_error: float = 0.2) -> EventDist:
    """Two records are individually harmless but jointly reveal the logical bit.

    Event tuple: (logical L, error X, record A, record B, syndrome S).
    """

    rows: EventDist = []
    for logical in (0, 1):
        for error in (0, 1):
            p_x = p_error if error else 1.0 - p_error
            for pad in (0, 1):
                record_a = pad
                record_b = logical ^ pad
                syndrome = 0
                rows.append(((logical, error, record_a, record_b, syndrome), 0.5 * p_x * 0.5))
    return rows


def clean_syndrome_distribution(p_error: float = 0.2, syndrome_flip: float = 0.0) -> EventDist:
    """A syndrome record tracks errors and remains independent of the logical bit."""

    rows: EventDist = []
    for logical in (0, 1):
        for error in (0, 1):
            p_x = p_error if error else 1.0 - p_error
            for flip in (0, 1):
                p_flip = syndrome_flip if flip else 1.0 - syndrome_flip
                syndrome = error ^ flip
                record_a = error
                record_b = syndrome
                rows.append(((logical, error, record_a, record_b, syndrome), 0.5 * p_x * p_flip))
    return rows


def leaky_syndrome_distribution(p_error: float = 0.2, leak_probability: float = 0.35) -> EventDist:
    """A useful syndrome plus a centralizing logical-branch erasure record."""

    rows: EventDist = []
    for logical in (0, 1):
        for error in (0, 1):
            p_x = p_error if error else 1.0 - p_error
            syndrome = error
            for leaks in (0, 1):
                p_leak = leak_probability if leaks else 1.0 - leak_probability
                record_a = syndrome
                record_b = logical if leaks else 2
                rows.append(((logical, error, record_a, record_b, syndrome), 0.5 * p_x * p_leak))
    return rows


def interaction_information_tests() -> list[dict[str, float | str]]:
    scenarios = [
        (
            "split_logical_leak",
            xor_logical_leak_distribution(),
            "falsifies_positive_logical_synergy_as_resource",
        ),
        (
            "clean_error_syndrome",
            clean_syndrome_distribution(),
            "useful_syndrome_with_zero_logical_synergy",
        ),
        (
            "noisy_error_syndrome",
            clean_syndrome_distribution(syndrome_flip=0.12),
            "useful_but_imperfect_syndrome_with_zero_logical_synergy",
        ),
        (
            "syndrome_plus_logical_leak",
            leaky_syndrome_distribution(),
            "syndrome_information_does_not_excuse_logical_leakage",
        ),
    ]

    rows: list[dict[str, float | str]] = []
    for name, dist, verdict in scenarios:
        # Indices: L=0, error=1, record_a=2, record_b=3, syndrome=4.
        i_error_syndrome = mutual_information(dist, (1,), (4,))
        i_l_a = mutual_information(dist, (0,), (2,))
        i_l_b = mutual_information(dist, (0,), (3,))
        i_l_ab = mutual_information(dist, (0,), (2, 3))
        synergy = i_l_ab - i_l_a - i_l_b
        conditional_leakage = conditional_mutual_information(dist, (0,), (2, 3), (1,))
        rows.append(
            {
                "scenario": name,
                "error_syndrome_mi_bits": clean_bits(i_error_syndrome),
                "logical_record_a_mi_bits": clean_bits(i_l_a),
                "logical_record_b_mi_bits": clean_bits(i_l_b),
                "logical_joint_record_mi_bits": clean_bits(i_l_ab),
                "logical_noise_env_synergy_bits": clean_bits(synergy),
                "conditional_logical_leakage_given_error_bits": clean_bits(conditional_leakage),
                "verdict": verdict,
            }
        )
    return rows


# ---------------------------------------------------------------------------
# Repetition-code channel tests


def basis(index: int) -> np.ndarray:
    ket = np.zeros(DIM, dtype=complex)
    ket[index] = 1.0
    return ket


KET_0L = basis(0)
KET_1L = basis(7)
KET_PLUS = (KET_0L + KET_1L) / np.sqrt(2.0)
RHO_0L = np.outer(KET_0L, KET_0L.conjugate())
RHO_PLUS = np.outer(KET_PLUS, KET_PLUS.conjugate())
PROJECTOR_0L = np.outer(KET_0L, KET_0L.conjugate())
PROJECTOR_PLUS = np.outer(KET_PLUS, KET_PLUS.conjugate())
PROJECTOR_CODE = np.outer(KET_0L, KET_0L.conjugate()) + np.outer(KET_1L, KET_1L.conjugate())
LOGICAL_Z = np.diag([1, 1, 1, 1, -1, -1, -1, -1]).astype(complex)


def bitflip_operator(qubit: int) -> np.ndarray:
    op = np.zeros((DIM, DIM), dtype=complex)
    mask = 1 << (N_QUBITS - 1 - qubit)
    for index in range(DIM):
        op[index ^ mask, index] = 1.0
    return op


X_OPS = [bitflip_operator(qubit) for qubit in range(N_QUBITS)]


def mask_operator(mask: int) -> np.ndarray:
    op = np.eye(DIM, dtype=complex)
    for qubit in range(N_QUBITS):
        if mask & (1 << (N_QUBITS - 1 - qubit)):
            op = X_OPS[qubit] @ op
    return op


MASKS = list(range(2**N_QUBITS))
MASK_OPS = [mask_operator(mask) for mask in MASKS]
MASK_WEIGHTS = np.array([bin(mask).count("1") for mask in MASKS])


def projector(indices: list[int]) -> np.ndarray:
    p = np.zeros((DIM, DIM), dtype=complex)
    for index in indices:
        p[index, index] = 1.0
    return p


SYNDROME_PROJECTORS = [
    projector([0b000, 0b111]),
    projector([0b100, 0b011]),
    projector([0b010, 0b101]),
    projector([0b001, 0b110]),
]
RECOVERY_OPS = [np.eye(DIM, dtype=complex), X_OPS[0], X_OPS[1], X_OPS[2]]
RECOVERY_KRAUS = [u @ p for u, p in zip(RECOVERY_OPS, SYNDROME_PROJECTORS)]


def syndrome_from_errors(errors: tuple[int, int, int]) -> int:
    e0, e1, e2 = errors
    return (e0 ^ e1) * 2 + (e1 ^ e2)


def syndrome_from_mask(mask: int) -> int:
    return syndrome_from_errors(((mask >> 2) & 1, (mask >> 1) & 1, mask & 1))


SYNDROMES = np.array([syndrome_from_mask(mask) for mask in MASKS])


def bitflip_noise(rho: np.ndarray, p_noise: float) -> np.ndarray:
    out = np.zeros_like(rho)
    for mask, op, weight in zip(MASKS, MASK_OPS, MASK_WEIGHTS):
        probability = (p_noise**weight) * ((1.0 - p_noise) ** (N_QUBITS - weight))
        out += probability * op @ rho @ op.conjugate().T
    return out


def recovery_channel(rho: np.ndarray) -> np.ndarray:
    return sum(k @ rho @ k.conjugate().T for k in RECOVERY_KRAUS)


def logical_dephasing(rho: np.ndarray, strength: float) -> np.ndarray:
    strength = float(np.clip(strength, 0.0, 0.5))
    return (1.0 - strength) * rho + strength * LOGICAL_Z @ rho @ LOGICAL_Z


def logical_branch_record_backaction(rho: np.ndarray, centrality: float) -> np.ndarray:
    centrality = float(np.clip(centrality, 0.0, 1.0))
    measured = 0.5 * (rho + LOGICAL_Z @ rho @ LOGICAL_Z)
    return (1.0 - centrality) * rho + centrality * measured


def syndrome_mi_uniform(p_noise: float) -> float:
    syndrome_probs = np.zeros(4, dtype=float)
    for mask, weight, syndrome in zip(MASKS, MASK_WEIGHTS, SYNDROMES):
        probability = (p_noise**weight) * ((1.0 - p_noise) ** (N_QUBITS - weight))
        syndrome_probs[syndrome] += probability
    return entropy_bits(syndrome_probs)


def state_metrics(rho_0: np.ndarray, rho_plus: np.ndarray) -> dict[str, float]:
    bit_fidelity = float(np.real(np.trace(PROJECTOR_0L @ rho_0)))
    plus_fidelity = float(np.real(np.trace(PROJECTOR_PLUS @ rho_plus)))
    code_population = float(np.real(np.trace(PROJECTOR_CODE @ rho_0)))
    logical_coherence = float(2.0 * abs(rho_plus[0, 7]))
    bit_advantage = max(0.0, 2.0 * bit_fidelity - 1.0)
    productive_score = bit_advantage * plus_fidelity * code_population * logical_coherence
    return {
        "bit_fidelity": bit_fidelity,
        "bit_advantage": bit_advantage,
        "plus_fidelity": plus_fidelity,
        "code_population": code_population,
        "logical_coherence": logical_coherence,
        "productive_score": productive_score,
    }


LOGICAL_INDICES = np.array([0, 7])
PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
PAULI_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
PAULI_Z = np.array([[1, 0], [0, -1]], dtype=complex)


def embed_logical(operator: np.ndarray) -> np.ndarray:
    physical = np.zeros((DIM, DIM), dtype=complex)
    physical[np.ix_(LOGICAL_INDICES, LOGICAL_INDICES)] = operator
    return physical


def decode_logical(operator: np.ndarray) -> np.ndarray:
    return operator[np.ix_(LOGICAL_INDICES, LOGICAL_INDICES)]


def recovered_logical_channel_pauli_metrics(
    p_noise: float, centrality: float
) -> dict[str, float]:
    """Logical-channel metrics after one noisy round and recovery.

    The plus-state coherence test is intentionally not enough: logical X
    failures leave |+_L> invariant. These Pauli-transfer diagnostics expose the
    full recovered logical channel for the one-round repetition-code toy.
    """

    paulis = [PAULI_X, PAULI_Y, PAULI_Z]
    diagonals: list[float] = []
    for pauli in paulis:
        physical = embed_logical(pauli)
        physical = bitflip_noise(physical, p_noise)
        physical = recovery_channel(physical)
        physical = logical_branch_record_backaction(physical, centrality)
        logical = decode_logical(physical)
        diagonals.append(float(np.real(np.trace(pauli @ logical)) / 2.0))

    fe_identity = (1.0 + sum(diagonals)) / 4.0
    return {
        "logical_channel_fe_identity": float(fe_identity),
        "logical_ptm_xx": diagonals[0],
        "logical_ptm_yy": diagonals[1],
        "logical_ptm_zz": diagonals[2],
    }


def syndrome_measurement_tests() -> list[dict[str, float | str]]:
    p_noise = SYNDROME_TEST_NOISE
    tests = [
        ("no_recovery", False, 0.0, "under_corrected_noise_accumulates"),
        ("ideal_syndrome_recovery", True, 0.0, "falsifies_syndrome_equals_crystallization"),
        ("partial_logical_record", True, 0.4, "costly_or_centralizing_monitoring_degrades_coherence"),
        ("logical_branch_record", True, 1.0, "centralizing_measurement_preserves_bit_but_kills_superposition"),
    ]

    rows: list[dict[str, float | str]] = []
    for name, recover, centrality, verdict in tests:
        rho_0 = bitflip_noise(RHO_0L, p_noise)
        rho_plus = bitflip_noise(RHO_PLUS, p_noise)
        syndrome_bits = syndrome_mi_uniform(p_noise) if recover else 0.0
        if recover:
            rho_0 = recovery_channel(rho_0)
            rho_plus = recovery_channel(rho_plus)
        rho_0 = logical_branch_record_backaction(rho_0, centrality)
        rho_plus = logical_branch_record_backaction(rho_plus, centrality)
        metrics = state_metrics(rho_0, rho_plus)
        channel_metrics = (
            recovered_logical_channel_pauli_metrics(p_noise, centrality)
            if recover
            else {
                "logical_channel_fe_identity": float("nan"),
                "logical_ptm_xx": float("nan"),
                "logical_ptm_yy": float("nan"),
                "logical_ptm_zz": float("nan"),
            }
        )
        rows.append(
            {
                "scenario": name,
                "p_noise": p_noise,
                "syndrome_mi_bits": syndrome_bits,
                "logical_record_probability": centrality,
                "logical_leakage_bits_model": centrality,
                **metrics,
                **channel_metrics,
                "verdict": verdict,
            }
        )
    return rows


def evolve(
    initial_rho: np.ndarray, p_noise: float, correction_interval: int, backaction_per_recovery: float
) -> np.ndarray:
    rho = initial_rho.copy()
    for tick in range(1, TOTAL_TICKS + 1):
        rho = bitflip_noise(rho, p_noise)
        if tick % correction_interval == 0:
            rho = recovery_channel(rho)
            rho = logical_dephasing(rho, backaction_per_recovery)
    return rho


def monitoring_interval_scan() -> list[dict[str, float | int | str]]:
    rows: list[dict[str, float | int | str]] = []
    for backaction in (0.0, 0.012):
        for interval in range(1, TOTAL_TICKS + 1):
            rho_0 = evolve(RHO_0L, MONITORING_TEST_NOISE, interval, backaction)
            rho_plus = evolve(RHO_PLUS, MONITORING_TEST_NOISE, interval, backaction)
            metrics = state_metrics(rho_0, rho_plus)
            rows.append(
                {
                    "p_noise": MONITORING_TEST_NOISE,
                    "backaction_per_recovery": backaction,
                    "correction_interval": interval,
                    **metrics,
                }
            )
    return rows


# ---------------------------------------------------------------------------
# Noisiest-qubit test


def one_round_error_syndrome_distribution(rates: tuple[float, float, float]) -> EventDist:
    rows: EventDist = []
    for e0 in (0, 1):
        for e1 in (0, 1):
            for e2 in (0, 1):
                errors = (e0, e1, e2)
                probability = 1.0
                for error, rate in zip(errors, rates):
                    probability *= rate if error else 1.0 - rate
                syndrome = syndrome_from_errors(errors)
                rows.append(((e0, e1, e2, syndrome), probability))
    return rows


def bare_bit_advantage_after_ticks(p_error: float, ticks: int = 24) -> float:
    return float((1.0 - 2.0 * p_error) ** ticks)


def noisiest_qubit_tests() -> list[dict[str, float | int | str]]:
    rates = (0.12, 0.02, 0.02)
    ticks = 24
    dist = one_round_error_syndrome_distribution(rates)
    noisiest = int(np.argmax(rates))
    rows: list[dict[str, float | int | str]] = []
    for qubit, rate in enumerate(rates):
        bit_advantage = bare_bit_advantage_after_ticks(rate, ticks)
        rows.append(
            {
                "qubit": qubit,
                "physical_error_rate": rate,
                "is_noisiest": int(qubit == noisiest),
                "bare_memory_ticks": ticks,
                "bare_bit_advantage": bit_advantage,
                "bare_bit_fidelity": 0.5 * (1.0 + bit_advantage),
                "single_round_mi_error_qubit_syndrome_bits": mutual_information(dist, (qubit,), (3,)),
                "verdict": "decoder_attention_not_computation_start"
                if qubit == noisiest
                else "better_bare_storage_candidate",
            }
        )
    return rows


def summarize(
    interaction_rows: list[dict[str, float | str]],
    syndrome_rows: list[dict[str, float | str]],
    monitoring_rows: list[dict[str, float | int | str]],
    noisiest_rows: list[dict[str, float | int | str]],
) -> list[dict[str, str]]:
    split = next(row for row in interaction_rows if row["scenario"] == "split_logical_leak")
    clean = next(row for row in interaction_rows if row["scenario"] == "clean_error_syndrome")
    ideal = next(row for row in syndrome_rows if row["scenario"] == "ideal_syndrome_recovery")
    central = next(row for row in syndrome_rows if row["scenario"] == "logical_branch_record")

    monitoring_summary = []
    for backaction in (0.0, 0.012):
        subset = [
            row
            for row in monitoring_rows
            if abs(float(row["backaction_per_recovery"]) - backaction) < 1e-12
        ]
        best = max(subset, key=lambda row: float(row["productive_score"]))
        interval_1 = next(row for row in subset if int(row["correction_interval"]) == 1)
        monitoring_summary.extend(
            [
                {
                    "metric": f"best_interval_backaction_{backaction:.3f}",
                    "value": str(int(best["correction_interval"])),
                },
                {
                    "metric": f"best_score_backaction_{backaction:.3f}",
                    "value": f"{float(best['productive_score']):.6f}",
                },
                {
                    "metric": f"interval_1_score_backaction_{backaction:.3f}",
                    "value": f"{float(interval_1['productive_score']):.6f}",
                },
            ]
        )

    noisiest = next(row for row in noisiest_rows if int(row["is_noisiest"]) == 1)
    quietest = max(
        (row for row in noisiest_rows if int(row["is_noisiest"]) == 0),
        key=lambda row: float(row["bare_bit_advantage"]),
    )

    rows = [
        {
            "metric": "split_logical_leak_synergy_bits",
            "value": f"{float(split['logical_noise_env_synergy_bits']):.6f}",
        },
        {
            "metric": "split_logical_leak_conditional_leakage_bits",
            "value": f"{float(split['conditional_logical_leakage_given_error_bits']):.6f}",
        },
        {
            "metric": "clean_syndrome_error_syndrome_mi_bits",
            "value": f"{float(clean['error_syndrome_mi_bits']):.6f}",
        },
        {
            "metric": "clean_syndrome_logical_synergy_bits",
            "value": f"{float(clean['logical_noise_env_synergy_bits']):.6f}",
        },
        {
            "metric": "ideal_syndrome_logical_coherence",
            "value": f"{float(ideal['logical_coherence']):.6f}",
        },
        {
            "metric": "ideal_syndrome_logical_channel_fe_identity",
            "value": f"{float(ideal['logical_channel_fe_identity']):.6f}",
        },
        {
            "metric": "centralizing_record_logical_coherence",
            "value": f"{float(central['logical_coherence']):.6f}",
        },
        {
            "metric": "centralizing_record_logical_channel_fe_identity",
            "value": f"{float(central['logical_channel_fe_identity']):.6f}",
        },
        {
            "metric": "centralizing_record_bit_fidelity",
            "value": f"{float(central['bit_fidelity']):.6f}",
        },
        *monitoring_summary,
        {
            "metric": "noisiest_qubit_bare_bit_advantage",
            "value": f"{float(noisiest['bare_bit_advantage']):.6f}",
        },
        {
            "metric": "quiet_qubit_bare_bit_advantage",
            "value": f"{float(quietest['bare_bit_advantage']):.6f}",
        },
        {
            "metric": "noisiest_qubit_syndrome_mi_bits",
            "value": f"{float(noisiest['single_round_mi_error_qubit_syndrome_bits']):.6f}",
        },
    ]
    return rows


def main() -> None:
    interaction_rows = interaction_information_tests()
    syndrome_rows = syndrome_measurement_tests()
    monitoring_rows = monitoring_interval_scan()
    noisiest_rows = noisiest_qubit_tests()
    summary_rows = summarize(interaction_rows, syndrome_rows, monitoring_rows, noisiest_rows)

    write_csv(INTERACTION_CSV, interaction_rows)
    write_csv(SYNDROME_CSV, syndrome_rows)
    write_csv(MONITORING_CSV, monitoring_rows)
    write_csv(NOISIEST_CSV, noisiest_rows)
    write_csv(SUMMARY_CSV, summary_rows)

    print(f"wrote {INTERACTION_CSV}")
    print(f"wrote {SYNDROME_CSV}")
    print(f"wrote {MONITORING_CSV}")
    print(f"wrote {NOISIEST_CSV}")
    print(f"wrote {SUMMARY_CSV}")
    for row in summary_rows:
        print(f"{row['metric']}: {row['value']}")


if __name__ == "__main__":
    main()
