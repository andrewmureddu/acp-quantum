#!/usr/bin/env python3
"""Circuit-level syndrome-extraction benchmark for adaptive decoder alignment.

This is the H2 scaffold for OP-23. It keeps the same 3-qubit repetition memory
used by the H0/H1 hardware-adaptive decoder benchmarks, but replaces the
single abstract data-error layer with an explicit parity-extraction circuit:
ancilla preparation, two CNOT-style parity checks, gate/idling faults,
measurement noise, leakage-like random records, correlated gate faults, and
feedback error.

The protected logical channel is still fixed. Adaptation changes only the
decoder likelihoods used to interpret the two observed parity bits. The script
also reconstructs the cumulative induced logical bit-flip process, its
symmetrized PTM entries, coherent information, terminal phase-window metrics,
schedule-phase robustness across calibration offsets for generated traces, and
a Pauli-frame logical-channel audit that tracks X and Z data faults into a
diagonal logical Pauli channel.
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
    CHARACTERIZATION_DATA_ERROR,
    MEASUREMENT_ERROR,
    N_QUBITS,
    N_STATES,
    Protocol,
    Q_STATES,
    choose_correction,
    correction_mask,
    q_eta_floor,
    round_transition,
)


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
TRACE_PATH = OUT / "circuit_level_noise_trace.csv"
SUMMARY_PATH = OUT / "circuit_level_decoder_summary.csv"
TIMESERIES_PATH = OUT / "circuit_level_decoder_timeseries.csv"
CURVES_PATH = OUT / "circuit_level_decoder_curves.png"
PHASE_SCAN_SUMMARY_PATH = OUT / "circuit_level_phase_scan_summary.csv"

DEFAULT_ROUNDS = 96
DEFAULT_ANISOTROPY = 4.00
DEFAULT_DRIFT_CYCLES = 1.40
DEFAULT_CALIBRATION_PERIOD = 4
DEFAULT_SEED = 271828
DEFAULT_CROSSTALK_SCALE = 10.0
DEFAULT_LEAKAGE_SCALE = 1.0

BASE_IDLE_ERROR = 0.00055
BASE_GATE_DATA_ERROR = 0.0019
BASE_ANCILLA_GATE_ERROR = 0.0015
BASE_PREP_ERROR = 0.0011
BASE_CORRELATED_GATE = 0.00025
BASE_DATA_CROSSTALK = 0.00020
BASE_LEAKAGE_ERROR = 0.00030
BASE_CORRECTION_ERROR = 0.00080
BASE_IDLE_PHASE_ERROR = 0.00075
BASE_GATE_PHASE_ERROR = 0.00120
BASE_CORRELATED_PHASE = 0.00018
BASE_PHASE_CROSSTALK = 0.00016
BASE_CORRECTION_PHASE_ERROR = 0.00025
CHARACTERIZATION_PHASE_ERROR = 0.00065

UPDATE_L1_THRESHOLD = 0.0018
UPDATE_BENEFIT_LOG10_THRESHOLD = 0.0025
UPDATE_LOOKAHEAD_ROUNDS = DEFAULT_CALIBRATION_PERIOD
PTM_SYMMETRY_TOLERANCE = 5e-10

CIRCUIT_PROTOCOLS = [
    Protocol("uniform_decoder", "uniform"),
    Protocol("static_tailored", "static"),
    Protocol("adaptive_decoder", "adaptive"),
    Protocol("overactive_decoder", "adaptive"),
    Protocol("instant_proxy_decoder", "oracle"),
]


@dataclass(frozen=True)
class CircuitNoise:
    data_idle: np.ndarray
    data_gate: np.ndarray
    data_idle_z: np.ndarray
    data_gate_z: np.ndarray
    ancilla_gate: float
    prep_error: float
    meas_error: float
    leakage_error: float
    correlated_gate: float
    correlated_phase: float
    data_crosstalk: float
    data_crosstalk_z: float
    correction_error: float
    correction_phase_error: float


@dataclass(frozen=True)
class CircuitRound:
    round_index: int
    noise: CircuitNoise
    calib_rates: np.ndarray
    calib_meas: float
    calibration_fresh: bool


def bit(state: int, qubit: int) -> int:
    return (state >> qubit) & 1


def logical_bit(state: int) -> int:
    """Logical bit after ideal majority decoding of the repetition block."""

    return 1 if int(state).bit_count() >= 2 else 0


def binary_entropy(probability: float) -> float:
    p = min(max(float(probability), 0.0), 1.0)
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def clip_probability(value: float, upper: float = 0.24) -> float:
    return float(np.clip(value, 1e-7, upper))


def clip_rates(values: np.ndarray, upper: float = 0.24) -> np.ndarray:
    return np.clip(np.asarray(values, dtype=float), 1e-7, upper)


def add_prob(target: dict[tuple[int, ...], float], key: tuple[int, ...], probability: float) -> None:
    target[key] = target.get(key, 0.0) + float(probability)


def apply_binary_fault(
    distribution: dict[tuple[int, ...], float],
    probability: float,
    transform,
) -> dict[tuple[int, ...], float]:
    p = clip_probability(probability, upper=0.49)
    if p <= 0.0:
        return distribution

    out: dict[tuple[int, ...], float] = {}
    for key, value in distribution.items():
        add_prob(out, key, value * (1.0 - p))
        add_prob(out, transform(key), value * p)
    return out


def flip_data_key(qubit: int):
    mask = 1 << qubit

    def transform(key: tuple[int, ...]) -> tuple[int, ...]:
        return (key[0] ^ mask, *key[1:])

    return transform


def flip_ancilla_key(key: tuple[int, ...]) -> tuple[int, ...]:
    data, record, ancilla = key
    return data, record, ancilla ^ 1


def flip_data_and_ancilla_key(qubit: int):
    mask = 1 << qubit

    def transform(key: tuple[int, ...]) -> tuple[int, ...]:
        data, record, ancilla = key
        return data ^ mask, record, ancilla ^ 1

    return transform


def apply_data_faults(
    distribution: dict[tuple[int, ...], float], rates: np.ndarray
) -> dict[tuple[int, ...], float]:
    out = distribution
    for qubit, rate in enumerate(clip_rates(rates, upper=0.49)):
        out = apply_binary_fault(out, float(rate), flip_data_key(qubit))
    return out


def ideal_cnot(
    distribution: dict[tuple[int, int, int], float], control: int
) -> dict[tuple[int, int, int], float]:
    out: dict[tuple[int, int, int], float] = {}
    for (data, record, ancilla), probability in distribution.items():
        add_prob(out, (data, record, ancilla ^ bit(data, control)), probability)
    return out


def append_measurement(
    distribution: dict[tuple[int, int, int], float], noise: CircuitNoise
) -> dict[tuple[int, int], float]:
    out: dict[tuple[int, int], float] = {}
    p_meas = clip_probability(noise.meas_error, upper=0.49)
    p_leak = clip_probability(noise.leakage_error, upper=0.49)

    for data, record, ancilla in distribution:
        probability = distribution[(data, record, ancilla)]
        for measured_bit, p_bit in ((ancilla, 1.0 - p_meas), (ancilla ^ 1, p_meas)):
            add_prob(out, (data, (record << 1) | measured_bit), probability * (1.0 - p_leak) * p_bit)
        for measured_bit in (0, 1):
            add_prob(out, (data, (record << 1) | measured_bit), probability * p_leak * 0.5)
    return out


def extract_check(
    distribution: dict[tuple[int, int], float],
    check: tuple[int, int],
    noise: CircuitNoise,
) -> dict[tuple[int, int], float]:
    with_ancilla: dict[tuple[int, int, int], float] = {
        (data, record, 0): probability for (data, record), probability in distribution.items()
    }
    with_ancilla = apply_binary_fault(with_ancilla, noise.prep_error, flip_ancilla_key)

    for control in check:
        with_ancilla = ideal_cnot(with_ancilla, control)
        with_ancilla = apply_binary_fault(with_ancilla, noise.data_gate[control], flip_data_key(control))
        with_ancilla = apply_binary_fault(with_ancilla, noise.ancilla_gate, flip_ancilla_key)
        with_ancilla = apply_binary_fault(
            with_ancilla, noise.correlated_gate, flip_data_and_ancilla_key(control)
        )
        for qubit in range(N_QUBITS):
            if qubit not in check:
                with_ancilla = apply_binary_fault(with_ancilla, noise.data_crosstalk, flip_data_key(qubit))

    return append_measurement(with_ancilla, noise)


def pre_correction_distribution(source_physical_state: int, noise: CircuitNoise) -> dict[tuple[int, int], float]:
    distribution: dict[tuple[int, int], float] = {(source_physical_state, 0): 1.0}
    distribution = apply_data_faults(distribution, noise.data_idle)
    distribution = extract_check(distribution, (0, 1), noise)
    distribution = apply_data_faults(distribution, 0.5 * noise.data_idle)
    distribution = extract_check(distribution, (1, 2), noise)
    distribution = apply_data_faults(distribution, 0.5 * noise.data_idle)
    return distribution


def observed_tuple(record: int) -> tuple[int, int]:
    return (record >> 1) & 1, record & 1


def apply_correction_distribution(
    distribution: dict[tuple[int, int], float],
    estimated_rates: np.ndarray,
    estimated_meas: float,
    correction_error: float,
) -> dict[int, float]:
    out: dict[int, float] = {}
    p_fail = clip_probability(correction_error, upper=0.49)

    for (data, record), probability in distribution.items():
        correction = correction_mask(
            choose_correction(observed_tuple(record), estimated_rates, estimated_meas)
        )
        if correction == 0:
            out[data] = out.get(data, 0.0) + probability
        else:
            out[data ^ correction] = out.get(data ^ correction, 0.0) + probability * (1.0 - p_fail)
            out[data] = out.get(data, 0.0) + probability * p_fail
    return out


def apply_state_faults(distribution: dict[int, float], rates: np.ndarray) -> dict[int, float]:
    out = distribution
    for qubit, rate in enumerate(clip_rates(rates, upper=0.49)):
        mask = 1 << qubit
        p = float(rate)
        next_out: dict[int, float] = {}
        for state, probability in out.items():
            next_out[state] = next_out.get(state, 0.0) + probability * (1.0 - p)
            next_out[state ^ mask] = next_out.get(state ^ mask, 0.0) + probability * p
        out = next_out
    return out


def flip_pauli_x_key(qubit: int):
    mask = 1 << qubit

    def transform(key: tuple[int, ...]) -> tuple[int, ...]:
        return (key[0] ^ mask, key[1], *key[2:])

    return transform


def flip_pauli_z_key(qubit: int):
    mask = 1 << qubit

    def transform(key: tuple[int, ...]) -> tuple[int, ...]:
        return (key[0], key[1] ^ mask, *key[2:])

    return transform


def flip_pauli_ancilla_key(key: tuple[int, ...]) -> tuple[int, ...]:
    x_mask, z_mask, record, ancilla = key
    return x_mask, z_mask, record, ancilla ^ 1


def flip_pauli_x_and_ancilla_key(qubit: int):
    mask = 1 << qubit

    def transform(key: tuple[int, ...]) -> tuple[int, ...]:
        x_mask, z_mask, record, ancilla = key
        return x_mask ^ mask, z_mask, record, ancilla ^ 1

    return transform


def apply_pauli_data_faults(
    distribution: dict[tuple[int, int, int], float],
    x_rates: np.ndarray,
    z_rates: np.ndarray,
) -> dict[tuple[int, int, int], float]:
    out = distribution
    for qubit, rate in enumerate(clip_rates(x_rates, upper=0.49)):
        out = apply_binary_fault(out, float(rate), flip_pauli_x_key(qubit))
    for qubit, rate in enumerate(clip_rates(z_rates, upper=0.49)):
        out = apply_binary_fault(out, float(rate), flip_pauli_z_key(qubit))
    return out


def ideal_pauli_cnot(
    distribution: dict[tuple[int, int, int, int], float], control: int
) -> dict[tuple[int, int, int, int], float]:
    out: dict[tuple[int, int, int, int], float] = {}
    for (x_mask, z_mask, record, ancilla), probability in distribution.items():
        add_prob(out, (x_mask, z_mask, record, ancilla ^ bit(x_mask, control)), probability)
    return out


def append_pauli_measurement(
    distribution: dict[tuple[int, int, int, int], float], noise: CircuitNoise
) -> dict[tuple[int, int, int], float]:
    out: dict[tuple[int, int, int], float] = {}
    p_meas = clip_probability(noise.meas_error, upper=0.49)
    p_leak = clip_probability(noise.leakage_error, upper=0.49)

    for x_mask, z_mask, record, ancilla in distribution:
        probability = distribution[(x_mask, z_mask, record, ancilla)]
        for measured_bit, p_bit in ((ancilla, 1.0 - p_meas), (ancilla ^ 1, p_meas)):
            add_prob(
                out,
                (x_mask, z_mask, (record << 1) | measured_bit),
                probability * (1.0 - p_leak) * p_bit,
            )
        for measured_bit in (0, 1):
            add_prob(
                out,
                (x_mask, z_mask, (record << 1) | measured_bit),
                probability * p_leak * 0.5,
            )
    return out


def pauli_extract_check(
    distribution: dict[tuple[int, int, int], float],
    check: tuple[int, int],
    noise: CircuitNoise,
) -> dict[tuple[int, int, int], float]:
    with_ancilla: dict[tuple[int, int, int, int], float] = {
        (x_mask, z_mask, record, 0): probability
        for (x_mask, z_mask, record), probability in distribution.items()
    }
    with_ancilla = apply_binary_fault(with_ancilla, noise.prep_error, flip_pauli_ancilla_key)

    for control in check:
        with_ancilla = ideal_pauli_cnot(with_ancilla, control)
        with_ancilla = apply_binary_fault(
            with_ancilla, noise.data_gate[control], flip_pauli_x_key(control)
        )
        with_ancilla = apply_binary_fault(
            with_ancilla, noise.data_gate_z[control], flip_pauli_z_key(control)
        )
        with_ancilla = apply_binary_fault(with_ancilla, noise.ancilla_gate, flip_pauli_ancilla_key)
        with_ancilla = apply_binary_fault(
            with_ancilla, noise.correlated_gate, flip_pauli_x_and_ancilla_key(control)
        )
        with_ancilla = apply_binary_fault(
            with_ancilla, noise.correlated_phase, flip_pauli_z_key(control)
        )
        for qubit in range(N_QUBITS):
            if qubit not in check:
                with_ancilla = apply_binary_fault(
                    with_ancilla, noise.data_crosstalk, flip_pauli_x_key(qubit)
                )
                with_ancilla = apply_binary_fault(
                    with_ancilla, noise.data_crosstalk_z, flip_pauli_z_key(qubit)
                )

    return append_pauli_measurement(with_ancilla, noise)


def apply_pauli_correction_distribution(
    distribution: dict[tuple[int, int, int], float],
    estimated_rates: np.ndarray,
    estimated_meas: float,
    correction_error: float,
    correction_phase_error: float,
) -> dict[tuple[int, int], float]:
    out: dict[tuple[int, int], float] = {}
    p_fail = clip_probability(correction_error, upper=0.49)
    p_phase = clip_probability(correction_phase_error, upper=0.49)

    for (x_mask, z_mask, record), probability in distribution.items():
        correction = correction_mask(
            choose_correction(observed_tuple(record), estimated_rates, estimated_meas)
        )
        branches: dict[tuple[int, int], float] = {}
        if correction == 0:
            branches[(x_mask, z_mask)] = probability
        else:
            branches[(x_mask ^ correction, z_mask)] = probability * (1.0 - p_fail)
            branches[(x_mask, z_mask)] = probability * p_fail

        for (branch_x, branch_z), branch_probability in branches.items():
            if correction == 0:
                add_prob(out, (branch_x, branch_z), branch_probability)
                continue
            add_prob(out, (branch_x, branch_z), branch_probability * (1.0 - p_phase))
            add_prob(out, (branch_x, branch_z ^ correction), branch_probability * p_phase)
    return out


def apply_pauli_frame_faults(
    distribution: dict[tuple[int, int], float],
    x_rates: np.ndarray,
    z_rates: np.ndarray,
) -> dict[tuple[int, int], float]:
    with_record = {(x_mask, z_mask, 0): probability for (x_mask, z_mask), probability in distribution.items()}
    faulted = apply_pauli_data_faults(with_record, x_rates, z_rates)
    out: dict[tuple[int, int], float] = {}
    for (x_mask, z_mask, _record), probability in faulted.items():
        add_prob(out, (x_mask, z_mask), probability)
    return out


def pauli_round_distribution(
    distribution: dict[tuple[int, int], float],
    noise: CircuitNoise,
    estimated_rates: np.ndarray,
    estimated_meas: float,
    update_overhead: bool,
) -> dict[tuple[int, int], float]:
    with_record = {
        (source_x, source_z, 0): probability
        for (source_x, source_z), probability in distribution.items()
    }
    with_record = apply_pauli_data_faults(with_record, noise.data_idle, noise.data_idle_z)
    with_record = pauli_extract_check(with_record, (0, 1), noise)
    with_record = apply_pauli_data_faults(
        with_record, 0.5 * noise.data_idle, 0.5 * noise.data_idle_z
    )
    with_record = pauli_extract_check(with_record, (1, 2), noise)
    with_record = apply_pauli_data_faults(
        with_record, 0.5 * noise.data_idle, 0.5 * noise.data_idle_z
    )
    out = apply_pauli_correction_distribution(
        with_record,
        estimated_rates,
        estimated_meas,
        noise.correction_error,
        noise.correction_phase_error,
    )

    if update_overhead:
        out = apply_pauli_frame_faults(
            out,
            np.full(N_QUBITS, CHARACTERIZATION_DATA_ERROR, dtype=float),
            np.full(N_QUBITS, CHARACTERIZATION_PHASE_ERROR, dtype=float),
        )

    total = sum(out.values())
    if not math.isclose(total, 1.0, rel_tol=0.0, abs_tol=1e-9):
        raise RuntimeError(f"non-stochastic Pauli-frame distribution: {total}")
    return out


def circuit_round_transition(
    noise: CircuitNoise,
    estimated_rates: np.ndarray,
    estimated_meas: float,
    update_overhead: bool,
) -> np.ndarray:
    transition = np.zeros((N_STATES, N_STATES), dtype=float)
    for source in range(N_STATES):
        pre = pre_correction_distribution(source, noise)
        post = apply_correction_distribution(
            pre, estimated_rates, estimated_meas, noise.correction_error
        )
        if update_overhead:
            post = apply_state_faults(
                post, np.full(N_QUBITS, CHARACTERIZATION_DATA_ERROR, dtype=float)
            )
        for target, probability in post.items():
            transition[target, source] += probability

    column_sums = np.sum(transition, axis=0)
    if not np.allclose(column_sums, 1.0, atol=1e-10):
        raise RuntimeError(f"non-stochastic circuit transition: {column_sums}")
    return transition


def no_flip_product(rates: list[float]) -> float:
    product = 1.0
    for rate in rates:
        product *= 1.0 - clip_probability(rate, upper=0.49)
    return product


def decoder_proxy_rates(noise: CircuitNoise) -> np.ndarray:
    """Map the circuit fault model to the decoder's three single-error priors."""

    appearances = [1, 2, 1]
    crosstalk_opportunities = [2, 0, 2]
    rates = []
    for qubit in range(N_QUBITS):
        no_flip = no_flip_product(
            [float(noise.data_idle[qubit])] * 2
            + [float(noise.data_gate[qubit])] * appearances[qubit]
            + [noise.correlated_gate] * appearances[qubit]
            + [noise.data_crosstalk] * crosstalk_opportunities[qubit]
        )
        rates.append(1.0 - no_flip)
    return clip_rates(np.array(rates, dtype=float), upper=0.30)


