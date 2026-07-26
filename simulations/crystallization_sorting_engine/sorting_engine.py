#!/usr/bin/env python3
"""Distinguishability ledger for the crystallization sorting engine.

This is the executable companion to `bridges/crystallization_sorting_engine.md`.
It is not a gravitational simulation. It is an exact finite-information model of
the claim that contraction toward the crystallization boundary is the only
source of exportable boundary records, and that the resulting sorting operation
is either lossless or wasteful depending on whether distinctions are exported
before they are merged.

Model
-----
An interior microstate is a pair

    s = (g, l)

where `g` is a sector label (the QEC error sector / gravitational geometry
sector) and `l` is a protected label (the logical state / interior microstate).
`S0` is the initial microstate, uniform over `N_G * N_L` values.

The interior register `M_k` carries a coarsened label in which either
coordinate may have been merged away, written `None`. Each step applies:

1. an emission channel (the sorter), which reads the interior label and places
   it into one of finitely many slots, or emits the null symbol;
2. a contraction channel, which merges one still-present coordinate with
   probability `rate`.

Both channels depend only on `(M_k, R_{<=k})`, never on `S0` directly, so the
chain `S0 -> (M_k, R_{<=k}) -> (M_{k+1}, R_{<=k+1})` is Markov and the data
processing inequality applies.

Ledger
------
    T_k = I(S0; M_k, R_{<=k})      total surviving distinguishability
    E_k = I(S0; R_{<=k})           exported (sorted) column
    J_k = I(S0; M_k | R_{<=k})     retained interior column (the backlog)

with `T_k = J_k + E_k` exactly. Per step,

    gamma_k = J_k - J_{k+1}        interior contraction   (>= 0)
    sigma_k = E_{k+1} - E_k        sorted output          (>= 0)
    delta_k = T_k - T_{k+1}        destroyed              (>= 0)
    gamma_k = sigma_k + delta_k    ledger identity

and the sorting efficiency is `chi = sum(sigma) / sum(gamma)`.

Two bounds are checked numerically at every step:

    sigma_k <= gamma_k                      no record without contraction
    delta_k >= gamma_k - C_k                bandwidth-limited sorting

where `C_k = log2(#slots)` is the per-step record capacity.

Exactness
---------
The joint distribution over `(S0, M_k, R_{<=k})` is propagated as a list of
record branches, each holding a normalized joint over `(S0, M)` plus a weight.
Branches whose posteriors coincide are merged, which is exact because every
reported quantity depends on the record only through the branch posterior and
its weight. No sampling is used.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Sequence


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
LEDGER_CSV = OUT / "sorting_engine_ledger.csv"
SUMMARY_CSV = OUT / "sorting_engine_summary.csv"
SCAN_CSV = OUT / "sorting_engine_throughput_scan.csv"
LEDGER_SVG = OUT / "sorting_engine_ledger.svg"
FRONTIER_SVG = OUT / "sorting_engine_throughput_frontier.svg"

N_G = 3
N_L = 3
STEPS = 24
SWITCH_STEP = 10
LATE_TRIGGER_STEP = 14
SCAN_EMITS = (0.1, 0.4, 0.7, 1.0)
EMIT_PROB = 0.30
GATED_RATE = 0.60
MERGE_TOLERANCE = 12

Micro = tuple[int, int]
Label = tuple[int | None, int | None]
Reading = tuple[str, int]

NULL: Reading = ("null", 0)

MICROSTATES: list[Micro] = [(g, l) for g in range(N_G) for l in range(N_L)]
H_S0 = math.log2(len(MICROSTATES))
H_G = math.log2(N_G)
H_L_GIVEN_G = math.log2(N_L)


# --------------------------------------------------------------------------
# information helpers
# --------------------------------------------------------------------------


def clamp(value: float, tolerance: float = 1e-12) -> float:
    """Round away signed-zero and sub-tolerance numerical dust."""

    return 0.0 if abs(value) < tolerance else value


def entropy_bits(weights: Iterable[float]) -> float:
    total = sum(weights)
    if total <= 0.0:
        return 0.0
    acc = 0.0
    for w in weights:
        if w > 0.0:
            p = w / total
            acc -= p * math.log2(p)
    return acc


def label_support(label: Label) -> frozenset[Micro]:
    g, l = label
    return frozenset(
        (gg, ll)
        for (gg, ll) in MICROSTATES
        if (g is None or gg == g) and (l is None or ll == l)
    )


# --------------------------------------------------------------------------
# channels
# --------------------------------------------------------------------------


Partition = list[frozenset[Micro]]


def trivial_partition() -> Partition:
    """One slot. Finite bandwidth, zero resolution: a bare 'collapse happened' flag."""

    return [frozenset(MICROSTATES)]


def sector_partition() -> Partition:
    return [frozenset((g, l) for l in range(N_L)) for g in range(N_G)]


def protected_partition() -> Partition:
    return [frozenset((g, l) for g in range(N_G)) for l in range(N_L)]


def singleton_partition() -> Partition:
    return [frozenset({s}) for s in MICROSTATES]


def sorter(partition: Partition, emit_prob: float) -> Callable[[Label], list[tuple[Reading, float]]]:
    """A slot sorter.

    The sorter can only place a label into a slot when the label's whole
    support lies inside one block. A coin whose denomination has already been
    melted away cannot be filed.
    """

    def channel(label: Label) -> list[tuple[Reading, float]]:
        support = label_support(label)
        for index, block in enumerate(partition):
            if support <= block:
                if emit_prob >= 1.0:
                    return [(("slot", index), 1.0)]
                return [(("slot", index), emit_prob), (NULL, 1.0 - emit_prob)]
        return [(NULL, 1.0)]

    return channel


def contraction(
    label: Label,
    rate: float,
    gated: bool,
    merge_all: bool,
    g_known: bool,
    l_known: bool,
) -> list[tuple[Label, float]]:
    """Merge interior distinctions with probability `rate`.

    Ungated contraction crushes fine structure first and then coarse structure,
    regardless of what has been exported. Gated contraction merges a coordinate
    only once the accumulated record already determines it. With `merge_all`,
    every remaining distinction is annihilated in a single step: the singular
    endpoint rather than a graded coarsening.
    """

    g, l = label
    if rate <= 0.0:
        return [(label, 1.0)]

    merged: Label
    if merge_all:
        if g is None and l is None:
            return [(label, 1.0)]
        if gated and not (g_known and l_known):
            return [(label, 1.0)]
        merged = (None, None)
    else:
        target: str | None = None
        if l is not None and (l_known or not gated):
            target = "l"
        elif g is not None and (g_known or not gated):
            target = "g"
        if target is None:
            return [(label, 1.0)]
        merged = (g, None) if target == "l" else (None, l)

    if rate >= 1.0:
        return [(merged, 1.0)]
    return [(merged, rate), (label, 1.0 - rate)]


# --------------------------------------------------------------------------
# branch state
# --------------------------------------------------------------------------


Joint = dict[tuple[Micro, Label], float]


@dataclass
class Branch:
    weight: float
    joint: Joint  # normalized within the branch

    def posterior_s0(self) -> dict[Micro, float]:
        out: dict[Micro, float] = {}
        for (s0, _label), p in self.joint.items():
            out[s0] = out.get(s0, 0.0) + p
        return out

    def conditional_entropy_s0_given_m(self) -> float:
        by_label: dict[Label, dict[Micro, float]] = {}
        for (s0, label), p in self.joint.items():
            by_label.setdefault(label, {})[s0] = by_label.setdefault(label, {}).get(s0, 0.0) + p
        acc = 0.0
        for label, table in by_label.items():
            mass = sum(table.values())
            if mass > 0.0:
                acc += mass * entropy_bits(table.values())
        return acc

    def entropy_g(self) -> float:
        table: dict[int, float] = {}
        for (s0, _label), p in self.joint.items():
            table[s0[0]] = table.get(s0[0], 0.0) + p
        return entropy_bits(table.values())

    def conditional_entropy_l_given_g(self) -> float:
        by_g: dict[int, dict[int, float]] = {}
        for (s0, _label), p in self.joint.items():
            by_g.setdefault(s0[0], {})
            by_g[s0[0]][s0[1]] = by_g[s0[0]].get(s0[1], 0.0) + p
        acc = 0.0
        for g, table in by_g.items():
            mass = sum(table.values())
            if mass > 0.0:
                acc += mass * entropy_bits(table.values())
        return acc

    def g_known(self) -> bool:
        return self.entropy_g() <= 1e-12

    def l_known(self) -> bool:
        return self.conditional_entropy_l_given_g() <= 1e-12


def initial_branch() -> Branch:
    mass = 1.0 / len(MICROSTATES)
    joint: Joint = {(s, (s[0], s[1])): mass for s in MICROSTATES}
    return Branch(weight=1.0, joint=joint)


def merge_branches(branches: Sequence[Branch]) -> list[Branch]:
    """Collapse branches with identical posteriors.

    Exact: every reported quantity is an expectation over branches of a
    function of the branch posterior alone.
    """

    table: dict[tuple, Branch] = {}
    for branch in branches:
        if branch.weight <= 0.0:
            continue
        key = tuple(
            sorted(
                (repr(s0), repr(label), round(p, MERGE_TOLERANCE))
                for (s0, label), p in branch.joint.items()
                if p > 0.0
            )
        )
        existing = table.get(key)
        if existing is None:
            table[key] = Branch(weight=branch.weight, joint=dict(branch.joint))
        else:
            existing.weight += branch.weight
    return list(table.values())


# --------------------------------------------------------------------------
# policy
# --------------------------------------------------------------------------


@dataclass
class Policy:
    name: str
    partition_at: Callable[[int], Partition]
    emit_at: Callable[[int], float]
    gated: bool
    rate_at: Callable[[int], float]
    note: str
    merge_all: bool = False


def emit_schedule(k: int) -> float:
    """Shared boundary-channel schedule.

    Before the decoding scale the exterior channel is throttled; at and after
    the decoding scale it runs at full rate. Every policy is given the same
    channel so that the comparison isolates what each policy reads and when it
    contracts, not how much bandwidth it was handed.
    """

    return EMIT_PROB if k < SWITCH_STEP else 1.0


def ramping_rate(k: int) -> float:
    """Classical focusing: contraction accelerates as the core concentrates."""

    return min(0.95, 0.10 + 0.055 * k)


def constant_rate(rate: float) -> Callable[[int], float]:
    return lambda _k: rate


def policies() -> list[Policy]:
    return [
        Policy(
            name="classical_collapse",
            partition_at=lambda _k: trivial_partition(),
            emit_at=emit_schedule,
            gated=False,
            rate_at=ramping_rate,
            note="finite bandwidth, zero resolution; crushes without sorting",
        ),
        Policy(
            name="over_driven_sorter",
            partition_at=lambda _k: sector_partition(),
            emit_at=emit_schedule,
            gated=False,
            rate_at=ramping_rate,
            note="informative slots, but contraction outruns export",
        ),
        Policy(
            name="sort_then_contract",
            partition_at=lambda k: (
                sector_partition()
                if k < SWITCH_STEP
                else (protected_partition() if (k - SWITCH_STEP) % 2 == 0 else sector_partition())
            ),
            emit_at=emit_schedule,
            gated=True,
            rate_at=constant_rate(GATED_RATE),
            note="merges only what the record already determines; late protected release",
        ),
        Policy(
            name="centralizing_sorter",
            partition_at=lambda _k: singleton_partition(),
            emit_at=emit_schedule,
            gated=True,
            rate_at=constant_rate(GATED_RATE),
            note="lossless but reads the protected label immediately",
        ),
        Policy(
            name="late_completion",
            partition_at=lambda k: (
                trivial_partition()
                if k < LATE_TRIGGER_STEP
                else (sector_partition() if k < LATE_TRIGGER_STEP + 4 else protected_partition())
            ),
            emit_at=emit_schedule,
            gated=False,
            rate_at=lambda k: 0.0 if k < LATE_TRIGGER_STEP else 0.95,
            note="right mechanism, triggered too late: one step of crush exceeds record capacity",
            merge_all=True,
        ),
        Policy(
            name="stalled_remnant",
            partition_at=lambda _k: sector_partition(),
            emit_at=emit_schedule,
            gated=True,
            rate_at=constant_rate(GATED_RATE),
            note="lossless but never opens a protected-release channel",
        ),
    ]


# --------------------------------------------------------------------------
# ledger
# --------------------------------------------------------------------------


@dataclass
class LedgerRow:
    policy: str
    step: int
    total_bits: float
    exported_bits: float
    retained_bits: float
    contraction_bits: float
    sorted_bits: float
    destroyed_bits: float
    step_efficiency: float
    cumulative_efficiency: float
    capacity_bits: float
    record_entropy_bits: float
    sector_exported_bits: float
    protected_leakage_bits: float
    bandwidth_slack_bits: float


def measure(branches: Sequence[Branch]) -> dict[str, float]:
    exported = H_S0
    total = H_S0
    sector = H_G
    leakage = H_L_GIVEN_G
    for branch in branches:
        posterior = branch.posterior_s0()
        exported -= branch.weight * entropy_bits(posterior.values())
        total -= branch.weight * branch.conditional_entropy_s0_given_m()
        sector -= branch.weight * branch.entropy_g()
        leakage -= branch.weight * branch.conditional_entropy_l_given_g()
    return {
        "exported": exported,
        "total": total,
        "retained": total - exported,
        "sector": sector,
        "leakage": leakage,
    }


def advance(
    branches: Sequence[Branch], policy: Policy, step: int
) -> tuple[list[Branch], float, float]:
    """One emission + contraction step. Returns (branches, capacity, record entropy)."""

    partition = policy.partition_at(step)
    emit = sorter(partition, policy.emit_at(step))
    capacity = math.log2(len(partition) + 1)
    rate = policy.rate_at(step)

    record_entropy = 0.0
    emitted: list[Branch] = []
    for branch in branches:
        outcome_mass: dict[Reading, float] = {}
        split: dict[Reading, Joint] = {}
        for (s0, label), p in branch.joint.items():
            for reading, prob in emit(label):
                if prob <= 0.0:
                    continue
                mass = p * prob
                outcome_mass[reading] = outcome_mass.get(reading, 0.0) + mass
                split.setdefault(reading, {})[(s0, label)] = mass
        record_entropy += branch.weight * entropy_bits(outcome_mass.values())
        for reading, joint in split.items():
            mass = outcome_mass[reading]
            if mass <= 0.0:
                continue
            emitted.append(
                Branch(
                    weight=branch.weight * mass,
                    joint={key: value / mass for key, value in joint.items()},
                )
            )

    emitted = merge_branches(emitted)

    contracted: list[Branch] = []
    for branch in emitted:
        g_known = branch.g_known()
        l_known = branch.l_known()
        joint: Joint = {}
        for (s0, label), p in branch.joint.items():
            for new_label, prob in contraction(
                label, rate, policy.gated, policy.merge_all, g_known, l_known
            ):
                if prob <= 0.0:
                    continue
                key = (s0, new_label)
                joint[key] = joint.get(key, 0.0) + p * prob
        contracted.append(Branch(weight=branch.weight, joint=joint))

    return merge_branches(contracted), capacity, record_entropy


def run_policy(policy: Policy, steps: int = STEPS) -> list[LedgerRow]:
    branches = [initial_branch()]
    stats = measure(branches)
    rows: list[LedgerRow] = [
        LedgerRow(
            policy=policy.name,
            step=0,
            total_bits=stats["total"],
            exported_bits=stats["exported"],
            retained_bits=stats["retained"],
            contraction_bits=0.0,
            sorted_bits=0.0,
            destroyed_bits=0.0,
            step_efficiency=float("nan"),
            cumulative_efficiency=float("nan"),
            capacity_bits=0.0,
            record_entropy_bits=0.0,
            sector_exported_bits=stats["sector"],
            protected_leakage_bits=stats["leakage"],
            bandwidth_slack_bits=float("nan"),
        )
    ]

    cumulative_sorted = 0.0
    cumulative_contraction = 0.0

    for step in range(steps):
        previous = stats
        branches, capacity, record_entropy = advance(branches, policy, step)
        stats = measure(branches)

        gamma = clamp(previous["retained"] - stats["retained"])
        sigma = clamp(stats["exported"] - previous["exported"])
        delta = clamp(previous["total"] - stats["total"])
        cumulative_sorted += sigma
        cumulative_contraction += gamma

        rows.append(
            LedgerRow(
                policy=policy.name,
                step=step + 1,
                total_bits=stats["total"],
                exported_bits=stats["exported"],
                retained_bits=stats["retained"],
                contraction_bits=gamma,
                sorted_bits=sigma,
                destroyed_bits=delta,
                step_efficiency=(sigma / gamma) if gamma > 1e-12 else float("nan"),
                cumulative_efficiency=(
                    cumulative_sorted / cumulative_contraction
                    if cumulative_contraction > 1e-12
                    else float("nan")
                ),
                capacity_bits=capacity,
                record_entropy_bits=record_entropy,
                sector_exported_bits=stats["sector"],
                protected_leakage_bits=stats["leakage"],
                bandwidth_slack_bits=clamp(delta - max(0.0, gamma - capacity)),
            )
        )

    return rows


# --------------------------------------------------------------------------
# consistency checks
# --------------------------------------------------------------------------


def check_ledger(rows: Sequence[LedgerRow]) -> dict[str, float]:
    identity = 0.0
    monotone_total = 0.0
    monotone_export = 0.0
    record_bound = 0.0
    bandwidth_violation = 0.0
    limited_steps = 0
    for row in rows[1:]:
        identity = max(identity, abs(row.contraction_bits - row.sorted_bits - row.destroyed_bits))
        monotone_total = max(monotone_total, -row.destroyed_bits)
        monotone_export = max(monotone_export, -row.sorted_bits)
        record_bound = max(record_bound, row.sorted_bits - row.contraction_bits)
        bandwidth_violation = min(bandwidth_violation, row.bandwidth_slack_bits)
        if row.contraction_bits > row.capacity_bits:
            limited_steps += 1
    return {
        "max_identity_residual": identity,
        "max_total_increase": monotone_total,
        "max_export_decrease": monotone_export,
        "max_record_without_contraction": record_bound,
        "max_bandwidth_violation": bandwidth_violation,
        "bandwidth_limited_steps": float(limited_steps),
    }


# --------------------------------------------------------------------------
# throughput scan
# --------------------------------------------------------------------------


def scan_rows() -> list[dict[str, object]]:
    resolutions = [
        ("flag", trivial_partition()),
        ("sector", sector_partition()),
        ("microstate", singleton_partition()),
    ]
    rates = [round(0.05 + 0.1125 * i, 4) for i in range(9)]
    emits = list(SCAN_EMITS)

    rows: list[dict[str, object]] = []
    for label, partition in resolutions:
        for emit in emits:
            for rate in rates:
                policy = Policy(
                    name=f"{label}|emit={emit}|rate={rate}",
                    partition_at=lambda _k, p=partition: p,
                    emit_at=lambda _k, e=emit: e,
                    gated=False,
                    rate_at=constant_rate(rate),
                    note="scan",
                )
                ledger = run_policy(policy)
                final = ledger[-1]
                contraction_total = clamp(sum(r.contraction_bits for r in ledger[1:]))
                sorted_total = clamp(sum(r.sorted_bits for r in ledger[1:]))
                destroyed_total = clamp(sum(r.destroyed_bits for r in ledger[1:]))
                rows.append(
                    {
                        "resolution": label,
                        "slots": len(partition),
                        "capacity_bits": round(math.log2(len(partition) + 1), 6),
                        "emit_prob": emit,
                        "contraction_rate": rate,
                        "contraction_total_bits": round(contraction_total, 6),
                        "sorted_total_bits": round(sorted_total, 6),
                        "destroyed_total_bits": round(destroyed_total, 6),
                        "sorting_efficiency": (
                            round(sorted_total / contraction_total, 6)
                            if contraction_total > 1e-12
                            else ""
                        ),
                        "final_exported_bits": round(final.exported_bits, 6),
                        "final_retained_bits": round(final.retained_bits, 6),
                    }
                )
    return rows


# --------------------------------------------------------------------------
# output
# --------------------------------------------------------------------------


def write_ledger(all_rows: Sequence[LedgerRow]) -> None:
    with LEDGER_CSV.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "policy",
                "step",
                "total_bits",
                "exported_bits",
                "retained_bits",
                "contraction_bits",
                "sorted_bits",
                "destroyed_bits",
                "step_efficiency",
                "cumulative_efficiency",
                "capacity_bits",
                "record_entropy_bits",
                "sector_exported_bits",
                "protected_leakage_bits",
                "bandwidth_slack_bits",
            ]
        )
        for row in all_rows:
            writer.writerow(
                [
                    row.policy,
                    row.step,
                    f"{clamp(row.total_bits, 1e-9):.6f}",
                    f"{clamp(row.exported_bits, 1e-9):.6f}",
                    f"{clamp(row.retained_bits, 1e-9):.6f}",
                    f"{clamp(row.contraction_bits, 1e-9):.6f}",
                    f"{clamp(row.sorted_bits, 1e-9):.6f}",
                    f"{clamp(row.destroyed_bits, 1e-9):.6f}",
                    "" if row.step_efficiency != row.step_efficiency else f"{row.step_efficiency:.6f}",
                    ""
                    if row.cumulative_efficiency != row.cumulative_efficiency
                    else f"{row.cumulative_efficiency:.6f}",
                    f"{row.capacity_bits:.6f}",
                    f"{clamp(row.record_entropy_bits, 1e-9):.6f}",
                    f"{clamp(row.sector_exported_bits, 1e-9):.6f}",
                    f"{clamp(row.protected_leakage_bits, 1e-9):.6f}",
                    ""
                    if row.bandwidth_slack_bits != row.bandwidth_slack_bits
                    else f"{row.bandwidth_slack_bits:.6f}",
                ]
            )


def verdict(rows: Sequence[LedgerRow], early_leakage: float, limited_steps: int) -> str:
    final = rows[-1]
    contraction_total = sum(r.contraction_bits for r in rows[1:])
    sorted_total = sum(r.sorted_bits for r in rows[1:])
    chi = sorted_total / contraction_total if contraction_total > 1e-12 else float("nan")
    if chi == chi and chi < 0.99:
        if limited_steps > 0:
            return "destructive: contraction outran the record capacity"
        return "destructive: contraction annihilates unexported distinctions"
    if early_leakage > 0.05:
        return "lossless but centralizing: protected label read before release scale"
    if final.retained_bits > 0.01:
        return "lossless but incomplete: permanent unexported backlog"
    return "admissible sorting: lossless, sector-first, fully released"


def summarize(results: dict[str, list[LedgerRow]]) -> list[dict]:
    summary = []
    for name, rows in results.items():
        contraction_total = clamp(sum(r.contraction_bits for r in rows[1:]))
        sorted_total = clamp(sum(r.sorted_bits for r in rows[1:]))
        destroyed_total = clamp(sum(r.destroyed_bits for r in rows[1:]))
        early = max(r.protected_leakage_bits for r in rows[: SWITCH_STEP + 1])
        checks = check_ledger(rows)
        summary.append(
            {
                "policy": name,
                "contraction_total_bits": round(contraction_total, 6),
                "sorted_total_bits": round(sorted_total, 6),
                "destroyed_total_bits": round(destroyed_total, 6),
                "sorting_efficiency": (
                    round(sorted_total / contraction_total, 6)
                    if contraction_total > 1e-12
                    else ""
                ),
                "final_exported_bits": round(clamp(rows[-1].exported_bits), 6),
                "final_retained_bits": round(clamp(rows[-1].retained_bits, 1e-9), 6),
                "final_sector_exported_bits": round(clamp(rows[-1].sector_exported_bits), 6),
                "max_early_protected_leakage_bits": round(clamp(early, 1e-9), 6),
                "final_protected_leakage_bits": round(
                    clamp(rows[-1].protected_leakage_bits, 1e-9), 6
                ),
                "max_identity_residual": f"{checks['max_identity_residual']:.3e}",
                "max_bandwidth_violation_bits": f"{checks['max_bandwidth_violation']:.3e}",
                "bandwidth_limited_steps": int(checks["bandwidth_limited_steps"]),
                "verdict": verdict(rows, early, int(checks["bandwidth_limited_steps"])),
            }
        )
    return summary


def write_rows(path: Path, rows: Sequence[dict]) -> None:
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


# --------------------------------------------------------------------------
# hand-written SVG (no plotting dependency)
# --------------------------------------------------------------------------


PALETTE = ["#1b6ca8", "#c44536", "#2a9d8f", "#8f5fbf", "#c98a1b"]


def _axes(
    width: int,
    height: int,
    pad_left: int,
    pad_bottom: int,
    title: str,
    x_label: str,
    y_label: str,
    x_ticks: Sequence[tuple[float, str]],
    y_ticks: Sequence[tuple[float, str]],
    to_px: Callable[[float, float], tuple[float, float]],
) -> list[str]:
    parts = [
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
        f'<text x="{width / 2:.1f}" y="26" font-family="Helvetica,Arial" font-size="16" '
        f'text-anchor="middle" fill="#111111">{title}</text>',
    ]
    for value, text in x_ticks:
        px, _ = to_px(value, 0.0)
        parts.append(
            f'<line x1="{px:.1f}" y1="{height - pad_bottom}" x2="{px:.1f}" '
            f'y2="{height - pad_bottom + 5}" stroke="#666666" stroke-width="1"/>'
        )
        parts.append(
            f'<text x="{px:.1f}" y="{height - pad_bottom + 20}" font-family="Helvetica,Arial" '
            f'font-size="11" text-anchor="middle" fill="#333333">{text}</text>'
        )
    for value, text in y_ticks:
        _, py = to_px(0.0, value)
        parts.append(
            f'<line x1="{pad_left - 5}" y1="{py:.1f}" x2="{pad_left}" y2="{py:.1f}" '
            f'stroke="#666666" stroke-width="1"/>'
        )
        parts.append(
            f'<text x="{pad_left - 9}" y="{py + 4:.1f}" font-family="Helvetica,Arial" '
            f'font-size="11" text-anchor="end" fill="#333333">{text}</text>'
        )
        parts.append(
            f'<line x1="{pad_left}" y1="{py:.1f}" x2="{width - 210}" y2="{py:.1f}" '
            f'stroke="#e6e6e6" stroke-width="1"/>'
        )
    parts.append(
        f'<line x1="{pad_left}" y1="{height - pad_bottom}" x2="{width - 210}" '
        f'y2="{height - pad_bottom}" stroke="#333333" stroke-width="1.2"/>'
    )
    parts.append(
        f'<line x1="{pad_left}" y1="40" x2="{pad_left}" y2="{height - pad_bottom}" '
        f'stroke="#333333" stroke-width="1.2"/>'
    )
    parts.append(
        f'<text x="{(width - 210 + pad_left) / 2:.1f}" y="{height - 8}" '
        f'font-family="Helvetica,Arial" font-size="12" text-anchor="middle" '
        f'fill="#333333">{x_label}</text>'
    )
    parts.append(
        f'<text x="16" y="{height / 2:.1f}" font-family="Helvetica,Arial" font-size="12" '
        f'text-anchor="middle" fill="#333333" '
        f'transform="rotate(-90 16 {height / 2:.1f})">{y_label}</text>'
    )
    return parts


def plot_ledger(results: dict[str, list[LedgerRow]]) -> None:
    width, height = 900, 480
    pad_left, pad_bottom = 62, 46
    x_max, y_max = STEPS, H_S0

    def to_px(x: float, y: float) -> tuple[float, float]:
        px = pad_left + (x / x_max) * (width - 210 - pad_left)
        py = (height - pad_bottom) - (y / y_max) * (height - pad_bottom - 40)
        return px, py

    parts = _axes(
        width,
        height,
        pad_left,
        pad_bottom,
        "Distinguishability ledger: exported (solid) vs retained backlog (dashed)",
        "step",
        "bits about the initial interior microstate",
        [(t, str(t)) for t in range(0, STEPS + 1, 2)],
        [(v, f"{v:.1f}") for v in (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0)],
        to_px,
    )

    for index, (name, rows) in enumerate(results.items()):
        color = PALETTE[index % len(PALETTE)]
        exported = " ".join(
            "{:.1f},{:.1f}".format(*to_px(row.step, row.exported_bits)) for row in rows
        )
        retained = " ".join(
            "{:.1f},{:.1f}".format(*to_px(row.step, row.retained_bits)) for row in rows
        )
        parts.append(
            f'<polyline points="{exported}" fill="none" stroke="{color}" stroke-width="2.2"/>'
        )
        parts.append(
            f'<polyline points="{retained}" fill="none" stroke="{color}" stroke-width="1.6" '
            f'stroke-dasharray="5 4" opacity="0.75"/>'
        )
        legend_y = 58 + index * 20
        parts.append(
            f'<line x1="{width - 200}" y1="{legend_y}" x2="{width - 176}" y2="{legend_y}" '
            f'stroke="{color}" stroke-width="2.2"/>'
        )
        parts.append(
            f'<text x="{width - 170}" y="{legend_y + 4}" font-family="Helvetica,Arial" '
            f'font-size="11" fill="#222222">{name}</text>'
        )

    parts.append(
        f'<line x1="{to_px(0, H_S0)[0]:.1f}" y1="{to_px(0, H_S0)[1]:.1f}" '
        f'x2="{to_px(STEPS, H_S0)[0]:.1f}" y2="{to_px(STEPS, H_S0)[1]:.1f}" '
        f'stroke="#999999" stroke-width="1" stroke-dasharray="2 3"/>'
    )
    parts.append(
        f'<text x="{to_px(0.3, H_S0)[0]:.1f}" y="{to_px(0, H_S0)[1] - 6:.1f}" '
        f'font-family="Helvetica,Arial" font-size="10" fill="#666666">'
        f'H(S0) = {H_S0:.3f} bits</text>'
    )

    body = "\n".join(parts)
    LEDGER_SVG.write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">\n{body}\n</svg>\n'
    )


def plot_frontier(rows: Sequence[dict[str, object]]) -> None:
    width, height = 900, 460
    pad_left, pad_bottom = 62, 46

    def to_px(x: float, y: float) -> tuple[float, float]:
        px = pad_left + x * (width - 210 - pad_left)
        py = (height - pad_bottom) - y * (height - pad_bottom - 40)
        return px, py

    parts = _axes(
        width,
        height,
        pad_left,
        pad_bottom,
        "Throughput frontier: sorting efficiency falls as contraction outruns export",
        "contraction rate per step",
        "sorting efficiency  chi = sorted / contracted",
        [(v, f"{v:.1f}") for v in (0.0, 0.2, 0.4, 0.6, 0.8, 1.0)],
        [(v, f"{v:.1f}") for v in (0.0, 0.2, 0.4, 0.6, 0.8, 1.0)],
        to_px,
    )

    series: dict[tuple[str, float], list[tuple[float, float]]] = {}
    for row in rows:
        if row["sorting_efficiency"] == "":
            continue
        key = (str(row["resolution"]), float(row["emit_prob"]))
        series.setdefault(key, []).append(
            (float(row["contraction_rate"]), float(row["sorting_efficiency"]))
        )

    shown = [
        ("microstate", 1.0),
        ("microstate", 0.4),
        ("sector", 1.0),
        ("sector", 0.4),
        ("flag", 1.0),
    ]
    for index, key in enumerate(shown):
        points = sorted(series.get(key, []))
        if not points:
            continue
        color = PALETTE[index % len(PALETTE)]
        path = " ".join("{:.1f},{:.1f}".format(*to_px(x, y)) for x, y in points)
        parts.append(
            f'<polyline points="{path}" fill="none" stroke="{color}" stroke-width="2.2"/>'
        )
        legend_y = 58 + index * 20
        parts.append(
            f'<line x1="{width - 200}" y1="{legend_y}" x2="{width - 176}" y2="{legend_y}" '
            f'stroke="{color}" stroke-width="2.2"/>'
        )
        parts.append(
            f'<text x="{width - 170}" y="{legend_y + 4}" font-family="Helvetica,Arial" '
            f'font-size="11" fill="#222222">{key[0]} slots, emit={key[1]}</text>'
        )

    body = "\n".join(parts)
    FRONTIER_SVG.write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">\n{body}\n</svg>\n'
    )


# --------------------------------------------------------------------------


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    policy_list = policies()
    results = {policy.name: run_policy(policy) for policy in policy_list}

    all_rows: list[LedgerRow] = []
    for rows in results.values():
        all_rows.extend(rows)

    write_ledger(all_rows)
    summary = summarize(results)
    write_rows(SUMMARY_CSV, summary)

    scan = scan_rows()
    write_rows(SCAN_CSV, scan)

    plot_ledger(results)
    plot_frontier(scan)

    print(f"H(S0) = {H_S0:.6f} bits over {len(MICROSTATES)} interior microstates")
    print(f"wrote {LEDGER_CSV}")
    print(f"wrote {SUMMARY_CSV}")
    print(f"wrote {SCAN_CSV}")
    print()
    for row in summary:
        print(
            f"{row['policy']}: "
            f"contracted={row['contraction_total_bits']}, "
            f"sorted={row['sorted_total_bits']}, "
            f"destroyed={row['destroyed_total_bits']}, "
            f"chi={row['sorting_efficiency']}, "
            f"final_export={row['final_exported_bits']}, "
            f"backlog={row['final_retained_bits']}, "
            f"early_leak={row['max_early_protected_leakage_bits']}"
        )
        print(f"    {row['verdict']}")

    print()
    for name, rows in results.items():
        checks = check_ledger(rows)
        print(
            f"{name}: identity residual {checks['max_identity_residual']:.2e}, "
            f"max sigma-gamma excess {checks['max_record_without_contraction']:.2e}, "
            f"bandwidth violation {checks['max_bandwidth_violation']:.2e} "
            f"over {int(checks['bandwidth_limited_steps'])} bandwidth-limited steps"
        )


if __name__ == "__main__":
    main()
