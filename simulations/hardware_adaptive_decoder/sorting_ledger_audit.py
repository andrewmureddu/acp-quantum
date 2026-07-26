#!/usr/bin/env python3
"""Sorting-efficiency audit for the H2 circuit-level syndrome extraction.

This measures the crystallization sorting engine's diagnostic chi on the
existing OP-23 hardware scaffold. It imports the H2 circuit primitives
unchanged from `circuit_level_syndrome_decoder.py`, so the fault model, the
parity-extraction circuit, the decoder policies, and the calibration/drift
schedule are exactly those already audited for logical error.

See `bridges/crystallization_sorting_engine.md` for the ledger.

Question
--------
An unknown data-qubit error appears. How much of its distinguishability
reaches the decoder as syndrome, and how much is scrambled away by subsequent
circuit noise before it can be extracted?

Probe
-----
At the start of each measurement window the data register is placed in an
unknown error configuration `S0`, uniform over the eight three-qubit states.
The window then runs the ordinary H2 rounds with the protocol's real decoder
state, carried forward from round 0 of the full trace so that drift and
calibration history are faithful.

The joint distribution over `(S0, D_k, R_{<=k})` is propagated exactly: every
one of the `4**window` syndrome histories is retained, with no sampling, no
pruning, and no branch merging.

Ledger
------
    T_k = I(S0; D_k, R_{<=k})     E_k = I(S0; R_{<=k})     J_k = I(S0; D_k | R)
    gamma_k = J_k - J_{k+1}       sigma_k = E_{k+1} - E_k  delta_k = T_k - T_{k+1}
    chi = sum(sigma) / sum(gamma)

Reference splits
----------------
`S0` factors bijectively as `(G0, L0)`:

    G0 = the syndrome class (e0^e1, e1^e2), two bits, the code's error sector;
    L0 = the logical component of the initial error, one bit.

The stabilizer group is the sorter's slot partition. For an [[n,k]] code it has
`n - k` bits of resolution against `n` bits of error space, so the resolution
ceiling of Corollary 4.2 is exactly

    chi <= (n - k) / n = 2/3       for this [[3,1]] repetition memory,

and the missing third is not waste: it is the logical label the code is
designed to be blind to. The sector ledger on `G0` has ceiling 1, so its
shortfall is genuine sorting loss. The protected ledger reports
`I(L0; R | G0)`, which Knill-Laflamme requires to vanish.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import replace
from pathlib import Path

import numpy as np

from circuit_level_syndrome_decoder import (
    DEFAULT_ANISOTROPY,
    DEFAULT_CALIBRATION_PERIOD,
    DEFAULT_CROSSTALK_SCALE,
    DEFAULT_DRIFT_CYCLES,
    DEFAULT_LEAKAGE_SCALE,
    DEFAULT_ROUNDS,
    DEFAULT_SEED,
    CIRCUIT_PROTOCOLS,
    CircuitRound,
    apply_state_faults,
    clip_probability,
    decoder_proxy_meas,
    decoder_proxy_rates,
    generate_circuit_trace,
    logical_bit,
    observed_tuple,
    pre_correction_distribution,
    should_update,
)
from hardware_adaptive_decoder import (
    CHARACTERIZATION_DATA_ERROR,
    MEASUREMENT_ERROR,
    BASE_DATA_ERROR,
    N_QUBITS,
    N_STATES,
    Protocol,
    choose_correction,
    correction_mask,
)


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
LEDGER_PATH = OUT / "sorting_ledger_timeseries.csv"
SUMMARY_PATH = OUT / "sorting_ledger_summary.csv"
EXTRACTION_PATH = OUT / "sorting_ledger_extraction_scan.csv"

N_RECORDS = 4
DEFAULT_WINDOW = 8
DEFAULT_WINDOW_STARTS = (0, 44, 52, 60, 72, 88)

RECORD_CAPACITY_BITS = math.log2(N_RECORDS)
RESOLUTION_CEILING = math.log2(N_RECORDS) / math.log2(N_STATES)

SECTOR_OF_STATE = np.array(
    [
        (((state & 1) ^ ((state >> 1) & 1)) << 1) | (((state >> 1) & 1) ^ ((state >> 2) & 1))
        for state in range(N_STATES)
    ],
    dtype=int,
)
LOGICAL_OF_STATE = np.array([logical_bit(state) for state in range(N_STATES)], dtype=int)


# --------------------------------------------------------------------------
# information helpers
# --------------------------------------------------------------------------


def clamp(value: float, tolerance: float = 1e-12) -> float:
    return 0.0 if abs(value) < tolerance else float(value)


def rowwise_entropy(table: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Mass and Shannon entropy (bits) of each row of a non-negative table."""

    mass = table.sum(axis=-1)
    safe = np.where(mass[..., None] > 0.0, mass[..., None], 1.0)
    p = table / safe
    logs = np.where(p > 0.0, np.log2(np.where(p > 0.0, p, 1.0)), 0.0)
    return mass, -(p * logs).sum(axis=-1)


