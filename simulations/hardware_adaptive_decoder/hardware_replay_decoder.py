#!/usr/bin/env python3
"""Replay a hardware-style calibration trace through fixed-code decoders.

This is the H1 scaffold for adaptive syndrome alignment. The trace format is
deliberately simple: each row supplies a reconstructed per-round physical
channel and the calibration record available to the controller. Real backend
logs can replace the generated example trace once they are available.

The logical code is still the same 3-qubit repetition memory used by
hardware_adaptive_decoder.py. The replay changes only decoder likelihoods and
counts update overhead; it never changes the protected logical channel.
"""

from __future__ import annotations

import argparse
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

from hardware_adaptive_decoder import (
    BASE_DATA_ERROR,
    MEASUREMENT_ERROR,
    N_QUBITS,
    N_STATES,
    Protocol,
    Q_STATES,
    candidate_priors,
    correction_mask,
    measurement_probability,
    q_eta_floor,
    round_transition,
    syndrome_for_candidate,
)


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
TRACE_PATH = OUT / "hardware_replay_trace.csv"
SUMMARY_PATH = OUT / "hardware_replay_summary.csv"
TIMESERIES_PATH = OUT / "hardware_replay_timeseries.csv"
CURVES_PATH = OUT / "hardware_replay_curves.png"

DEFAULT_ROUNDS = 96
DEFAULT_ANISOTROPY = 1.35
DEFAULT_DRIFT_CYCLES = 1.25
DEFAULT_CALIBRATION_PERIOD = 8
DEFAULT_CALIBRATION_SHOTS = 4000
DEFAULT_SEED = 1729

UPDATE_L1_THRESHOLD = 0.0020
UPDATE_BENEFIT_LOG10_THRESHOLD = 0.0025
UPDATE_LOOKAHEAD_ROUNDS = DEFAULT_CALIBRATION_PERIOD

REPLAY_PROTOCOLS = [
    Protocol("uniform_decoder", "uniform"),
    Protocol("static_tailored", "static"),
    Protocol("adaptive_decoder", "adaptive"),
    Protocol("overactive_decoder", "adaptive"),
    Protocol("oracle_decoder", "oracle"),
]


@dataclass(frozen=True)
class ReplayRound:
    round_index: int
    channel_rates: np.ndarray
    channel_meas: float
    calib_rates: np.ndarray
    calib_meas: float
    calibration_fresh: bool
    syndrome_rate_01: float
    syndrome_rate_12: float


def clip_rates(values: np.ndarray) -> np.ndarray:
    return np.clip(np.asarray(values, dtype=float), 1e-6, 0.24)


def clip_measurement(value: float) -> float:
    return float(np.clip(value, 1e-6, 0.24))


def parity_observed_rate(pa: float, pb: float, meas_error: float) -> float:
    """Single-round observed parity-event probability for two data rates."""

    true_parity = pa * (1.0 - pb) + (1.0 - pa) * pb
    return float(true_parity * (1.0 - meas_error) + (1.0 - true_parity) * meas_error)


def synthetic_channel_rates(
    round_index: int,
    total_rounds: int,
    anisotropy: float,
    drift_cycles: float,
) -> np.ndarray:
    """Hardware-like non-iid data-qubit rates with drift and one crosstalk burst."""

    total = max(1, total_rounds - 1)
    t = round_index / total
    phase = 2.0 * np.pi * drift_cycles * t
    offsets = np.array([0.0, 2.0 * np.pi / 3.0, 4.0 * np.pi / 3.0])
    logits = anisotropy * np.cos(phase - offsets)
    weights = np.exp(logits)
    weights /= float(np.mean(weights))

    rates = BASE_DATA_ERROR * weights
    burst = 0.010 * math.exp(-0.5 * ((t - 0.62) / 0.09) ** 2)
    rates[1] += burst
    rates[2] += 0.55 * burst
    rates[0] *= 1.0 + 0.20 * math.sin(2.0 * np.pi * t)
    return clip_rates(rates)


def synthetic_measurement_error(round_index: int, total_rounds: int) -> float:
    total = max(1, total_rounds - 1)
    t = round_index / total
    slow = MEASUREMENT_ERROR * (1.0 + 0.25 * math.sin(2.0 * np.pi * (t + 0.15)))
    bump = 0.0035 * math.exp(-0.5 * ((t - 0.58) / 0.11) ** 2)
    return clip_measurement(slow + bump)


