#!/usr/bin/env python3
"""Hardware-facing adaptive decoder benchmark for a 3-qubit repetition memory.

This is the first device-stack version of OP-16. The code is fixed: a
three-qubit bit-flip repetition memory. The adaptation variable is not the
logical encoding or protected Pauli axis. It is the decoder likelihood table
used to interpret noisy parity-syndrome measurements under drifting,
non-identically distributed data-qubit error rates.

The model is deliberately small enough to evaluate exactly as an 8-state
classical Pauli channel. That lets the script report a logical error rate,
entanglement fidelity for the induced logical bit-flip channel, and the
classical diagonal version of the SACR contraction calibration
q*, eta*, eta*/(1-q*) for each implemented correction round.
"""

from __future__ import annotations

import csv
import math
import os
from dataclasses import dataclass
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(__file__).resolve().parent / "outputs" / ".mpl-cache")
)
os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
CSV_PATH = OUT / "hardware_adaptive_decoder_scan.csv"
HEATMAP_PATH = OUT / "hardware_adaptive_decoder_heatmap.png"
CURVES_PATH = OUT / "hardware_adaptive_decoder_curves.png"

N_QUBITS = 3
N_STATES = 2**N_QUBITS
TOTAL_ROUNDS = 48
BASE_DATA_ERROR = 0.012
MEASUREMENT_ERROR = 0.012
CHARACTERIZATION_DATA_ERROR = 0.0009
ADAPTIVE_INTERVAL = 12
OVERACTIVE_INTERVAL = 1
ESTIMATOR_GAIN = 0.85

ANISOTROPY_VALUES = np.linspace(0.0, 1.8, 25)
DRIFT_VALUES = np.linspace(0.0, 2.0, 25)

# Correctable sector P: no data error or one data error. Leakage sector Q:
# states with majority bit flips, which decode to the wrong logical bit.
P_STATES = [state for state in range(N_STATES) if int(state).bit_count() <= 1]
Q_STATES = [state for state in range(N_STATES) if int(state).bit_count() >= 2]


@dataclass(frozen=True)
class Protocol:
    name: str
    mode: str
    update_interval: int | None = None
    characterization_overhead: bool = False


PROTOCOLS = [
    Protocol("uniform_decoder", "uniform"),
    Protocol("static_tailored", "static"),
    Protocol("adaptive_decoder", "adaptive", ADAPTIVE_INTERVAL, True),
    Protocol("overactive_decoder", "adaptive", OVERACTIVE_INTERVAL, True),
    Protocol("oracle_decoder", "oracle"),
]


def bit(state: int, qubit: int) -> int:
    """Return bit value for qubit index 0, 1, or 2."""

    return (state >> qubit) & 1


def syndrome(state: int) -> tuple[int, int]:
    """Return the two parity-check bits for the 3-bit repetition code."""

    return bit(state, 0) ^ bit(state, 1), bit(state, 1) ^ bit(state, 2)


def syndrome_for_candidate(candidate: int) -> tuple[int, int]:
    """Syndrome predicted by a single-round candidate correction."""

    return syndrome(candidate)


def correction_mask(candidate: int) -> int:
    """Map candidate labels to bit masks: 0 none, 1 q0, 2 q1, 3 q2."""

    if candidate == 0:
        return 0
    return 1 << (candidate - 1)


def data_rates(anisotropy: float, drift_cycles: float, round_index: int) -> np.ndarray:
    """Drifting, non-identically distributed data-qubit error probabilities."""

    phase = 2.0 * np.pi * drift_cycles * round_index / max(1, TOTAL_ROUNDS - 1)
    offsets = np.array([0.0, 2.0 * np.pi / 3.0, 4.0 * np.pi / 3.0])
    logits = anisotropy * np.cos(phase - offsets)
    weights = np.exp(logits)
    weights /= float(np.mean(weights))
    return np.clip(BASE_DATA_ERROR * weights, 1e-6, 0.24)


def measurement_probability(observed: tuple[int, int], predicted: tuple[int, int], p_meas: float) -> float:
    """Probability of an observed syndrome given the predicted syndrome."""

    p = 1.0
    for obs, pred in zip(observed, predicted):
        p *= 1.0 - p_meas if obs == pred else p_meas
    return float(p)