def conditional_entropy(table: np.ndarray) -> float:
    """H(last axis | all preceding axes) for a joint distribution."""

    mass, entropy = rowwise_entropy(table)
    return float((mass * entropy).sum())


def ledger_columns(joint: np.ndarray, reference: np.ndarray, n_reference: int) -> dict[str, float]:
    """Ledger columns for a reference variable that is a function of S0.

    `joint` has shape (branches, S0, D). Theorem 1 applies to any such
    reference: the update channel never consults S0, so it cannot consult a
    function of S0 either, and the record register is still retained.
    """

    branches, _, n_data = joint.shape
    grouped = np.zeros((branches, n_reference, n_data), dtype=float)
    for value in range(n_reference):
        mask = reference == value
        grouped[:, value, :] = joint[:, mask, :].sum(axis=1)

    prior = grouped.sum(axis=(0, 2))
    _, prior_entropy = rowwise_entropy(prior)
    h_prior = float(prior_entropy)

    # E = I(ref; R): condition on the record branch only.
    by_record = grouped.sum(axis=2)
    exported = h_prior - conditional_entropy(by_record)

    # T = I(ref; D, R): condition on the record branch and the data register.
    by_record_and_data = np.transpose(grouped, (0, 2, 1))
    total = h_prior - conditional_entropy(by_record_and_data)

    return {
        "total": clamp(total, 1e-12),
        "exported": clamp(exported, 1e-12),
        "retained": clamp(total - exported, 1e-12),
        "prior": h_prior,
    }


def conditional_ledger_columns(joint: np.ndarray) -> dict[str, float]:
    """Ledger columns for L0 conditioned on the sector G0."""

    branches, _, n_data = joint.shape
    total = 0.0
    exported = 0.0
    for sector in range(N_RECORDS):
        members = np.where(SECTOR_OF_STATE == sector)[0]
        block = joint[:, members, :]
        weight = float(block.sum())
        if weight <= 0.0:
            continue
        # order the two coset members by their logical label
        order = np.argsort(LOGICAL_OF_STATE[members])
        block = block[:, order, :] / weight

        prior = block.sum(axis=(0, 2))
        _, prior_entropy = rowwise_entropy(prior)
        h_prior = float(prior_entropy)

        by_record = block.sum(axis=2)
        by_record_and_data = np.transpose(block, (0, 2, 1))
        exported += weight * (h_prior - conditional_entropy(by_record))
        total += weight * (h_prior - conditional_entropy(by_record_and_data))

    return {
        "total": clamp(total, 1e-12),
        "exported": clamp(exported, 1e-12),
        "retained": clamp(total - exported, 1e-12),
    }


# --------------------------------------------------------------------------
# round kernel
# --------------------------------------------------------------------------