def generate_synthetic_trace(
    path: Path,
    total_rounds: int = DEFAULT_ROUNDS,
    anisotropy: float = DEFAULT_ANISOTROPY,
    drift_cycles: float = DEFAULT_DRIFT_CYCLES,
    calibration_period: int = DEFAULT_CALIBRATION_PERIOD,
    calibration_shots: int = DEFAULT_CALIBRATION_SHOTS,
    seed: int = DEFAULT_SEED,
) -> None:
    """Write a seeded hardware-like trace for replay development."""

    rng = np.random.default_rng(seed)
    path.parent.mkdir(parents=True, exist_ok=True)

    current_calib_rates = synthetic_channel_rates(0, total_rounds, anisotropy, drift_cycles)
    current_calib_meas = synthetic_measurement_error(0, total_rounds)
    rows: list[dict[str, float | int | str]] = []

    for round_index in range(total_rounds):
        rates = synthetic_channel_rates(round_index, total_rounds, anisotropy, drift_cycles)
        meas = synthetic_measurement_error(round_index, total_rounds)
        fresh = round_index % max(1, calibration_period) == 0

        if fresh:
            rate_sigma = 0.00045 + 0.10 * rates
            current_calib_rates = clip_rates(rates + rng.normal(0.0, rate_sigma))
            current_calib_meas = clip_measurement(
                meas + float(rng.normal(0.0, 0.00045 + 0.08 * meas))
            )

        syn01 = parity_observed_rate(float(rates[0]), float(rates[1]), meas)
        syn12 = parity_observed_rate(float(rates[1]), float(rates[2]), meas)
        syn01_obs = rng.binomial(calibration_shots, syn01) / calibration_shots
        syn12_obs = rng.binomial(calibration_shots, syn12) / calibration_shots

        rows.append(
            {
                "round": round_index,
                "channel_p0": float(rates[0]),
                "channel_p1": float(rates[1]),
                "channel_p2": float(rates[2]),
                "channel_meas": meas,
                "calib_p0": float(current_calib_rates[0]),
                "calib_p1": float(current_calib_rates[1]),
                "calib_p2": float(current_calib_rates[2]),
                "calib_meas": current_calib_meas,
                "calibration_fresh": int(fresh),
                "syndrome_rate_01": float(syn01_obs),
                "syndrome_rate_12": float(syn12_obs),
                "source": "synthetic_h1_trace",
            }
        )

    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def float_field(row: dict[str, str], name: str, fallback: float | None = None) -> float:
    value = row.get(name, "")
    if value == "" or value is None:
        if fallback is None:
            raise ValueError(f"missing required field {name!r}")
        return fallback
    return float(value)


def bool_field(row: dict[str, str], name: str, fallback: bool = True) -> bool:
    value = row.get(name, "")
    if value == "" or value is None:
        return fallback
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def read_trace(path: Path) -> list[ReplayRound]:
    rounds: list[ReplayRound] = []
    with path.open(newline="") as f:
        for row in csv.DictReader(f):
            channel_rates = clip_rates(
                np.array(
                    [
                        float_field(row, "channel_p0"),
                        float_field(row, "channel_p1"),
                        float_field(row, "channel_p2"),
                    ],
                    dtype=float,
                )
            )
            channel_meas = clip_measurement(float_field(row, "channel_meas", MEASUREMENT_ERROR))
            calib_rates = clip_rates(
                np.array(
                    [
                        float_field(row, "calib_p0", float(channel_rates[0])),
                        float_field(row, "calib_p1", float(channel_rates[1])),
                        float_field(row, "calib_p2", float(channel_rates[2])),
                    ],
                    dtype=float,
                )
            )
            calib_meas = clip_measurement(float_field(row, "calib_meas", channel_meas))
            syn01 = float_field(
                row,
                "syndrome_rate_01",
                parity_observed_rate(float(channel_rates[0]), float(channel_rates[1]), channel_meas),
            )
            syn12 = float_field(
                row,
                "syndrome_rate_12",
                parity_observed_rate(float(channel_rates[1]), float(channel_rates[2]), channel_meas),
            )
            rounds.append(
                ReplayRound(
                    round_index=int(float_field(row, "round", float(len(rounds)))),
                    channel_rates=channel_rates,
                    channel_meas=channel_meas,
                    calib_rates=calib_rates,
                    calib_meas=calib_meas,
                    calibration_fresh=bool_field(row, "calibration_fresh", True),
                    syndrome_rate_01=float(syn01),
                    syndrome_rate_12=float(syn12),
                )
            )

    if not rounds:
        raise ValueError(f"trace {path} contained no rows")
    return rounds