def candidate_priors(estimated_rates: np.ndarray) -> np.ndarray:
    """One-round prior probabilities for no error or one data-qubit error."""

    rates = np.clip(np.asarray(estimated_rates, dtype=float), 1e-6, 0.49)
    none = float(np.prod(1.0 - rates))
    priors = [none]
    for qubit in range(N_QUBITS):
        p = rates[qubit]
        others = [i for i in range(N_QUBITS) if i != qubit]
        priors.append(float(p * np.prod(1.0 - rates[others])))
    priors = np.asarray(priors, dtype=float)
    priors /= float(np.sum(priors))
    return np.clip(priors, 1e-12, 1.0)


def choose_correction(
    observed: tuple[int, int], estimated_rates: np.ndarray, estimated_meas: float
) -> int:
    """Weighted maximum-likelihood one-round decoder."""

    priors = candidate_priors(estimated_rates)
    best_candidate = 0
    best_cost = math.inf
    for candidate in range(4):
        predicted = syndrome_for_candidate(correction_mask(candidate))
        likelihood = measurement_probability(observed, predicted, estimated_meas)
        cost = -math.log(float(priors[candidate])) - math.log(max(likelihood, 1e-15))
        if cost < best_cost:
            best_cost = cost
            best_candidate = candidate
    return best_candidate


def data_transition(rates: np.ndarray) -> np.ndarray:
    """Column-stochastic transition matrix for independent bit flips."""

    rates = np.asarray(rates, dtype=float)
    transition = np.zeros((N_STATES, N_STATES), dtype=float)
    for source in range(N_STATES):
        for mask in range(N_STATES):
            probability = 1.0
            for qubit in range(N_QUBITS):
                p = rates[qubit]
                probability *= p if bit(mask, qubit) else 1.0 - p
            target = source ^ mask
            transition[target, source] += probability
    return transition


def correction_transition(
    estimated_rates: np.ndarray,
    estimated_meas: float,
    true_meas: float = MEASUREMENT_ERROR,
) -> np.ndarray:
    """Column-stochastic transition matrix for noisy syndrome observation and correction."""

    transition = np.zeros((N_STATES, N_STATES), dtype=float)
    observed_syndromes = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for source in range(N_STATES):
        true_syndrome = syndrome(source)
        for observed in observed_syndromes:
            probability = measurement_probability(observed, true_syndrome, true_meas)
            correction = choose_correction(observed, estimated_rates, estimated_meas)
            target = source ^ correction_mask(correction)
            transition[target, source] += probability
    return transition


def round_transition(
    true_rates: np.ndarray,
    estimated_rates: np.ndarray,
    estimated_meas: float,
    update_overhead: bool,
    true_meas: float = MEASUREMENT_ERROR,
) -> np.ndarray:
    """One implemented hardware correction round."""

    transition = correction_transition(estimated_rates, estimated_meas, true_meas) @ data_transition(true_rates)
    if update_overhead:
        overhead_rates = np.full(N_QUBITS, CHARACTERIZATION_DATA_ERROR, dtype=float)
        transition = transition @ data_transition(overhead_rates)
    return transition


def q_eta_floor(transition: np.ndarray) -> tuple[float, float, float]:
    """Classical diagonal version of q*, eta*, and eta*/(1-q*)."""

    q_star = max(float(np.sum(transition[Q_STATES, source])) for source in Q_STATES)
    eta_star = max(float(np.sum(transition[Q_STATES, source])) for source in P_STATES)
    if q_star >= 1.0:
        floor = math.inf
    else:
        floor = eta_star / max(1.0 - q_star, 1e-15)
    return q_star, eta_star, floor


def estimate_update(previous: np.ndarray, current_true: np.ndarray) -> np.ndarray:
    """Lagged calibration update for decoder likelihoods."""

    return (1.0 - ESTIMATOR_GAIN) * previous + ESTIMATOR_GAIN * current_true