def round_kernel(
    noise,
    estimated_rates: np.ndarray,
    estimated_meas: float,
    update_overhead: bool,
) -> np.ndarray:
    """K[d, r, d'] = P(record r and next data state d' | current data state d).

    This is `circuit_round_transition` with the syndrome record kept instead of
    marginalized away. Summing over r reproduces that transition matrix exactly.
    """

    kernel = np.zeros((N_STATES, N_RECORDS, N_STATES), dtype=float)
    p_fail = clip_probability(noise.correction_error, upper=0.49)

    for source in range(N_STATES):
        by_record: dict[int, dict[int, float]] = {}
        for (data, record), probability in pre_correction_distribution(source, noise).items():
            correction = correction_mask(
                choose_correction(observed_tuple(record), estimated_rates, estimated_meas)
            )
            bucket = by_record.setdefault(record, {})
            if correction == 0:
                bucket[data] = bucket.get(data, 0.0) + probability
            else:
                target = data ^ correction
                bucket[target] = bucket.get(target, 0.0) + probability * (1.0 - p_fail)
                bucket[data] = bucket.get(data, 0.0) + probability * p_fail

        for record, bucket in by_record.items():
            if update_overhead:
                bucket = apply_state_faults(
                    bucket, np.full(N_QUBITS, CHARACTERIZATION_DATA_ERROR, dtype=float)
                )
            for target, probability in bucket.items():
                kernel[source, record, target] += probability

    column_sums = kernel.sum(axis=(1, 2))
    if not np.allclose(column_sums, 1.0, atol=1e-10):
        raise RuntimeError(f"non-stochastic record kernel: {column_sums}")
    return kernel


# --------------------------------------------------------------------------
# decoder replay
# --------------------------------------------------------------------------


def replay_decoder_state(
    protocol: Protocol, trace: list[CircuitRound]
) -> list[tuple[np.ndarray, float, bool]]:
    """Reproduce the decoder state of `run_circuit_protocol`, round by round."""

    initial = trace[0]
    if protocol.mode == "uniform":
        estimated_rates = np.full(N_QUBITS, BASE_DATA_ERROR, dtype=float)
        estimated_meas = MEASUREMENT_ERROR
    elif protocol.mode in {"static", "adaptive"}:
        estimated_rates = initial.calib_rates.copy()
        estimated_meas = initial.calib_meas
    elif protocol.mode == "oracle":
        estimated_rates = decoder_proxy_rates(initial.noise)
        estimated_meas = decoder_proxy_meas(initial.noise)
    else:
        raise ValueError(f"unknown protocol mode {protocol.mode!r}")

    schedule: list[tuple[np.ndarray, float, bool]] = []
    for item in trace:
        update_this_round = False
        if protocol.mode == "oracle":
            estimated_rates = decoder_proxy_rates(item.noise)
            estimated_meas = decoder_proxy_meas(item.noise)
        elif protocol.name == "overactive_decoder":
            estimated_rates = item.calib_rates.copy()
            estimated_meas = item.calib_meas
            update_this_round = True
        elif protocol.name == "adaptive_decoder" and item.calibration_fresh:
            if should_update(estimated_rates, estimated_meas, item.calib_rates, item.calib_meas):
                estimated_rates = item.calib_rates.copy()
                estimated_meas = item.calib_meas
                update_this_round = True
        schedule.append((estimated_rates.copy(), float(estimated_meas), update_this_round))
    return schedule


# --------------------------------------------------------------------------
# window audit
# --------------------------------------------------------------------------


