#!/usr/bin/env python3
"""Area-derived record capacity for the relational macrocell collapse toy.

Executable companion to Conjecture SE-1 of
`bridges/crystallization_sorting_engine.md`, closing OP-30 task (a).

SE-1 says the scale at which quantum gravity must modify classical collapse is
set by where the contraction first exceeds the boundary export capacity, rather
than by a fixed curvature threshold alone. Turning that into a number needs
three things this toy can supply and one it cannot:

1. the interior contraction gamma, measured from the toy's own kernel;
2. the exported record sigma, measured from the toy's own boundary bins;
3. the slot resolution of the toy's record map;
4. a boundary capacity in bits, which requires the Bekenstein-Hawking area law
   and an explicit mass calibration -- imported physics, not toy output.

This script computes all four and reports the crossing test honestly, including
the outcome that inside this toy the crossing does not occur.

Ledger and bound
----------------
A rate ledger is measured; a stock bound is derived. They answer different
questions.

**Rate ledger** (fresh reference each step). Take the reference to be the
current macrocell X_k = M_k. Because the toy's boundary record is a
deterministic function of the macrocell, one step gives

    delta_k = H(M_k) - I(M_k; M_{k+1})
    sigma_k = I(M_k; R_{k+1})
    gamma_k = sigma_k + delta_k

exactly. This is the instantaneous merging rate of the coarse kernel against
the instantaneous record yield, which is the quantity SE-1 compares to a
capacity rate.

**Stock bound.** The Bekenstein bound constrains what the record register
*holds*, not what it carries per step, so the area comparison needs the
cumulative export E = I(S0; R_<=k) rather than a rate. Exact record-history
tracking over 36 steps with 15 record values is not affordable, and pruned
branch tracking was tried and rejected: the surviving-mass error swamped the
signal. It is also unnecessary, because Theorem 1 gives the exact bound

    E_k  <=  H(S0)  for every k,

with H(S0) the entropy of the toy's initial macrocell distribution. That single
number is an upper bound over all time on everything the toy's boundary
register can ever be asked to hold, and it settles the area comparison without
approximation.

Capacities
----------
    C_slots = log2(number of distinct boundary record tuples)   [toy-intrinsic]
    C_area  = A / (4 ln 2) = 4 pi M^2 / (C_R^2 ln 2) bits        [imported]

in Planck units, using the toy's own compactness C_R = 2M/R_areal so that
A = 4 pi R_areal^2 = 16 pi M^2 / C_R^2. The quantum-record form is 2 C_area,
per Theorem 4-Q.
"""

from __future__ import annotations

import csv
import functools
import math
from collections import defaultdict
from pathlib import Path

from cosmic_coordination_floor import (
    CENTERS,
    COMPACTNESS_BIN_COUNT,
    HORIZON_TRANSFER_CENTER,
    HORIZON_TRANSFER_SIGMA,
    HORIZON_TRIGGER_C,
    QG_TRANSFER_SIGMA,
    QG_TRIGGER_C,
    STEPS,
    Macrocell,
    collapse_center,
    collapse_sigma,
    entropy_bits,
    gaussian_weights,
    initial_distribution,
    macrocell_from_index,
    mixture_weights,
    normalize,
    normalize_distribution,
    singular_escape_probability,
)


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
RATE_CSV = OUT / "area_capacity_rate_ledger.csv"
SUMMARY_CSV = OUT / "area_capacity_summary.csv"
CALIBRATION_CSV = OUT / "area_capacity_calibration.csv"
MARGINALITY_CSV = OUT / "area_capacity_marginality.csv"

POLICIES = ["naked_collapse", "hard_exclusion", "horizon_transfer", "quantum_completion"]

LN2 = math.log(2.0)
CALIBRATION_MASSES = [0.25, 0.5, 1.0, 3.0, 10.0]
MARGINALITY_MASSES = [1.0, 10.0, 1e3, 1e38]

Record = tuple[int, int, int]
Distribution = dict[Macrocell, float]


# --------------------------------------------------------------------------
# macrocell bookkeeping
# --------------------------------------------------------------------------


@functools.lru_cache(maxsize=None)
def cached_macrocell(index: int, kind: str) -> Macrocell:
    return macrocell_from_index(index, kind)


@functools.lru_cache(maxsize=None)
def record_of(cell: Macrocell) -> Record:
    """The finite boundary record: area, null, and radiation bins."""

    return (cell.boundary_area, cell.null_record, cell.radiation_record)


@functools.lru_cache(maxsize=None)
def cell_universe() -> tuple[tuple[Macrocell, ...], dict[Macrocell, int]]:
    cells: list[Macrocell] = []
    for kind in ("quiet", "collapse", "horizon", "qg"):
        for index in range(COMPACTNESS_BIN_COUNT):
            cells.append(cached_macrocell(index, kind))
    ordered = tuple(dict.fromkeys(cells))
    return ordered, {cell: i for i, cell in enumerate(ordered)}