def single_round_syndrome_mi(rates: np.ndarray, meas_error: float) -> float:
    """Mutual information I(single-error candidate; observed syndrome), in bits."""

    observed_syndromes = [(0, 0), (1, 0), (1, 1), (0, 1)]
    priors = candidate_priors(rates)
    joint = np.zeros((4, 4), dtype=float)

    for candidate in range(4):
        predicted = syndrome_for_candidate(correction_mask(candidate))
        for s_index, observed in enumerate(observed_syndromes):
            joint[candidate, s_index] = priors[candidate] * measurement_probability(
                observed, predicted, meas_error
            )

    p_error = np.sum(joint, axis=1)
    p_syndrome = np.sum(joint, axis=0)
    mi = 0.0
    for candidate in range(4):
        for s_index in range(4):
            p = float(joint[candidate, s_index])
            if p > 0.0:
                mi += p * math.log2(p / (float(p_error[candidate]) * float(p_syndrome[s_index])))
    return float(mi)


def expected_logical_error(
    proxy_rates: np.ndarray,
    proxy_meas: float,
    decoder_rates: np.ndarray,
    decoder_meas: float,
) -> float:
    state_distribution = np.zeros(N_STATES, dtype=float)
    state_distribution[0] = 1.0
    transition = round_transition(
        proxy_rates,
        decoder_rates,
        decoder_meas,
        update_overhead=False,
        true_meas=proxy_meas,
    )
    for _ in range(UPDATE_LOOKAHEAD_ROUNDS):
        state_distribution = transition @ state_distribution
    return float(np.sum(state_distribution[Q_STATES]))


def should_update(
    current_rates: np.ndarray,
    current_meas: float,
    candidate_rates: np.ndarray,
    candidate_meas: float,
) -> bool:
    """Gate adaptive updates by estimated short-horizon logical improvement."""

    l1_change = float(np.sum(np.abs(candidate_rates - current_rates)))
    l1_change += abs(candidate_meas - current_meas)
    if l1_change < UPDATE_L1_THRESHOLD:
        return False

    old_error = expected_logical_error(candidate_rates, candidate_meas, current_rates, current_meas)
    new_error = expected_logical_error(candidate_rates, candidate_meas, candidate_rates, candidate_meas)
    benefit = math.log10((old_error + 1e-15) / (new_error + 1e-15))
    return benefit >= UPDATE_BENEFIT_LOG10_THRESHOLD