def audit_window(
    protocol: Protocol,
    trace: list[CircuitRound],
    schedule: list[tuple[np.ndarray, float, bool]],
    start: int,
    length: int,
) -> list[dict[str, float | str]]:
    joint = np.zeros((1, N_STATES, N_STATES), dtype=float)
    for state in range(N_STATES):
        joint[0, state, state] = 1.0 / N_STATES

    full = ledger_columns(joint, np.arange(N_STATES), N_STATES)
    sector = ledger_columns(joint, SECTOR_OF_STATE, N_RECORDS)
    protected = conditional_ledger_columns(joint)

    rows: list[dict[str, float | str]] = [
        {
            "protocol": protocol.name,
            "window_start": start,
            "step": 0,
            "round": start,
            "updated": 0.0,
            "total_bits": full["total"],
            "exported_bits": full["exported"],
            "retained_bits": full["retained"],
            "contraction_bits": 0.0,
            "sorted_bits": 0.0,
            "destroyed_bits": 0.0,
            "sector_total_bits": sector["total"],
            "sector_exported_bits": sector["exported"],
            "sector_retained_bits": sector["retained"],
            "sector_contraction_bits": 0.0,
            "sector_sorted_bits": 0.0,
            "sector_destroyed_bits": 0.0,
            "protected_exported_bits": protected["exported"],
            "protected_retained_bits": protected["retained"],
            "capacity_bits": 0.0,
            "record_entropy_bits": 0.0,
            "branches": 1,
        }
    ]

    for step in range(length):
        index = start + step
        estimated_rates, estimated_meas, update_this_round = schedule[index]
        kernel = round_kernel(
            trace[index].noise, estimated_rates, estimated_meas, update_this_round
        )

        expanded = np.einsum("bsd,drp->brsp", joint, kernel, optimize=True)
        record_mass = expanded.sum(axis=(2, 3))
        branch_mass, branch_record_entropy = rowwise_entropy(record_mass)
        record_entropy = float((branch_mass * branch_record_entropy).sum())
        joint = expanded.reshape(-1, N_STATES, N_STATES)

        previous_full, previous_sector, previous_protected = full, sector, protected
        full = ledger_columns(joint, np.arange(N_STATES), N_STATES)
        sector = ledger_columns(joint, SECTOR_OF_STATE, N_RECORDS)
        protected = conditional_ledger_columns(joint)

        rows.append(
            {
                "protocol": protocol.name,
                "window_start": start,
                "step": step + 1,
                "round": index + 1,
                "updated": float(update_this_round),
                "total_bits": full["total"],
                "exported_bits": full["exported"],
                "retained_bits": full["retained"],
                "contraction_bits": clamp(
                    previous_full["retained"] - full["retained"], 1e-12
                ),
                "sorted_bits": clamp(full["exported"] - previous_full["exported"], 1e-12),
                "destroyed_bits": clamp(previous_full["total"] - full["total"], 1e-12),
                "sector_total_bits": sector["total"],
                "sector_exported_bits": sector["exported"],
                "sector_retained_bits": sector["retained"],
                "sector_contraction_bits": clamp(
                    previous_sector["retained"] - sector["retained"], 1e-12
                ),
                "sector_sorted_bits": clamp(
                    sector["exported"] - previous_sector["exported"], 1e-12
                ),
                "sector_destroyed_bits": clamp(
                    previous_sector["total"] - sector["total"], 1e-12
                ),
                "protected_exported_bits": protected["exported"],
                "protected_retained_bits": protected["retained"],
                "capacity_bits": RECORD_CAPACITY_BITS,
                "record_entropy_bits": clamp(record_entropy, 1e-12),
                "branches": joint.shape[0],
            }
        )
        del previous_protected

    return rows