SLOT_COUNT = len({record_of(cell) for cell in cell_universe()[0]})
C_SLOTS_BITS = math.log2(SLOT_COUNT)


# --------------------------------------------------------------------------
# one-step kernel, with the source retained
# --------------------------------------------------------------------------


@functools.lru_cache(maxsize=None)
def cell_targets(policy: str, cell: Macrocell) -> tuple[dict[Macrocell, float], float]:
    """Targets and singular mass for one source cell, mirroring `transition`."""

    compactness = CENTERS[cell.compactness]
    targets: defaultdict[Macrocell, float] = defaultdict(float)

    def spread(weights: list[float], mass: float, kind: str) -> None:
        for index, weight in enumerate(normalize(weights)):
            if weight > 0.0:
                targets[cached_macrocell(index, kind)] += mass * weight

    if policy == "horizon_transfer" and compactness >= HORIZON_TRIGGER_C:
        spread(gaussian_weights(HORIZON_TRANSFER_CENTER, HORIZON_TRANSFER_SIGMA), 1.0, "horizon")
        return dict(targets), 0.0

    if policy == "quantum_completion" and compactness >= QG_TRIGGER_C:
        spread(
            mixture_weights(
                [(0.34, QG_TRANSFER_SIGMA, 0.58), (0.55, QG_TRANSFER_SIGMA * 1.25, 0.42)]
            ),
            1.0,
            "qg",
        )
        return dict(targets), 0.0

    center = collapse_center(compactness)
    sigma = collapse_sigma(compactness)
    singular = singular_escape_probability(center) if policy == "naked_collapse" else 0.0
    spread(gaussian_weights(min(center, 0.995), sigma), 1.0 - singular, "collapse")
    return dict(targets), singular


# --------------------------------------------------------------------------
# information helpers
# --------------------------------------------------------------------------


def clamp(value: float, tolerance: float = 1e-12) -> float:
    return 0.0 if abs(value) < tolerance else float(value)


def mutual_information(joint: dict[tuple, float]) -> float:
    total = sum(joint.values())
    if total <= 0.0:
        return 0.0
    px: defaultdict = defaultdict(float)
    py: defaultdict = defaultdict(float)
    for (x, y), mass in joint.items():
        px[x] += mass / total
        py[y] += mass / total
    info = 0.0
    for (x, y), mass in joint.items():
        p = mass / total
        denominator = px[x] * py[y]
        if p > 0.0 and denominator > 0.0:
            info += p * math.log2(p / denominator)
    return max(0.0, info)


# --------------------------------------------------------------------------
# rate ledger
# --------------------------------------------------------------------------


def rate_ledger(policy: str) -> list[dict[str, float | str]]:
    distribution = normalize_distribution(initial_distribution())
    rows: list[dict[str, float | str]] = []

    for step in range(STEPS):
        joint: defaultdict[tuple[Macrocell, Macrocell], float] = defaultdict(float)
        for cell, mass in distribution.items():
            if mass <= 0.0:
                continue
            targets, _singular = cell_targets(policy, cell)
            for target, weight in targets.items():
                joint[(cell, target)] += mass * weight

        total = sum(joint.values())
        if total <= 0.0:
            break
        scaled = {key: value / total for key, value in joint.items()}

        source_record: defaultdict[tuple[Macrocell, Record], float] = defaultdict(float)
        record_marginal: defaultdict[Record, float] = defaultdict(float)
        successor: defaultdict[Macrocell, float] = defaultdict(float)
        for (source, target), mass in scaled.items():
            source_record[(source, record_of(target))] += mass
            record_marginal[record_of(target)] += mass
            successor[target] += mass

        h_source = entropy_bits(list(distribution.values()))
        sigma = clamp(mutual_information(dict(source_record)))
        delta = clamp(h_source - mutual_information(scaled))
        gamma = clamp(sigma + delta)

        normalized = normalize_distribution(dict(successor))
        rows.append(
            {
                "policy": policy,
                "step": step + 1,
                "mean_compactness": sum(
                    mass * CENTERS[cell.compactness] for cell, mass in normalized.items()
                ),
                "source_entropy_bits": clamp(h_source),
                "contraction_bits": gamma,
                "sorted_bits": sigma,
                "destroyed_bits": delta,
                "step_efficiency": (sigma / gamma) if gamma > 1e-12 else "",
                "record_entropy_bits": clamp(entropy_bits(list(record_marginal.values()))),
                "active_slots": len([m for m in record_marginal.values() if m > 1e-15]),
                "slot_capacity_bits": C_SLOTS_BITS,
                "bandwidth_limited": float(gamma > C_SLOTS_BITS + 1e-12),
                "bandwidth_slack_bits": clamp(delta - max(0.0, gamma - C_SLOTS_BITS)),
            }
        )
        distribution = normalized

    return rows