def decoder_proxy_meas(noise: CircuitNoise) -> float:
    no_flip = no_flip_product(
        [
            noise.meas_error,
            noise.prep_error,
            noise.ancilla_gate,
            noise.ancilla_gate,
            noise.correlated_gate,
            noise.correlated_gate,
        ]
    )
    effective = 1.0 - no_flip
    effective = effective * (1.0 - noise.leakage_error) + 0.5 * noise.leakage_error
    return clip_probability(effective, upper=0.30)


def structured_circuit_noise(
    round_index: int,
    total_rounds: int,
    anisotropy: float,
    drift_cycles: float,
    crosstalk_scale: float,
    leakage_scale: float,
) -> CircuitNoise:
    total = max(1, total_rounds - 1)
    t = round_index / total
    phase = 2.0 * np.pi * drift_cycles * t
    offsets = np.array([0.0, 2.0 * np.pi / 3.0, 4.0 * np.pi / 3.0])
    weights = np.exp(anisotropy * np.cos(phase - offsets))
    weights /= float(np.mean(weights))

    burst = math.exp(-0.5 * ((t - 0.58) / 0.11) ** 2)
    slow_meas = 1.0 + 0.22 * math.sin(2.0 * np.pi * (t + 0.13))

    data_idle = BASE_IDLE_ERROR * weights
    data_gate = BASE_GATE_DATA_ERROR * weights
    data_gate[1] += crosstalk_scale * 0.0018 * burst
    data_gate[2] += crosstalk_scale * 0.0011 * burst
    data_gate[0] *= 1.0 + 0.12 * math.sin(2.0 * np.pi * t)

    phase_weights = np.exp(0.55 * anisotropy * np.sin(phase - offsets + 0.37))
    phase_weights /= float(np.mean(phase_weights))
    data_idle_z = BASE_IDLE_PHASE_ERROR * phase_weights
    data_gate_z = BASE_GATE_PHASE_ERROR * phase_weights
    data_gate_z[0] += crosstalk_scale * 0.0007 * burst
    data_gate_z[2] += crosstalk_scale * 0.0005 * burst

    return CircuitNoise(
        data_idle=clip_rates(data_idle, upper=0.10),
        data_gate=clip_rates(data_gate, upper=0.10),
        data_idle_z=clip_rates(data_idle_z, upper=0.10),
        data_gate_z=clip_rates(data_gate_z, upper=0.10),
        ancilla_gate=clip_probability(BASE_ANCILLA_GATE_ERROR * (1.0 + 0.45 * burst), upper=0.10),
        prep_error=clip_probability(BASE_PREP_ERROR * (1.0 + 0.20 * burst), upper=0.10),
        meas_error=clip_probability(MEASUREMENT_ERROR * slow_meas + 0.0038 * burst, upper=0.20),
        leakage_error=clip_probability(leakage_scale * (BASE_LEAKAGE_ERROR + 0.0019 * burst), upper=0.20),
        correlated_gate=clip_probability(
            BASE_CORRELATED_GATE + crosstalk_scale * 0.0016 * burst, upper=0.10
        ),
        correlated_phase=clip_probability(
            BASE_CORRELATED_PHASE + crosstalk_scale * 0.0008 * burst, upper=0.10
        ),
        data_crosstalk=clip_probability(
            BASE_DATA_CROSSTALK + crosstalk_scale * 0.0013 * burst, upper=0.10
        ),
        data_crosstalk_z=clip_probability(
            BASE_PHASE_CROSSTALK + crosstalk_scale * 0.0006 * burst, upper=0.10
        ),
        correction_error=clip_probability(BASE_CORRECTION_ERROR * (1.0 + 0.30 * burst), upper=0.10),
        correction_phase_error=clip_probability(
            BASE_CORRECTION_PHASE_ERROR * (1.0 + 0.25 * burst), upper=0.10
        ),
    )