def summarize_window(rows: list[dict[str, float | str]]) -> dict[str, float | str]:
    body = rows[1:]
    contraction = clamp(sum(float(r["contraction_bits"]) for r in body), 1e-12)
    sorted_bits = clamp(sum(float(r["sorted_bits"]) for r in body), 1e-12)
    destroyed = clamp(sum(float(r["destroyed_bits"]) for r in body), 1e-12)
    sector_contraction = clamp(sum(float(r["sector_contraction_bits"]) for r in body), 1e-12)
    sector_sorted = clamp(sum(float(r["sector_sorted_bits"]) for r in body), 1e-12)
    sector_destroyed = clamp(sum(float(r["sector_destroyed_bits"]) for r in body), 1e-12)

    identity = max(
        abs(
            float(r["contraction_bits"]) - float(r["sorted_bits"]) - float(r["destroyed_bits"])
        )
        for r in body
    )
    record_bound = max(float(r["sorted_bits"]) - float(r["contraction_bits"]) for r in body)
    noise_bound = max(
        float(r["sorted_bits"]) - float(r["record_entropy_bits"]) for r in body
    )
    peak_capacity_use = max(
        float(r["record_entropy_bits"]) / float(r["capacity_bits"]) for r in body
    )
    peak_contraction_use = max(
        float(r["contraction_bits"]) / float(r["capacity_bits"]) for r in body
    )
    bandwidth_violation = min(
        float(r["destroyed_bits"])
        - max(0.0, float(r["contraction_bits"]) - float(r["capacity_bits"]))
        for r in body
    )
    limited = sum(
        1 for r in body if float(r["contraction_bits"]) > float(r["capacity_bits"]) + 1e-12
    )

    return {
        "protocol": rows[0]["protocol"],
        "window_start": rows[0]["window_start"],
        "window_length": len(body),
        "updates_in_window": sum(float(r["updated"]) for r in body),
        "contraction_bits": round(contraction, 6),
        "sorted_bits": round(sorted_bits, 6),
        "destroyed_bits": round(destroyed, 6),
        "chi": round(sorted_bits / contraction, 6) if contraction > 1e-12 else "",
        "chi_resolution_ceiling": round(RESOLUTION_CEILING, 6),
        "sector_contraction_bits": round(sector_contraction, 6),
        "sector_sorted_bits": round(sector_sorted, 6),
        "sector_destroyed_bits": round(sector_destroyed, 6),
        "chi_sector": (
            round(sector_sorted / sector_contraction, 6) if sector_contraction > 1e-12 else ""
        ),
        "final_retained_bits": round(float(rows[-1]["retained_bits"]), 6),
        "final_protected_retained_bits": round(float(rows[-1]["protected_retained_bits"]), 6),
        "max_protected_leakage_bits": round(
            max(float(r["protected_exported_bits"]) for r in rows), 9
        ),
        "max_identity_residual": f"{identity:.3e}",
        "max_sigma_minus_gamma": f"{record_bound:.3e}",
        "max_sigma_minus_record_entropy": f"{noise_bound:.3e}",
        "peak_record_entropy_over_capacity": round(peak_capacity_use, 6),
        "peak_contraction_over_capacity": round(peak_contraction_use, 6),
        "window_chi_ceiling": (
            round(2.0 / (3.0 - float(rows[-1]["retained_bits"])), 6)
            if float(rows[-1]["retained_bits"]) < 3.0
            else ""
        ),
        "max_bandwidth_violation": f"{min(0.0, bandwidth_violation):.3e}",
        "bandwidth_limited_steps": limited,
    }