def run_protocol(protocol: Protocol, anisotropy: float, drift_cycles: float) -> dict[str, float | str]:
    """Evaluate one protocol exactly as an 8-state Markov channel."""

    uniform_rates = np.full(N_QUBITS, BASE_DATA_ERROR, dtype=float)
    initial_true = data_rates(anisotropy, drift_cycles, 0)

    if protocol.mode == "uniform":
        estimated_rates = uniform_rates.copy()
    elif protocol.mode in {"static", "adaptive"}:
        estimated_rates = initial_true.copy()
    elif protocol.mode == "oracle":
        estimated_rates = initial_true.copy()
    else:
        raise ValueError(f"unknown protocol mode {protocol.mode!r}")

    state_distribution = np.zeros(N_STATES, dtype=float)
    state_distribution[0] = 1.0
    updates = 0
    average_l1_estimation_error = 0.0
    worst_q = 0.0
    worst_eta = 0.0
    worst_floor = 0.0

    for round_index in range(TOTAL_ROUNDS):
        true_rates = data_rates(anisotropy, drift_cycles, round_index)
        update_this_round = False

        if protocol.mode == "oracle":
            estimated_rates = true_rates.copy()
        elif protocol.mode == "adaptive" and round_index % int(protocol.update_interval or 1) == 0:
            estimated_rates = estimate_update(estimated_rates, true_rates)
            update_this_round = protocol.characterization_overhead
            updates += 1

        average_l1_estimation_error += float(np.sum(np.abs(true_rates - estimated_rates)))
        transition = round_transition(
            true_rates,
            estimated_rates,
            MEASUREMENT_ERROR,
            update_this_round,
        )
        q_star, eta_star, floor = q_eta_floor(transition)
        worst_q = max(worst_q, q_star)
        worst_eta = max(worst_eta, eta_star)
        worst_floor = max(worst_floor, floor)
        state_distribution = transition @ state_distribution

    logical_error = float(np.sum(state_distribution[Q_STATES]))
    entanglement_fidelity = 1.0 - logical_error
    average_l1_estimation_error /= TOTAL_ROUNDS

    return {
        "protocol": protocol.name,
        "anisotropy": float(anisotropy),
        "drift_cycles": float(drift_cycles),
        "logical_error": logical_error,
        "entanglement_fidelity": entanglement_fidelity,
        "updates": float(updates),
        "avg_l1_estimation_error": average_l1_estimation_error,
        "worst_q_star": worst_q,
        "worst_eta_star": worst_eta,
        "worst_alignment_floor": worst_floor,
    }


def summarize_point(anisotropy: float, drift_cycles: float) -> list[dict[str, float | str]]:
    rows = [
        run_protocol(protocol, float(anisotropy), float(drift_cycles))
        for protocol in PROTOCOLS
    ]
    static_names = {"uniform_decoder", "static_tailored"}
    best_static_error = min(
        float(row["logical_error"]) for row in rows if row["protocol"] in static_names
    )
    adaptive_error = next(
        float(row["logical_error"]) for row in rows if row["protocol"] == "adaptive_decoder"
    )
    overactive_error = next(
        float(row["logical_error"]) for row in rows if row["protocol"] == "overactive_decoder"
    )
    oracle_error = next(
        float(row["logical_error"]) for row in rows if row["protocol"] == "oracle_decoder"
    )
    best_protocol = min(rows, key=lambda row: float(row["logical_error"]))["protocol"]
    eps = 1e-15

    for row in rows:
        row["best_static_logical_error"] = best_static_error
        row["adaptive_benefit_log10"] = float(
            np.log10((best_static_error + eps) / (adaptive_error + eps))
        )
        row["overactive_penalty_log10"] = float(
            np.log10((overactive_error + eps) / (adaptive_error + eps))
        )
        row["oracle_gap_log10"] = float(
            np.log10((adaptive_error + eps) / (oracle_error + eps))
        )
        row["best_protocol"] = str(best_protocol)
    return rows


def scan() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for anisotropy in ANISOTROPY_VALUES:
        for drift_cycles in DRIFT_VALUES:
            rows.extend(summarize_point(float(anisotropy), float(drift_cycles)))
    return rows