# --------------------------------------------------------------------------
# stock ledger
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# area calibration
# --------------------------------------------------------------------------


def bekenstein_bits(mass: float, compactness: float) -> float:
    """S_BH = A/4 in Planck units, converted to bits.

    C_R = 2M/R gives R = 2M/C_R, so A = 4 pi R^2 = 16 pi M^2 / C_R^2 and
    S = A/4 = 4 pi M^2 / C_R^2 nats.
    """

    compactness = max(compactness, 1e-6)
    return 4.0 * math.pi * mass * mass / (compactness * compactness * LN2)


def crossing_mass(budget_bits: float, compactness: float) -> float:
    """Mass below which the area capacity falls under a given interior budget."""

    return compactness * math.sqrt(max(budget_bits, 0.0) * LN2 / (4.0 * math.pi))


def calibration_rows(interior_budget_bits: float) -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for mass in CALIBRATION_MASSES:
        for compactness in (0.12, 0.35, 0.66, 0.78, 1.0):
            classical = bekenstein_bits(mass, compactness)
            rows.append(
                {
                    "mass_planck": mass,
                    "compactness": compactness,
                    "areal_radius_planck": 2.0 * mass / compactness,
                    "area_capacity_classical_bits": classical,
                    "area_capacity_quantum_bits": 2.0 * classical,
                    "toy_interior_budget_bits": interior_budget_bits,
                    "toy_slot_capacity_bits": C_SLOTS_BITS,
                    "binding_constraint": (
                        "slot_resolution" if C_SLOTS_BITS < classical else "area_capacity"
                    ),
                    "area_capacity_over_interior_budget": classical / interior_budget_bits,
                }
            )
    return rows


def marginality_rows() -> list[dict[str, float | str]]:
    """Interior budget against horizon record capacity for a real horizon.

    Standard counting gives a horizon of area A about exp(S_BH) interior
    microstates, so the quantum interior budget of Corollary 6.1 is
    2 H(R) = 2 S_BH bits. A horizon record of S_BH qubits carries at most
    2 S_BH bits of quantum mutual information (Theorem 4-Q) and at most S_BH
    bits once decohered (Theorem 7).
    """

    rows: list[dict[str, float | str]] = []
    for mass in MARGINALITY_MASSES:
        s_bh = bekenstein_bits(mass, 1.0)
        rows.append(
            {
                "mass_planck": mass,
                "horizon_entropy_bits": s_bh,
                "interior_budget_quantum_bits": 2.0 * s_bh,
                "record_capacity_quantum_bits": 2.0 * s_bh,
                "record_capacity_classical_bits": s_bh,
                "quantum_capacity_margin_bits": 0.0,
                "chi_max_quantum_record": 1.0,
                "chi_max_classical_record": 0.5,
            }
        )
    return rows