def generate_circuit_trace(
    path: Path | None,
    total_rounds: int = DEFAULT_ROUNDS,
    anisotropy: float = DEFAULT_ANISOTROPY,
    drift_cycles: float = DEFAULT_DRIFT_CYCLES,
    calibration_period: int = DEFAULT_CALIBRATION_PERIOD,
    calibration_phase: int = 0,
    seed: int = DEFAULT_SEED,
    crosstalk_scale: float = 1.0,
    leakage_scale: float = 1.0,
) -> list[CircuitRound]:
    rng = np.random.default_rng(seed)
    rounds: list[CircuitRound] = []
    rows: list[dict[str, float | int | str]] = []

    period = max(1, int(calibration_period))
    phase_offset = int(calibration_phase) % period
    noises = [
        structured_circuit_noise(
            round_index,
            total_rounds,
            anisotropy,
            drift_cycles,
            crosstalk_scale,
            leakage_scale,
        )
        for round_index in range(total_rounds)
    ]
    calibration_candidates: list[tuple[np.ndarray, float]] = []
    for noise in noises:
        true_proxy_rates = decoder_proxy_rates(noise)
        true_proxy_meas = decoder_proxy_meas(noise)
        rate_sigma = 0.00035 + 0.10 * true_proxy_rates
        sampled_rates = clip_rates(
            true_proxy_rates + rng.normal(0.0, rate_sigma), upper=0.30
        )
        sampled_meas = clip_probability(
            true_proxy_meas + float(rng.normal(0.0, 0.00035 + 0.08 * true_proxy_meas)),
            upper=0.30,
        )
        calibration_candidates.append((sampled_rates, sampled_meas))

    current_calib_rates = calibration_candidates[0][0].copy()
    current_calib_meas = calibration_candidates[0][1]

    for round_index in range(total_rounds):
        noise = noises[round_index]
        fresh = (round_index - phase_offset) % period == 0
        true_proxy_rates = decoder_proxy_rates(noise)
        true_proxy_meas = decoder_proxy_meas(noise)

        if fresh:
            current_calib_rates = calibration_candidates[round_index][0].copy()
            current_calib_meas = calibration_candidates[round_index][1]

        rounds.append(
            CircuitRound(
                round_index=round_index,
                noise=noise,
                calib_rates=current_calib_rates.copy(),
                calib_meas=current_calib_meas,
                calibration_fresh=fresh,
            )
        )
        rows.append(
            {
                "round": round_index,
                "data_idle_p0": float(noise.data_idle[0]),
                "data_idle_p1": float(noise.data_idle[1]),
                "data_idle_p2": float(noise.data_idle[2]),
                "data_gate_p0": float(noise.data_gate[0]),
                "data_gate_p1": float(noise.data_gate[1]),
                "data_gate_p2": float(noise.data_gate[2]),
                "data_idle_z_p0": float(noise.data_idle_z[0]),
                "data_idle_z_p1": float(noise.data_idle_z[1]),
                "data_idle_z_p2": float(noise.data_idle_z[2]),
                "data_gate_z_p0": float(noise.data_gate_z[0]),
                "data_gate_z_p1": float(noise.data_gate_z[1]),
                "data_gate_z_p2": float(noise.data_gate_z[2]),
                "ancilla_gate": noise.ancilla_gate,
                "prep_error": noise.prep_error,
                "meas_error": noise.meas_error,
                "leakage_error": noise.leakage_error,
                "correlated_gate": noise.correlated_gate,
                "correlated_phase": noise.correlated_phase,
                "data_crosstalk": noise.data_crosstalk,
                "data_crosstalk_z": noise.data_crosstalk_z,
                "correction_error": noise.correction_error,
                "correction_phase_error": noise.correction_phase_error,
                "decoder_proxy_p0": float(true_proxy_rates[0]),
                "decoder_proxy_p1": float(true_proxy_rates[1]),
                "decoder_proxy_p2": float(true_proxy_rates[2]),
                "decoder_proxy_meas": true_proxy_meas,
                "calib_p0": float(current_calib_rates[0]),
                "calib_p1": float(current_calib_rates[1]),
                "calib_p2": float(current_calib_rates[2]),
                "calib_meas": current_calib_meas,
                "calibration_fresh": int(fresh),
                "calibration_period": period,
                "calibration_phase": phase_offset,
                "source": "synthetic_h2_circuit_trace",
            }
        )

    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    return rounds


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