def write_csv(rows: list[dict[str, float | str]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def protocol_rows(rows: list[dict[str, float | str]], protocol: str) -> list[dict[str, float | str]]:
    return [row for row in rows if row["protocol"] == protocol]


def grid(rows: list[dict[str, float | str]], key: str) -> np.ndarray:
    values = np.zeros((len(ANISOTROPY_VALUES), len(DRIFT_VALUES)))
    index = {
        (round(float(r["anisotropy"]), 6), round(float(r["drift_cycles"]), 6)): float(r[key])
        for r in rows
    }
    for i, anisotropy in enumerate(ANISOTROPY_VALUES):
        for j, drift_cycles in enumerate(DRIFT_VALUES):
            values[i, j] = index[(round(float(anisotropy), 6), round(float(drift_cycles), 6))]
    return values


def write_heatmap(rows: list[dict[str, float | str]]) -> None:
    adaptive = protocol_rows(rows, "adaptive_decoder")
    overactive = protocol_rows(rows, "overactive_decoder")
    benefit = grid(adaptive, "adaptive_benefit_log10")
    adaptive_error = grid(adaptive, "logical_error")
    estimation_error = grid(adaptive, "avg_l1_estimation_error")
    floor = grid(adaptive, "worst_alignment_floor")
    overactive_penalty = grid(overactive, "overactive_penalty_log10")

    fig, axes = plt.subplots(1, 5, figsize=(22, 4), constrained_layout=True)
    panels = [
        ("adaptive benefit vs static", benefit, "coolwarm", None, None),
        ("adaptive logical error", adaptive_error, "magma", 0.0, None),
        ("estimation lag", estimation_error, "viridis", 0.0, None),
        ("worst alignment floor", floor, "cividis", 0.0, None),
        ("overactive penalty", overactive_penalty, "plasma", 0.0, None),
    ]
    for ax, (title, values, cmap, vmin, vmax) in zip(axes, panels):
        im = ax.imshow(
            values,
            origin="lower",
            aspect="auto",
            extent=[
                DRIFT_VALUES[0],
                DRIFT_VALUES[-1],
                ANISOTROPY_VALUES[0],
                ANISOTROPY_VALUES[-1],
            ],
            cmap=cmap,
            vmin=vmin if vmin is not None else float(values.min()),
            vmax=vmax if vmax is not None else float(values.max()),
        )
        ax.set_title(title)
        ax.set_xlabel("drift cycles over memory")
        ax.set_ylabel("hardware anisotropy")
        fig.colorbar(im, ax=ax)
    fig.suptitle("Hardware adaptive decoder: same code, drifting non-iid noise")
    fig.savefig(HEATMAP_PATH, dpi=180)
    plt.close(fig)


def write_curves(rows: list[dict[str, float | str]]) -> None:
    selected_anisotropies = [0.0, 0.6, 1.2, 1.8]
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), constrained_layout=True)

    for target in selected_anisotropies:
        anisotropy = min(ANISOTROPY_VALUES, key=lambda x: abs(float(x) - target))
        adaptive = [
            r
            for r in protocol_rows(rows, "adaptive_decoder")
            if abs(float(r["anisotropy"]) - float(anisotropy)) < 1e-9
        ]
        adaptive.sort(key=lambda r: float(r["drift_cycles"]))
        x = [float(r["drift_cycles"]) for r in adaptive]
        axes[0].plot(
            x,
            [float(r["adaptive_benefit_log10"]) for r in adaptive],
            label=f"anisotropy={float(anisotropy):.2f}",
        )
        axes[1].plot(
            x,
            [float(r["logical_error"]) for r in adaptive],
            label=f"anisotropy={float(anisotropy):.2f}",
        )

    axes[0].axhline(0.0, color="black", linewidth=1.0, alpha=0.5)
    axes[0].set_title("Benefit over best static decoder")
    axes[0].set_xlabel("drift cycles over memory")
    axes[0].set_ylabel("log10(error_static / error_adaptive)")
    axes[0].grid(alpha=0.25)
    axes[0].legend()

    axes[1].set_title("Adaptive logical error")
    axes[1].set_xlabel("drift cycles over memory")
    axes[1].set_ylabel("logical bit-flip probability")
    axes[1].grid(alpha=0.25)
    axes[1].legend()

    fig.savefig(CURVES_PATH, dpi=180)
    plt.close(fig)


def main() -> None:
    rows = scan()
    write_csv(rows)
    write_heatmap(rows)
    write_curves(rows)

    adaptive = protocol_rows(rows, "adaptive_decoder")
    best_adaptive = max(adaptive, key=lambda r: float(r["adaptive_benefit_log10"]))
    best_overall = min(rows, key=lambda r: float(r["logical_error"]))
    best_counts: dict[str, int] = {}
    for row in adaptive:
        best_counts[str(row["best_protocol"])] = best_counts.get(str(row["best_protocol"]), 0) + 1

    print(f"wrote {CSV_PATH}")
    print(f"wrote {HEATMAP_PATH}")
    print(f"wrote {CURVES_PATH}")
    print(
        "max adaptive benefit: "
        f"{float(best_adaptive['adaptive_benefit_log10']):.3f} log10 at "
        f"anisotropy={float(best_adaptive['anisotropy']):.3f}, "
        f"drift={float(best_adaptive['drift_cycles']):.3f}"
    )
    print(
        "best logical error: "
        f"{float(best_overall['logical_error']):.5f} from {best_overall['protocol']} "
        f"at anisotropy={float(best_overall['anisotropy']):.3f}, "
        f"drift={float(best_overall['drift_cycles']):.3f}"
    )
    print(f"best protocol counts over grid: {best_counts}")


if __name__ == "__main__":
    main()