def run_replay_protocol(
    protocol: Protocol,
    trace: list[ReplayRound],
) -> tuple[dict[str, float | str], list[dict[str, float | str]]]:
    uniform_rates = np.full(N_QUBITS, BASE_DATA_ERROR, dtype=float)
    initial = trace[0]

    if protocol.mode == "uniform":
        estimated_rates = uniform_rates.copy()
        estimated_meas = MEASUREMENT_ERROR
    elif protocol.mode in {"static", "adaptive"}:
        estimated_rates = initial.calib_rates.copy()
        estimated_meas = initial.calib_meas
    elif protocol.mode == "oracle":
        estimated_rates = initial.channel_rates.copy()
        estimated_meas = initial.channel_meas
    else:
        raise ValueError(f"unknown protocol mode {protocol.mode!r}")

    state_distribution = np.zeros(N_STATES, dtype=float)
    state_distribution[0] = 1.0
    updates = 0
    average_l1_estimation_error = 0.0
    average_meas_estimation_error = 0.0
    average_syndrome_mi = 0.0
    worst_q = 0.0
    worst_eta = 0.0
    worst_floor = 0.0
    timeseries: list[dict[str, float | str]] = []

    for item in trace:
        update_this_round = False

        if protocol.mode == "oracle":
            estimated_rates = item.channel_rates.copy()
            estimated_meas = item.channel_meas
        elif protocol.name == "overactive_decoder":
            estimated_rates = item.calib_rates.copy()
            estimated_meas = item.calib_meas
            update_this_round = True
            updates += 1
        elif protocol.name == "adaptive_decoder" and item.calibration_fresh:
            if should_update(estimated_rates, estimated_meas, item.calib_rates, item.calib_meas):
                estimated_rates = item.calib_rates.copy()
                estimated_meas = item.calib_meas
                update_this_round = True
                updates += 1

        transition = round_transition(
            item.channel_rates,
            estimated_rates,
            estimated_meas,
            update_overhead=update_this_round,
            true_meas=item.channel_meas,
        )
        q_star, eta_star, floor = q_eta_floor(transition)
        worst_q = max(worst_q, q_star)
        worst_eta = max(worst_eta, eta_star)
        worst_floor = max(worst_floor, floor)

        state_distribution = transition @ state_distribution
        logical_error = float(np.sum(state_distribution[Q_STATES]))
        estimation_l1 = float(np.sum(np.abs(item.channel_rates - estimated_rates)))
        meas_estimation_error = abs(item.channel_meas - estimated_meas)
        syndrome_mi = single_round_syndrome_mi(item.channel_rates, item.channel_meas)

        average_l1_estimation_error += estimation_l1
        average_meas_estimation_error += meas_estimation_error
        average_syndrome_mi += syndrome_mi

        timeseries.append(
            {
                "protocol": protocol.name,
                "round": float(item.round_index),
                "logical_error": logical_error,
                "entanglement_fidelity": 1.0 - logical_error,
                "updated": float(update_this_round),
                "estimate_l1_error": estimation_l1,
                "meas_estimation_error": meas_estimation_error,
                "syndrome_mi_bits": syndrome_mi,
                "q_star": q_star,
                "eta_star": eta_star,
                "alignment_floor": floor,
                "channel_p0": float(item.channel_rates[0]),
                "channel_p1": float(item.channel_rates[1]),
                "channel_p2": float(item.channel_rates[2]),
                "channel_meas": item.channel_meas,
                "calib_p0": float(item.calib_rates[0]),
                "calib_p1": float(item.calib_rates[1]),
                "calib_p2": float(item.calib_rates[2]),
                "calib_meas": item.calib_meas,
                "calibration_fresh": float(item.calibration_fresh),
                "syndrome_rate_01": item.syndrome_rate_01,
                "syndrome_rate_12": item.syndrome_rate_12,
            }
        )

    n_rounds = float(len(trace))
    logical_error = float(np.sum(state_distribution[Q_STATES]))
    summary = {
        "protocol": protocol.name,
        "rounds": n_rounds,
        "logical_error": logical_error,
        "entanglement_fidelity": 1.0 - logical_error,
        "updates": float(updates),
        "avg_l1_estimation_error": average_l1_estimation_error / n_rounds,
        "avg_meas_estimation_error": average_meas_estimation_error / n_rounds,
        "avg_syndrome_mi_bits": average_syndrome_mi / n_rounds,
        "worst_q_star": worst_q,
        "worst_eta_star": worst_eta,
        "worst_alignment_floor": worst_floor,
    }
    return summary, timeseries


def run_replay(
    trace: list[ReplayRound],
) -> tuple[list[dict[str, float | str]], list[dict[str, float | str]]]:
    summaries = []
    timeseries = []
    for protocol in REPLAY_PROTOCOLS:
        summary, protocol_timeseries = run_replay_protocol(protocol, trace)
        summaries.append(summary)
        timeseries.extend(protocol_timeseries)

    static_names = {"uniform_decoder", "static_tailored"}
    best_static_error = min(
        float(row["logical_error"]) for row in summaries if row["protocol"] in static_names
    )
    adaptive_error = next(
        float(row["logical_error"]) for row in summaries if row["protocol"] == "adaptive_decoder"
    )
    overactive_error = next(
        float(row["logical_error"]) for row in summaries if row["protocol"] == "overactive_decoder"
    )
    oracle_error = next(
        float(row["logical_error"]) for row in summaries if row["protocol"] == "oracle_decoder"
    )
    best_protocol = str(min(summaries, key=lambda row: float(row["logical_error"]))["protocol"])

    for row in summaries:
        row["best_static_logical_error"] = best_static_error
        row["adaptive_benefit_log10"] = math.log10(
            (best_static_error + 1e-15) / (adaptive_error + 1e-15)
        )
        row["overactive_penalty_log10"] = math.log10(
            (overactive_error + 1e-15) / (adaptive_error + 1e-15)
        )
        row["oracle_gap_log10"] = math.log10(
            (adaptive_error + 1e-15) / (oracle_error + 1e-15)
        )
        row["best_protocol"] = best_protocol

    return summaries, timeseries