def read_circuit_trace(path: Path) -> list[CircuitRound]:
    rounds: list[CircuitRound] = []
    with path.open(newline="") as f:
        for row in csv.DictReader(f):
            noise = CircuitNoise(
                data_idle=clip_rates(
                    np.array(
                        [
                            float_field(row, "data_idle_p0"),
                            float_field(row, "data_idle_p1"),
                            float_field(row, "data_idle_p2"),
                        ],
                        dtype=float,
                    ),
                    upper=0.10,
                ),
                data_gate=clip_rates(
                    np.array(
                        [
                            float_field(row, "data_gate_p0"),
                            float_field(row, "data_gate_p1"),
                            float_field(row, "data_gate_p2"),
                        ],
                        dtype=float,
                    ),
                    upper=0.10,
                ),
                data_idle_z=clip_rates(
                    np.array(
                        [
                            float_field(row, "data_idle_z_p0", 0.75 * float_field(row, "data_idle_p0")),
                            float_field(row, "data_idle_z_p1", 0.75 * float_field(row, "data_idle_p1")),
                            float_field(row, "data_idle_z_p2", 0.75 * float_field(row, "data_idle_p2")),
                        ],
                        dtype=float,
                    ),
                    upper=0.10,
                ),
                data_gate_z=clip_rates(
                    np.array(
                        [
                            float_field(row, "data_gate_z_p0", 0.55 * float_field(row, "data_gate_p0")),
                            float_field(row, "data_gate_z_p1", 0.55 * float_field(row, "data_gate_p1")),
                            float_field(row, "data_gate_z_p2", 0.55 * float_field(row, "data_gate_p2")),
                        ],
                        dtype=float,
                    ),
                    upper=0.10,
                ),
                ancilla_gate=clip_probability(float_field(row, "ancilla_gate"), upper=0.10),
                prep_error=clip_probability(float_field(row, "prep_error"), upper=0.10),
                meas_error=clip_probability(float_field(row, "meas_error"), upper=0.20),
                leakage_error=clip_probability(float_field(row, "leakage_error"), upper=0.20),
                correlated_gate=clip_probability(float_field(row, "correlated_gate"), upper=0.10),
                correlated_phase=clip_probability(
                    float_field(row, "correlated_phase", 0.5 * float_field(row, "correlated_gate")),
                    upper=0.10,
                ),
                data_crosstalk=clip_probability(float_field(row, "data_crosstalk"), upper=0.10),
                data_crosstalk_z=clip_probability(
                    float_field(row, "data_crosstalk_z", 0.5 * float_field(row, "data_crosstalk")),
                    upper=0.10,
                ),
                correction_error=clip_probability(float_field(row, "correction_error"), upper=0.10),
                correction_phase_error=clip_probability(
                    float_field(row, "correction_phase_error", BASE_CORRECTION_PHASE_ERROR),
                    upper=0.10,
                ),
            )
            fallback_rates = decoder_proxy_rates(noise)
            rounds.append(
                CircuitRound(
                    round_index=int(float_field(row, "round", float(len(rounds)))),
                    noise=noise,
                    calib_rates=clip_rates(
                        np.array(
                            [
                                float_field(row, "calib_p0", float(fallback_rates[0])),
                                float_field(row, "calib_p1", float(fallback_rates[1])),
                                float_field(row, "calib_p2", float(fallback_rates[2])),
                            ],
                            dtype=float,
                        ),
                        upper=0.30,
                    ),
                    calib_meas=clip_probability(
                        float_field(row, "calib_meas", decoder_proxy_meas(noise)), upper=0.30
                    ),
                    calibration_fresh=bool_field(row, "calibration_fresh", True),
                )
            )
    if not rounds:
        raise ValueError(f"trace {path} contained no rows")
    return rounds