# --------------------------------------------------------------------------


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(policy: str, rate_rows: list[dict], interior_budget: float) -> dict[str, float | str]:
    steps = len(rate_rows)
    gamma_total = clamp(sum(float(r["contraction_bits"]) for r in rate_rows))
    sigma_total = clamp(sum(float(r["sorted_bits"]) for r in rate_rows))
    delta_total = clamp(sum(float(r["destroyed_bits"]) for r in rate_rows))
    identity = max(
        abs(float(r["contraction_bits"]) - float(r["sorted_bits"]) - float(r["destroyed_bits"]))
        for r in rate_rows
    )
    peak_gamma = max(float(r["contraction_bits"]) for r in rate_rows)
    peak_record = max(float(r["record_entropy_bits"]) for r in rate_rows)
    limited = sum(int(float(r["bandwidth_limited"])) for r in rate_rows)
    min_slack = min(float(r["bandwidth_slack_bits"]) for r in rate_rows)
    return {
        "policy": policy,
        "steps": steps,
        "mean_contraction_bits": round(gamma_total / steps, 6),
        "mean_sorted_bits": round(sigma_total / steps, 6),
        "mean_destroyed_bits": round(delta_total / steps, 6),
        "chi": round(sigma_total / gamma_total, 6) if gamma_total > 1e-12 else "",
        "peak_contraction_bits": round(peak_gamma, 6),
        "peak_record_entropy_bits": round(peak_record, 6),
        "slot_capacity_bits": round(C_SLOTS_BITS, 6),
        "peak_contraction_over_slot_capacity": round(peak_gamma / C_SLOTS_BITS, 6),
        "bandwidth_limited_steps": limited,
        "min_bandwidth_slack_bits": round(min_slack, 6),
        "interior_stock_bound_bits": round(interior_budget, 6),
        "max_identity_residual": f"{identity:.3e}",
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    initial = normalize_distribution(initial_distribution())
    interior_budget = entropy_bits(list(initial.values()))

    rate_rows: list[dict] = []
    summaries: list[dict] = []
    for policy in POLICIES:
        rate = rate_ledger(policy)
        rate_rows.extend(rate)
        summaries.append(summarize(policy, rate, interior_budget))

    calibration = calibration_rows(interior_budget)
    marginality = marginality_rows()

    write_csv(RATE_CSV, rate_rows)
    write_csv(SUMMARY_CSV, summaries)
    write_csv(CALIBRATION_CSV, calibration)
    write_csv(MARGINALITY_CSV, marginality)

    print(f"toy interior budget H(M0)      = {interior_budget:.6f} bits")
    print(f"toy boundary record slots      = {SLOT_COUNT}  ->  C_slots = {C_SLOTS_BITS:.6f} bits")
    print(f"rate ledger over {STEPS} steps; stock bound E <= H(M0) holds for all time")
    print()

    header = (
        f"{'policy':<21}{'mean_g':>9}{'mean_s':>9}{'mean_d':>9}{'chi':>9}"
        f"{'peak_g':>9}{'g/Cslot':>9}{'BW-lim':>8}{'slack':>9}"
    )
    print(header)
    print("-" * len(header))
    for row in summaries:
        print(
            f"{row['policy']:<21}{float(row['mean_contraction_bits']):>9.4f}"
            f"{float(row['mean_sorted_bits']):>9.4f}{float(row['mean_destroyed_bits']):>9.4f}"
            f"{float(row['chi']):>9.5f}"
            f"{float(row['peak_contraction_bits']):>9.4f}"
            f"{float(row['peak_contraction_over_slot_capacity']):>9.4f}"
            f"{int(row['bandwidth_limited_steps']):>8}"
            f"{float(row['min_bandwidth_slack_bits']):>9.4f}"
        )

    print()
    print("area-derived capacity (Planck units, S = A / 4 ln2 bits)")
    print(
        f"{'M':>7}{'C_R':>7}{'R':>9}{'C_area':>13}{'2*C_area':>13}"
        f"{'C_area/budget':>15}{'binding':>17}"
    )
    for row in calibration:
        print(
            f"{float(row['mass_planck']):>7.2f}{float(row['compactness']):>7.2f}"
            f"{float(row['areal_radius_planck']):>9.2f}"
            f"{float(row['area_capacity_classical_bits']):>13.4g}"
            f"{float(row['area_capacity_quantum_bits']):>13.4g}"
            f"{float(row['area_capacity_over_interior_budget']):>15.4g}"
            f"{str(row['binding_constraint']):>17}"
        )

    smallest = min(float(r["area_capacity_classical_bits"]) for r in calibration)
    print()
    print(f"smallest tabulated area capacity : {smallest:.4f} bits")
    print(f"toy slot capacity                : {C_SLOTS_BITS:.4f} bits")
    print(f"toy interior budget              : {interior_budget:.4f} bits")
    print("SE-1 crossing needs the area capacity to fall below the interior budget:")
    for compactness in (0.66, 0.78, 1.0):
        star = crossing_mass(interior_budget, compactness)
        print(
            f"  at C_R = {compactness:.2f}, that needs M < {star:.4f} Planck masses"
            f"  ({'sub-Planckian' if star < 1.0 else 'super-Planckian'})"
        )

    print()
    print("horizon marginality: interior budget against horizon record capacity")
    print(
        f"{'M':>10}{'S_BH bits':>14}{'budget 2S':>14}{'quantum cap':>14}"
        f"{'classical cap':>15}{'chi_max_cl':>12}"
    )
    for row in marginality:
        print(
            f"{float(row['mass_planck']):>10.4g}{float(row['horizon_entropy_bits']):>14.4g}"
            f"{float(row['interior_budget_quantum_bits']):>14.4g}"
            f"{float(row['record_capacity_quantum_bits']):>14.4g}"
            f"{float(row['record_capacity_classical_bits']):>15.4g}"
            f"{float(row['chi_max_classical_record']):>12.2f}"
        )

    print()
    for row in summaries:
        print(
            f"{row['policy']}: identity residual {row['max_identity_residual']}, "
            f"{row['bandwidth_limited_steps']}/{row['steps']} bandwidth-limited steps, "
            f"min slack {row['min_bandwidth_slack_bits']} bits"
        )


if __name__ == "__main__":
    main()