def write_csv(path: Path, rows: list[dict[str, float | str]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


EXTRACTION_SCALES = (0.25, 0.5, 1.0, 2.0, 4.0)


def scaled_trace(trace: list[CircuitRound], scale: float) -> list[CircuitRound]:
    """Rescale the ancilla/readout fault rates that set the sorter's fidelity.

    The data-qubit fault rates are untouched, so the interior contraction is
    unchanged and only the quality of the extraction channel varies.
    """

    out: list[CircuitRound] = []
    for item in trace:
        noise = replace(
            item.noise,
            meas_error=clip_probability(item.noise.meas_error * scale, upper=0.49),
            prep_error=clip_probability(item.noise.prep_error * scale, upper=0.49),
            ancilla_gate=clip_probability(item.noise.ancilla_gate * scale, upper=0.49),
            leakage_error=clip_probability(item.noise.leakage_error * scale, upper=0.49),
        )
        out.append(replace(item, noise=noise))
    return out


def extraction_scan(
    trace: list[CircuitRound], starts: list[int], window: int
) -> list[dict[str, float | str]]:
    """Contrast decoder quality against extraction quality.

    Theorem 4 says chi is set by the record channel. This scan varies the
    channel while holding the data-qubit noise and the decoder fixed.
    """

    protocol = CIRCUIT_PROTOCOLS[0]
    rows: list[dict[str, float | str]] = []
    for scale in EXTRACTION_SCALES:
        variant = scaled_trace(trace, scale)
        schedule = replay_decoder_state(protocol, variant)
        for start in starts:
            summary = summarize_window(
                audit_window(protocol, variant, schedule, start, window)
            )
            rows.append(
                {
                    "extraction_scale": scale,
                    "window_start": start,
                    "contraction_bits": summary["contraction_bits"],
                    "sorted_bits": summary["sorted_bits"],
                    "destroyed_bits": summary["destroyed_bits"],
                    "chi": summary["chi"],
                    "chi_sector": summary["chi_sector"],
                }
            )
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rounds", type=int, default=DEFAULT_ROUNDS)
    parser.add_argument("--window", type=int, default=DEFAULT_WINDOW)
    parser.add_argument(
        "--window-starts",
        type=int,
        nargs="+",
        default=list(DEFAULT_WINDOW_STARTS),
    )
    parser.add_argument("--anisotropy", type=float, default=DEFAULT_ANISOTROPY)
    parser.add_argument("--drift-cycles", type=float, default=DEFAULT_DRIFT_CYCLES)
    parser.add_argument("--calibration-period", type=int, default=DEFAULT_CALIBRATION_PERIOD)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--crosstalk-scale", type=float, default=DEFAULT_CROSSTALK_SCALE)
    parser.add_argument("--leakage-scale", type=float, default=DEFAULT_LEAKAGE_SCALE)
    parser.add_argument("--skip-extraction-scan", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    trace = generate_circuit_trace(
        None,
        total_rounds=args.rounds,
        anisotropy=args.anisotropy,
        drift_cycles=args.drift_cycles,
        calibration_period=args.calibration_period,
        seed=args.seed,
        crosstalk_scale=args.crosstalk_scale,
        leakage_scale=args.leakage_scale,
    )

    starts = [s for s in args.window_starts if s + args.window <= len(trace)]
    if not starts:
        raise SystemExit("no window fits inside the trace")

    all_rows: list[dict[str, float | str]] = []
    summaries: list[dict[str, float | str]] = []
    for protocol in CIRCUIT_PROTOCOLS:
        schedule = replay_decoder_state(protocol, trace)
        for start in starts:
            rows = audit_window(protocol, trace, schedule, start, args.window)
            all_rows.extend(rows)
            summaries.append(summarize_window(rows))

    write_csv(LEDGER_PATH, all_rows)
    write_csv(SUMMARY_PATH, summaries)

    extraction_rows: list[dict[str, float | str]] = []
    if not args.skip_extraction_scan:
        extraction_rows = extraction_scan(trace, starts[:2], args.window)
        write_csv(EXTRACTION_PATH, extraction_rows)

    print(
        f"H(S0) = {math.log2(N_STATES):.6f} bits; "
        f"syndrome resolution = {math.log2(N_RECORDS):.6f} bits; "
        f"chi ceiling = {RESOLUTION_CEILING:.6f}"
    )
    print(f"window length {args.window} rounds, starts {starts}")
    print(f"wrote {LEDGER_PATH}")
    print(f"wrote {SUMMARY_PATH}")
    print()
    header = (
        f"{'protocol':<22}{'start':>6}{'upd':>5}{'gamma':>9}{'sigma':>9}"
        f"{'delta':>9}{'chi':>9}{'chi_G':>9}{'leakL':>11}"
    )
    print(header)
    print("-" * len(header))
    for row in summaries:
        print(
            f"{row['protocol']:<22}{row['window_start']:>6}"
            f"{int(float(row['updates_in_window'])):>5}"
            f"{row['contraction_bits']:>9.5f}{row['sorted_bits']:>9.5f}"
            f"{row['destroyed_bits']:>9.5f}"
            f"{float(row['chi']):>9.5f}{float(row['chi_sector']):>9.5f}"
            f"{float(row['max_protected_leakage_bits']):>11.2e}"
        )

    if extraction_rows:
        print()
        print("extraction-quality scan (uniform decoder, data-qubit noise fixed)")
        print(f"{'scale':>7}{'start':>7}{'gamma':>9}{'sigma':>9}{'chi':>9}{'chi_G':>9}")
        for row in extraction_rows:
            print(
                f"{float(row['extraction_scale']):>7.2f}{int(row['window_start']):>7}"
                f"{float(row['contraction_bits']):>9.5f}{float(row['sorted_bits']):>9.5f}"
                f"{float(row['chi']):>9.5f}{float(row['chi_sector']):>9.5f}"
            )

    print()
    for row in summaries:
        print(
            f"{row['protocol']}@{row['window_start']}: "
            f"identity {row['max_identity_residual']}, "
            f"max(sigma-gamma) {row['max_sigma_minus_gamma']}, "
            f"max(sigma-H(R|R)) {row['max_sigma_minus_record_entropy']}, "
            f"peak gamma/C {row['peak_contraction_over_capacity']}, "
            f"bandwidth violation {row['max_bandwidth_violation']}, "
            f"{row['bandwidth_limited_steps']} bandwidth-limited steps"
        )


if __name__ == "__main__":
    main()