def mutual_information(joint: np.ndarray) -> float:
    total = float(np.sum(joint))
    if total <= 0.0:
        return 0.0
    p = joint / total
    row = np.sum(p, axis=1)
    col = np.sum(p, axis=0)
    mi = 0.0
    for i in range(p.shape[0]):
        for j in range(p.shape[1]):
            value = float(p[i, j])
            if value > 0.0:
                mi += value * math.log2(value / (float(row[i]) * float(col[j])))
    return max(0.0, float(mi))


def circuit_error_syndrome_mi(noise: CircuitNoise) -> float:
    joint = np.zeros((N_STATES, 4), dtype=float)
    for (data, record), probability in pre_correction_distribution(0, noise).items():
        joint[data, record] += probability
    return mutual_information(joint)


def conditional_logical_record_leakage(noise: CircuitNoise) -> float:
    joint = np.zeros((2, N_STATES, 4), dtype=float)
    for logical_bit, codeword in enumerate((0, 0b111)):
        for (data, record), probability in pre_correction_distribution(codeword, noise).items():
            error_sector = data ^ codeword
            joint[logical_bit, error_sector, record] += 0.5 * probability

    leakage = 0.0
    p_error = np.sum(joint, axis=(0, 2))
    for error_sector in range(N_STATES):
        weight = float(p_error[error_sector])
        if weight <= 0.0:
            continue
        conditional = joint[:, error_sector, :] / weight
        leakage += weight * mutual_information(conditional)
    return max(0.0, float(leakage))


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
    l1_change = float(np.sum(np.abs(candidate_rates - current_rates)))
    l1_change += abs(candidate_meas - current_meas)
    if l1_change < UPDATE_L1_THRESHOLD:
        return False

    old_error = expected_logical_error(candidate_rates, candidate_meas, current_rates, current_meas)
    new_error = expected_logical_error(candidate_rates, candidate_meas, candidate_rates, candidate_meas)
    benefit = math.log10((old_error + 1e-15) / (new_error + 1e-15))
    return benefit >= UPDATE_BENEFIT_LOG10_THRESHOLD


def logical_process_metrics(channel: np.ndarray) -> dict[str, float]:
    """Induced logical bit-flip process after ideal final majority decoding.

    This function is the legacy bit-flip-component audit. The Pauli-frame
    audit below is stricter and should be used for full logical-channel
    interpretation. The reported PTM here is the symmetrized Pauli-X channel
    implied by the two codeword transition rates; the asymmetry column records
    the error of that symmetry assumption.
    """

    p_0_to_1 = sum(
        float(channel[target, 0])
        for target in range(N_STATES)
        if logical_bit(target) == 1
    )
    p_1_to_0 = sum(
        float(channel[target, 0b111]) for target in range(N_STATES) if logical_bit(target) == 0
    )
    logical_bitflip = 0.5 * (p_0_to_1 + p_1_to_0)
    logical_bitflip = min(max(logical_bitflip, 0.0), 1.0)
    ptm_damping = 1.0 - 2.0 * logical_bitflip
    asymmetry = abs(p_0_to_1 - p_1_to_0)

    return {
        "logical_p01": p_0_to_1,
        "logical_p10": p_1_to_0,
        "logical_bitflip_probability": logical_bitflip,
        "logical_bitflip_asymmetry": asymmetry,
        "logical_ptm_symmetry_pass": float(asymmetry <= PTM_SYMMETRY_TOLERANCE),
        "logical_ptm_xx": 1.0,
        "logical_ptm_yy": ptm_damping,
        "logical_ptm_zz": ptm_damping,
        "logical_ptm_z_shift": p_1_to_0 - p_0_to_1,
        "logical_entanglement_fidelity": 1.0 - logical_bitflip,
        "logical_coherent_information_bits": 1.0 - binary_entropy(logical_bitflip),
    }


def shannon_entropy(probabilities: np.ndarray) -> float:
    entropy = 0.0
    for probability in probabilities:
        p = float(probability)
        if p > 0.0:
            entropy -= p * math.log2(p)
    return entropy


def logical_pauli_index(logical_x: int, logical_z: int) -> int:
    if logical_x and logical_z:
        return 2
    if logical_x:
        return 1
    if logical_z:
        return 3
    return 0


def logical_pauli_distribution(distribution: dict[tuple[int, int], float]) -> np.ndarray:
    pauli = np.zeros(4, dtype=float)
    for (x_mask, z_mask), probability in distribution.items():
        logical_x = logical_bit(x_mask)
        logical_z = int(int(z_mask).bit_count() % 2)
        pauli[logical_pauli_index(logical_x, logical_z)] += probability
    total = float(np.sum(pauli))
    if total <= 0.0:
        raise RuntimeError("empty Pauli-frame distribution")
    return pauli / total


def pauli_logical_process_metrics(
    distribution: dict[tuple[int, int], float], bitflip_reference: float
) -> dict[str, float]:
    """Return the actual diagonal logical Pauli channel from a Pauli-frame run.

    Index order is I, X, Y, Z. The 3-qubit bit-flip code leaves phase faults
    largely uncorrected, so this audit is intentionally more severe than the
    classical bit-flip PTM inferred above.
    """

    p_i, p_x, p_y, p_z = [float(x) for x in logical_pauli_distribution(distribution)]
    pauli_error = p_x + p_y + p_z
    bitflip = p_x + p_y
    phaseflip = p_z + p_y
    ptm_xx = p_i + p_x - p_y - p_z
    ptm_yy = p_i - p_x + p_y - p_z
    ptm_zz = p_i - p_x - p_y + p_z
    coherent_information = 1.0 - shannon_entropy(np.array([p_i, p_x, p_y, p_z]))

    return {
        "pauli_logical_p_i": p_i,
        "pauli_logical_p_x": p_x,
        "pauli_logical_p_y": p_y,
        "pauli_logical_p_z": p_z,
        "pauli_logical_error_probability": pauli_error,
        "pauli_logical_bitflip_probability": bitflip,
        "pauli_logical_phaseflip_probability": phaseflip,
        "pauli_logical_ptm_xx": ptm_xx,
        "pauli_logical_ptm_yy": ptm_yy,
        "pauli_logical_ptm_zz": ptm_zz,
        "pauli_logical_entanglement_fidelity": p_i,
        "pauli_logical_coherent_information_bits": coherent_information,
        "pauli_bitflip_consistency_error": abs(bitflip - bitflip_reference),
    }