def write_csv(path: Path, rows: list[dict[str, float | str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def protocol_series(
    rows: list[dict[str, float | str]], protocol: str
) -> list[dict[str, float | str]]:
    result = [row for row in rows if row["protocol"] == protocol]
    result.sort(key=lambda row: float(row["round"]))
    return result


def write_curves(
    trace: list[ReplayRound],
    summaries: list[dict[str, float | str]],
    timeseries: list[dict[str, float | str]],
) -> None:
    fig, axes = plt.subplots(3, 1, figsize=(11, 10), constrained_layout=True)

    for summary in summaries:
        protocol = str(summary["protocol"])
        series = protocol_series(timeseries, protocol)
        axes[0].plot(
            [float(row["round"]) for row in series],
            [float(row["logical_error"]) for row in series],
            label=protocol,
            linewidth=1.8,
        )
    axes[0].set_title("Replay logical error by decoder policy")
    axes[0].set_xlabel("round")
    axes[0].set_ylabel("logical failure probability")
    axes[0].grid(alpha=0.25)
    axes[0].legend(ncols=2, fontsize=8)

    x = [item.round_index for item in trace]
    for qubit in range(N_QUBITS):
        axes[1].plot(
            x,
            [float(item.channel_rates[qubit]) for item in trace],
            label=f"channel p{qubit}",
            linewidth=1.6,
        )
        fresh_x = [item.round_index for item in trace if item.calibration_fresh]
        fresh_y = [
            float(item.calib_rates[qubit]) for item in trace if item.calibration_fresh
        ]
        axes[1].scatter(fresh_x, fresh_y, s=18, alpha=0.75)
    axes[1].set_title("Reconstructed data-qubit rates and fresh calibrations")
    axes[1].set_xlabel("round")
    axes[1].set_ylabel("bit-flip probability")
    axes[1].grid(alpha=0.25)
    axes[1].legend(ncols=3, fontsize=8)

    for protocol in ["static_tailored", "adaptive_decoder", "overactive_decoder", "oracle_decoder"]:
        series = protocol_series(timeseries, protocol)
        axes[2].plot(
            [float(row["round"]) for row in series],
            [float(row["estimate_l1_error"]) for row in series],
            label=protocol,
            linewidth=1.6,
        )
    adaptive_series = protocol_series(timeseries, "adaptive_decoder")
    update_rounds = [
        float(row["round"]) for row in adaptive_series if float(row["updated"]) > 0.5
    ]
    for update_round in update_rounds:
        axes[2].axvline(update_round, color="black", linewidth=0.7, alpha=0.18)
    axes[2].set_title("Decoder-estimate error; vertical marks are gated adaptive updates")
    axes[2].set_xlabel("round")
    axes[2].set_ylabel("L1 rate-estimation error")
    axes[2].grid(alpha=0.25)
    axes[2].legend(ncols=2, fontsize=8)

    fig.suptitle("Hardware trace replay: fixed logical code, adaptive likelihoods")
    fig.savefig(CURVES_PATH, dpi=180)
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trace", type=Path, default=TRACE_PATH)
    parser.add_argument("--generate-example", action="store_true")
    parser.add_argument("--rounds", type=int, default=DEFAULT_ROUNDS)
    parser.add_argument("--anisotropy", type=float, default=DEFAULT_ANISOTROPY)
    parser.add_argument("--drift-cycles", type=float, default=DEFAULT_DRIFT_CYCLES)
    parser.add_argument("--calibration-period", type=int, default=DEFAULT_CALIBRATION_PERIOD)
    parser.add_argument("--calibration-shots", type=int, default=DEFAULT_CALIBRATION_SHOTS)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    trace_path = args.trace

    if args.generate_example or not trace_path.exists():
        generate_synthetic_trace(
            trace_path,
            total_rounds=args.rounds,
            anisotropy=args.anisotropy,
            drift_cycles=args.drift_cycles,
            calibration_period=args.calibration_period,
            calibration_shots=args.calibration_shots,
            seed=args.seed,
        )

    trace = read_trace(trace_path)
    summaries, timeseries = run_replay(trace)
    write_csv(SUMMARY_PATH, summaries)
    write_csv(TIMESERIES_PATH, timeseries)
    write_curves(trace, summaries, timeseries)

    adaptive = next(row for row in summaries if row["protocol"] == "adaptive_decoder")
    best = min(summaries, key=lambda row: float(row["logical_error"]))

    print(f"read trace {trace_path}")
    print(f"wrote {SUMMARY_PATH}")
    print(f"wrote {TIMESERIES_PATH}")
    print(f"wrote {CURVES_PATH}")
    print(
        "adaptive replay benefit: "
        f"{float(adaptive['adaptive_benefit_log10']):.3f} log10; "
        f"updates={int(float(adaptive['updates']))}; "
        f"logical_error={float(adaptive['logical_error']):.5f}"
    )
    print(
        "best replay protocol: "
        f"{best['protocol']} with logical_error={float(best['logical_error']):.5f}; "
        f"instant_rate_gap={float(adaptive['oracle_gap_log10']):.3f} log10"
    )


if __name__ == "__main__":
    main()