def infer_phase_window(trace: list[CircuitRound]) -> int:
    fresh_indices = [index for index, item in enumerate(trace) if item.calibration_fresh]
    if len(fresh_indices) >= 2:
        gaps = np.diff(np.asarray(fresh_indices, dtype=int))
        positive_gaps = [int(gap) for gap in gaps if int(gap) > 0]
        if positive_gaps:
            return max(1, min(len(trace), int(round(float(np.median(positive_gaps))))))
    return max(1, min(len(trace), DEFAULT_CALIBRATION_PERIOD))


def run_circuit_protocol(
    protocol: Protocol,
    trace: list[CircuitRound],
    diagnostics: list[dict[str, float]],
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
        estimated_rates = decoder_proxy_rates(initial.noise)
        estimated_meas = decoder_proxy_meas(initial.noise)
    else:
        raise ValueError(f"unknown protocol mode {protocol.mode!r}")

    state_distribution = np.zeros(N_STATES, dtype=float)
    state_distribution[0] = 1.0
    pauli_distribution: dict[tuple[int, int], float] = {(0, 0): 1.0}
    cumulative_transition = np.eye(N_STATES, dtype=float)
    updates = 0
    average_l1_estimation_error = 0.0
    average_meas_estimation_error = 0.0
    average_syndrome_mi = 0.0
    average_logical_leakage = 0.0
    worst_q = 0.0
    worst_eta = 0.0
    worst_floor = 0.0
    timeseries: list[dict[str, float | str]] = []

    for item, diag in zip(trace, diagnostics):
        update_this_round = False
        true_proxy_rates = decoder_proxy_rates(item.noise)
        true_proxy_meas = decoder_proxy_meas(item.noise)

        if protocol.mode == "oracle":
            estimated_rates = true_proxy_rates.copy()
            estimated_meas = true_proxy_meas
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

        transition = circuit_round_transition(
            item.noise,
            estimated_rates,
            estimated_meas,
            update_overhead=update_this_round,
        )
        q_star, eta_star, floor = q_eta_floor(transition)
        worst_q = max(worst_q, q_star)
        worst_eta = max(worst_eta, eta_star)
        worst_floor = max(worst_floor, floor)

        state_distribution = transition @ state_distribution
        cumulative_transition = transition @ cumulative_transition
        process = logical_process_metrics(cumulative_transition)
        pauli_distribution = pauli_round_distribution(
            pauli_distribution,
            item.noise,
            estimated_rates,
            estimated_meas,
            update_overhead=update_this_round,
        )
        pauli_process = pauli_logical_process_metrics(
            pauli_distribution, process["logical_bitflip_probability"]
        )
        logical_error = float(np.sum(state_distribution[Q_STATES]))
        estimation_l1 = float(np.sum(np.abs(true_proxy_rates - estimated_rates)))
        meas_estimation_error = abs(true_proxy_meas - estimated_meas)

        average_l1_estimation_error += estimation_l1
        average_meas_estimation_error += meas_estimation_error
        average_syndrome_mi += diag["syndrome_mi_bits"]
        average_logical_leakage += diag["logical_record_leakage_bits"]

        timeseries.append(
            {
                "protocol": protocol.name,
                "round": float(item.round_index),
                "logical_error": logical_error,
                "entanglement_fidelity": process["logical_entanglement_fidelity"],
                "logical_p01": process["logical_p01"],
                "logical_p10": process["logical_p10"],
                "logical_bitflip_probability": process["logical_bitflip_probability"],
                "logical_bitflip_asymmetry": process["logical_bitflip_asymmetry"],
                "logical_ptm_symmetry_pass": process["logical_ptm_symmetry_pass"],
                "logical_ptm_xx": process["logical_ptm_xx"],
                "logical_ptm_yy": process["logical_ptm_yy"],
                "logical_ptm_zz": process["logical_ptm_zz"],
                "logical_ptm_z_shift": process["logical_ptm_z_shift"],
                "logical_coherent_information_bits": process[
                    "logical_coherent_information_bits"
                ],
                "pauli_logical_p_i": pauli_process["pauli_logical_p_i"],
                "pauli_logical_p_x": pauli_process["pauli_logical_p_x"],
                "pauli_logical_p_y": pauli_process["pauli_logical_p_y"],
                "pauli_logical_p_z": pauli_process["pauli_logical_p_z"],
                "pauli_logical_error_probability": pauli_process[
                    "pauli_logical_error_probability"
                ],
                "pauli_logical_bitflip_probability": pauli_process[
                    "pauli_logical_bitflip_probability"
                ],
                "pauli_logical_phaseflip_probability": pauli_process[
                    "pauli_logical_phaseflip_probability"
                ],
                "pauli_logical_ptm_xx": pauli_process["pauli_logical_ptm_xx"],
                "pauli_logical_ptm_yy": pauli_process["pauli_logical_ptm_yy"],
                "pauli_logical_ptm_zz": pauli_process["pauli_logical_ptm_zz"],
                "pauli_logical_entanglement_fidelity": pauli_process[
                    "pauli_logical_entanglement_fidelity"
                ],
                "pauli_logical_coherent_information_bits": pauli_process[
                    "pauli_logical_coherent_information_bits"
                ],
                "pauli_bitflip_consistency_error": pauli_process[
                    "pauli_bitflip_consistency_error"
                ],
                "updated": float(update_this_round),
                "estimate_l1_error": estimation_l1,
                "meas_estimation_error": meas_estimation_error,
                "syndrome_mi_bits": diag["syndrome_mi_bits"],
                "logical_record_leakage_bits": diag["logical_record_leakage_bits"],
                "q_star": q_star,
                "eta_star": eta_star,
                "alignment_floor": floor,
                "proxy_p0": float(true_proxy_rates[0]),
                "proxy_p1": float(true_proxy_rates[1]),
                "proxy_p2": float(true_proxy_rates[2]),
                "proxy_meas": true_proxy_meas,
                "calib_p0": float(item.calib_rates[0]),
                "calib_p1": float(item.calib_rates[1]),
                "calib_p2": float(item.calib_rates[2]),
                "calib_meas": item.calib_meas,
                "calibration_fresh": float(item.calibration_fresh),
                "correlated_gate": item.noise.correlated_gate,
                "correlated_phase": item.noise.correlated_phase,
                "data_crosstalk": item.noise.data_crosstalk,
                "data_crosstalk_z": item.noise.data_crosstalk_z,
                "leakage_error": item.noise.leakage_error,
            }
        )

    n_rounds = float(len(trace))
    final_process = logical_process_metrics(cumulative_transition)
    phase_window = infer_phase_window(trace)
    phase_rows = timeseries[-phase_window:]
    phase_avg_logical_error = float(np.mean([float(row["logical_error"]) for row in phase_rows]))
    phase_avg_bitflip = float(
        np.mean([float(row["logical_bitflip_probability"]) for row in phase_rows])
    )
    phase_avg_coherent_information = float(
        np.mean([float(row["logical_coherent_information_bits"]) for row in phase_rows])
    )
    phase_avg_pauli_error = float(
        np.mean([float(row["pauli_logical_error_probability"]) for row in phase_rows])
    )
    phase_avg_pauli_coherent_information = float(
        np.mean([float(row["pauli_logical_coherent_information_bits"]) for row in phase_rows])
    )
    logical_error = float(np.sum(state_distribution[Q_STATES]))
    final_pauli_process = pauli_logical_process_metrics(
        pauli_distribution, final_process["logical_bitflip_probability"]
    )
    summary = {
        "protocol": protocol.name,
        "rounds": n_rounds,
        "logical_error": logical_error,
        "entanglement_fidelity": final_process["logical_entanglement_fidelity"],
        "logical_p01": final_process["logical_p01"],
        "logical_p10": final_process["logical_p10"],
        "logical_bitflip_probability": final_process["logical_bitflip_probability"],
        "logical_bitflip_asymmetry": final_process["logical_bitflip_asymmetry"],
        "logical_ptm_symmetry_pass": final_process["logical_ptm_symmetry_pass"],
        "logical_ptm_xx": final_process["logical_ptm_xx"],
        "logical_ptm_yy": final_process["logical_ptm_yy"],
        "logical_ptm_zz": final_process["logical_ptm_zz"],
        "logical_ptm_z_shift": final_process["logical_ptm_z_shift"],
        "logical_coherent_information_bits": final_process[
            "logical_coherent_information_bits"
        ],
        "pauli_logical_p_i": final_pauli_process["pauli_logical_p_i"],
        "pauli_logical_p_x": final_pauli_process["pauli_logical_p_x"],
        "pauli_logical_p_y": final_pauli_process["pauli_logical_p_y"],
        "pauli_logical_p_z": final_pauli_process["pauli_logical_p_z"],
        "pauli_logical_error_probability": final_pauli_process[
            "pauli_logical_error_probability"
        ],
        "pauli_logical_bitflip_probability": final_pauli_process[
            "pauli_logical_bitflip_probability"
        ],
        "pauli_logical_phaseflip_probability": final_pauli_process[
            "pauli_logical_phaseflip_probability"
        ],
        "pauli_logical_ptm_xx": final_pauli_process["pauli_logical_ptm_xx"],
        "pauli_logical_ptm_yy": final_pauli_process["pauli_logical_ptm_yy"],
        "pauli_logical_ptm_zz": final_pauli_process["pauli_logical_ptm_zz"],
        "pauli_logical_entanglement_fidelity": final_pauli_process[
            "pauli_logical_entanglement_fidelity"
        ],
        "pauli_logical_coherent_information_bits": final_pauli_process[
            "pauli_logical_coherent_information_bits"
        ],
        "pauli_bitflip_consistency_error": final_pauli_process[
            "pauli_bitflip_consistency_error"
        ],
        "phase_window_rounds": float(phase_window),
        "phase_avg_logical_error": phase_avg_logical_error,
        "phase_avg_entanglement_fidelity": 1.0 - phase_avg_bitflip,
        "phase_avg_coherent_information_bits": phase_avg_coherent_information,
        "phase_avg_pauli_logical_error_probability": phase_avg_pauli_error,
        "phase_avg_pauli_coherent_information_bits": phase_avg_pauli_coherent_information,
        "updates": float(updates),
        "avg_l1_estimation_error": average_l1_estimation_error / n_rounds,
        "avg_meas_estimation_error": average_meas_estimation_error / n_rounds,
        "avg_syndrome_mi_bits": average_syndrome_mi / n_rounds,
        "avg_logical_record_leakage_bits": average_logical_leakage / n_rounds,
        "worst_q_star": worst_q,
        "worst_eta_star": worst_eta,
        "worst_alignment_floor": worst_floor,
    }
    return summary, timeseries


def run_circuit_replay(
    trace: list[CircuitRound],
) -> tuple[list[dict[str, float | str]], list[dict[str, float | str]]]:
    diagnostics = [
        {
            "syndrome_mi_bits": circuit_error_syndrome_mi(item.noise),
            "logical_record_leakage_bits": conditional_logical_record_leakage(item.noise),
        }
        for item in trace
    ]
    summaries = []
    timeseries = []
    for protocol in CIRCUIT_PROTOCOLS:
        summary, protocol_timeseries = run_circuit_protocol(protocol, trace, diagnostics)
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
    instant_proxy_error = next(
        float(row["logical_error"])
        for row in summaries
        if row["protocol"] == "instant_proxy_decoder"
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
        row["instant_proxy_gap_log10"] = math.log10(
            (adaptive_error + 1e-15) / (instant_proxy_error + 1e-15)
        )
        row["best_protocol"] = best_protocol

    return summaries, timeseries


def run_calibration_phase_scan(args: argparse.Namespace) -> list[dict[str, float | str]]:
    """Replay all calibration-schedule offsets for the synthetic H2 trace.

    This does not change the code, decoder family, or physical noise trajectory.
    It changes only which residue class of rounds receives a fresh calibration
    record, so the headline adaptive result is tested against schedule-phase
    artifacts rather than only against the terminal stopping phase.
    """

    period = max(1, int(args.calibration_period))
    rows: list[dict[str, float | str]] = []
    for phase in range(period):
        phase_trace = generate_circuit_trace(
            None,
            total_rounds=args.rounds,
            anisotropy=args.anisotropy,
            drift_cycles=args.drift_cycles,
            calibration_period=period,
            calibration_phase=phase,
            seed=args.seed,
            crosstalk_scale=args.crosstalk_scale,
            leakage_scale=args.leakage_scale,
        )
        phase_summaries, _ = run_circuit_replay(phase_trace)
        for summary in phase_summaries:
            row = dict(summary)
            row["calibration_phase"] = float(phase)
            row["phase_scan_period"] = float(period)
            rows.append(row)
    return rows


def attach_phase_scan_metrics(
    summaries: list[dict[str, float | str]],
    phase_rows: list[dict[str, float | str]],
) -> None:
    if not phase_rows:
        return

    rows_by_protocol: dict[str, list[dict[str, float | str]]] = {}
    for row in phase_rows:
        rows_by_protocol.setdefault(str(row["protocol"]), []).append(row)

    for summary in summaries:
        protocol = str(summary["protocol"])
        rows = rows_by_protocol.get(protocol, [])
        if not rows:
            continue
        logical_errors = np.asarray([float(row["logical_error"]) for row in rows], dtype=float)
        coherent_information = np.asarray(
            [float(row["logical_coherent_information_bits"]) for row in rows], dtype=float
        )
        pauli_error = np.asarray(
            [float(row["pauli_logical_error_probability"]) for row in rows], dtype=float
        )
        pauli_coherent_information = np.asarray(
            [float(row["pauli_logical_coherent_information_bits"]) for row in rows],
            dtype=float,
        )
        adaptive_benefit = np.asarray(
            [float(row["adaptive_benefit_log10"]) for row in rows], dtype=float
        )
        summary["schedule_phase_count"] = float(len(rows))
        summary["schedule_phase_mean_logical_error"] = float(np.mean(logical_errors))
        summary["schedule_phase_std_logical_error"] = float(np.std(logical_errors))
        summary["schedule_phase_min_logical_error"] = float(np.min(logical_errors))
        summary["schedule_phase_max_logical_error"] = float(np.max(logical_errors))
        summary["schedule_phase_span_logical_error"] = float(
            np.max(logical_errors) - np.min(logical_errors)
        )
        summary["schedule_phase_mean_coherent_information_bits"] = float(
            np.mean(coherent_information)
        )
        summary["schedule_phase_mean_pauli_logical_error_probability"] = float(
            np.mean(pauli_error)
        )
        summary["schedule_phase_mean_pauli_coherent_information_bits"] = float(
            np.mean(pauli_coherent_information)
        )
        summary["schedule_phase_mean_adaptive_benefit_log10"] = float(
            np.mean(adaptive_benefit)
        )
        summary["schedule_phase_min_adaptive_benefit_log10"] = float(
            np.min(adaptive_benefit)
        )
        summary["schedule_phase_max_adaptive_benefit_log10"] = float(
            np.max(adaptive_benefit)
        )


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


def write_curves(trace: list[CircuitRound], summaries: list[dict[str, float | str]], timeseries: list[dict[str, float | str]]) -> None:
    fig, axes = plt.subplots(4, 1, figsize=(11, 12.5), constrained_layout=True)

    for summary in summaries:
        protocol = str(summary["protocol"])
        series = protocol_series(timeseries, protocol)
        axes[0].plot(
            [float(row["round"]) for row in series],
            [float(row["logical_error"]) for row in series],
            label=protocol,
            linewidth=1.8,
        )
    axes[0].set_title("Circuit-level replay logical error")
    axes[0].set_xlabel("round")
    axes[0].set_ylabel("logical failure probability")
    axes[0].grid(alpha=0.25)
    axes[0].legend(ncols=2, fontsize=8)

    x = [item.round_index for item in trace]
    proxy_rates = [decoder_proxy_rates(item.noise) for item in trace]
    for qubit in range(N_QUBITS):
        axes[1].plot(
            x,
            [float(rates[qubit]) for rates in proxy_rates],
            label=f"proxy p{qubit}",
            linewidth=1.5,
        )
        fresh_x = [item.round_index for item in trace if item.calibration_fresh]
        fresh_y = [
            float(item.calib_rates[qubit]) for item in trace if item.calibration_fresh
        ]
        axes[1].scatter(fresh_x, fresh_y, s=18, alpha=0.75)
    axes[1].set_title("Circuit fault trace compressed to decoder likelihoods")
    axes[1].set_xlabel("round")
    axes[1].set_ylabel("single-error proxy probability")
    axes[1].grid(alpha=0.25)
    axes[1].legend(ncols=3, fontsize=8)

    reference = protocol_series(timeseries, "adaptive_decoder")
    axes[2].plot(
        [float(row["round"]) for row in reference],
        [float(row["syndrome_mi_bits"]) for row in reference],
        label="I(error; syndrome)",
        linewidth=1.8,
    )
    axes[2].plot(
        [float(row["round"]) for row in reference],
        [float(row["logical_record_leakage_bits"]) for row in reference],
        label="I(logical; record | error)",
        linewidth=1.8,
    )
    for row in reference:
        if float(row["updated"]) > 0.5:
            axes[2].axvline(float(row["round"]), color="black", linewidth=0.7, alpha=0.18)
    axes[2].set_title("Controller-record audit; vertical marks are adaptive updates")
    axes[2].set_xlabel("round")
    axes[2].set_ylabel("bits")
    axes[2].grid(alpha=0.25)
    axes[2].legend(fontsize=8)

    axes[3].plot(
        [float(row["round"]) for row in reference],
        [float(row["pauli_logical_ptm_xx"]) for row in reference],
        label="Pauli PTM XX",
        linewidth=1.8,
    )
    axes[3].plot(
        [float(row["round"]) for row in reference],
        [float(row["pauli_logical_ptm_zz"]) for row in reference],
        label="Pauli PTM ZZ",
        linewidth=1.8,
    )
    axes[3].plot(
        [float(row["round"]) for row in reference],
        [float(row["pauli_logical_coherent_information_bits"]) for row in reference],
        label="Pauli coherent information",
        linewidth=1.8,
    )
    axes[3].axhline(0.0, color="black", linewidth=0.8, alpha=0.45)
    axes[3].set_title("Adaptive Pauli-frame logical-channel audit")
    axes[3].set_xlabel("round")
    axes[3].set_ylabel("process metric")
    axes[3].grid(alpha=0.25)
    axes[3].legend(fontsize=8)

    fig.suptitle("H2 circuit-level syndrome extraction: fixed logical code")
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
    parser.add_argument("--calibration-phase", type=int, default=0)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--crosstalk-scale", type=float, default=DEFAULT_CROSSTALK_SCALE)
    parser.add_argument("--leakage-scale", type=float, default=DEFAULT_LEAKAGE_SCALE)
    parser.add_argument(
        "--skip-phase-scan",
        action="store_true",
        help="skip the synthetic calibration schedule-phase replay audit",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    generated_trace = bool(args.generate_example or not args.trace.exists())
    if args.generate_example or not args.trace.exists():
        trace = generate_circuit_trace(
            args.trace,
            total_rounds=args.rounds,
            anisotropy=args.anisotropy,
            drift_cycles=args.drift_cycles,
            calibration_period=args.calibration_period,
            calibration_phase=args.calibration_phase,
            seed=args.seed,
            crosstalk_scale=args.crosstalk_scale,
            leakage_scale=args.leakage_scale,
        )
    else:
        trace = read_circuit_trace(args.trace)

    summaries, timeseries = run_circuit_replay(trace)
    phase_rows: list[dict[str, float | str]] = []
    if generated_trace and not args.skip_phase_scan:
        phase_rows = run_calibration_phase_scan(args)
        attach_phase_scan_metrics(summaries, phase_rows)
        write_csv(PHASE_SCAN_SUMMARY_PATH, phase_rows)

    write_csv(SUMMARY_PATH, summaries)
    write_csv(TIMESERIES_PATH, timeseries)
    write_curves(trace, summaries, timeseries)

    adaptive = next(row for row in summaries if row["protocol"] == "adaptive_decoder")
    best = min(summaries, key=lambda row: float(row["logical_error"]))

    print(f"read circuit trace {args.trace}")
    print(f"wrote {SUMMARY_PATH}")
    print(f"wrote {TIMESERIES_PATH}")
    print(f"wrote {CURVES_PATH}")
    if phase_rows:
        print(f"wrote {PHASE_SCAN_SUMMARY_PATH}")
    print(
        "adaptive circuit benefit: "
        f"{float(adaptive['adaptive_benefit_log10']):.3f} log10; "
        f"updates={int(float(adaptive['updates']))}; "
        f"logical_error={float(adaptive['logical_error']):.5f}"
    )
    print(
        "controller audit: "
        f"avg I(error;syndrome)={float(adaptive['avg_syndrome_mi_bits']):.5f} bits; "
        "avg I(logical;record|error)="
        f"{float(adaptive['avg_logical_record_leakage_bits']):.5e} bits"
    )
    print(
        "logical process audit: "
        f"p01={float(adaptive['logical_p01']):.5f}; "
        f"p10={float(adaptive['logical_p10']):.5f}; "
        f"PTM_YY_ZZ={float(adaptive['logical_ptm_zz']):.5f}; "
        f"Ic={float(adaptive['logical_coherent_information_bits']):.5f} bits; "
        f"phase_avg_error={float(adaptive['phase_avg_logical_error']):.5f}"
    )
    print(
        "Pauli-frame audit: "
        f"pI={float(adaptive['pauli_logical_p_i']):.5f}; "
        f"pX={float(adaptive['pauli_logical_p_x']):.5f}; "
        f"pY={float(adaptive['pauli_logical_p_y']):.5f}; "
        f"pZ={float(adaptive['pauli_logical_p_z']):.5f}; "
        f"PTM=({float(adaptive['pauli_logical_ptm_xx']):.5f}, "
        f"{float(adaptive['pauli_logical_ptm_yy']):.5f}, "
        f"{float(adaptive['pauli_logical_ptm_zz']):.5f}); "
        f"Ic={float(adaptive['pauli_logical_coherent_information_bits']):.5f} bits"
    )
    if phase_rows:
        print(
            "schedule phase audit: "
            "adaptive mean_error="
            f"{float(adaptive['schedule_phase_mean_logical_error']):.5f}; "
            "span="
            f"{float(adaptive['schedule_phase_span_logical_error']):.5f}; "
            "mean_benefit="
            f"{float(adaptive['schedule_phase_mean_adaptive_benefit_log10']):.3f} log10"
        )
    print(
        "best circuit protocol: "
        f"{best['protocol']} with logical_error={float(best['logical_error']):.5f}; "
        f"instant_proxy_gap={float(adaptive['instant_proxy_gap_log10']):.3f} log10"
    )


if __name__ == "__main__":
    main()
