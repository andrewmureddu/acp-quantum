#!/usr/bin/env python3
"""Toy ACP simulation for a monitored qubit.

The model scans a system-environment coupling strength g. The qubit evolves
under three simple effects:

1. Hamiltonian rotation around x, which keeps internal futures open.
2. Pointer-basis dephasing along z, which creates environmental records.
3. Thermal relaxation toward the maximally mixed state, which erases memory.

This is not a microscopic derivation. It is a small diagnostic instrument for
the quantum ACP idea: productive dynamics should require both retained memory
and exported record, while avoiding total thermal erasure.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
CSV_PATH = OUT / "monitored_qubit_scan.csv"
SVG_PATH = OUT / "monitored_qubit_scan.svg"


DT = 0.04
HORIZON = 4.0
OMEGA = 1.0
G_MAX = 4.0
G_STEPS = 121


INITIAL_STATES = [
    (1.0, 0.0, 0.0),
    (-1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, -1.0, 0.0),
    (0.0, 0.0, 1.0),
    (0.0, 0.0, -1.0),
]

ANTIPODAL_PAIRS = [(0, 1), (2, 3), (4, 5)]


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def binary_entropy(p: float) -> float:
    p = clamp(p, 1e-12, 1.0 - 1e-12)
    return -(p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p))


def qubit_entropy(r: tuple[float, float, float]) -> float:
    radius = min(1.0, math.sqrt(sum(v * v for v in r)))
    return binary_entropy((1.0 + radius) / 2.0)


def rates(g: float) -> tuple[float, float]:
    """Return dephasing and thermal relaxation rates.

    Dephasing grows approximately linearly with coupling. Thermal relaxation is
    negligible at tiny coupling and becomes important under strong monitoring.
    """

    gamma_phi = g
    gamma_thermal = 0.28 * g * g / (1.0 + g * g)
    return gamma_phi, gamma_thermal


def step_bloch(
    r: tuple[float, float, float], gamma_phi: float, gamma_thermal: float
) -> tuple[float, float, float]:
    x, y, z = r

    # Hamiltonian rotation around x.
    theta = OMEGA * DT
    c = math.cos(theta)
    s = math.sin(theta)
    y, z = y * c - z * s, y * s + z * c

    # Pointer-basis dephasing suppresses x/y coherence but leaves z populations.
    dephase = math.exp(-gamma_phi * DT)
    x *= dephase
    y *= dephase

    # Thermal relaxation pulls the full Bloch vector toward the mixed state.
    relax = math.exp(-gamma_thermal * DT)
    x *= math.sqrt(relax)
    y *= math.sqrt(relax)
    z *= relax

    return x, y, z


def evolve(
    r0: tuple[float, float, float], gamma_phi: float, gamma_thermal: float
) -> tuple[float, float, float]:
    r = r0
    for _ in range(int(HORIZON / DT)):
        r = step_bloch(r, gamma_phi, gamma_thermal)
    return r


def trace_distance(
    a: tuple[float, float, float], b: tuple[float, float, float]
) -> float:
    # For qubits, trace distance is half the Euclidean distance of Bloch vectors.
    return 0.5 * math.sqrt(sum((ai - bi) ** 2 for ai, bi in zip(a, b)))


def classify(record: float, memory: float, mixedness: float) -> str:
    if record < 0.08:
        return "crystallized"
    if memory < 0.08 or mixedness > 0.92:
        return "dissolved"
    return "productive"


def scan() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []

    for i in range(G_STEPS):
        g = G_MAX * i / (G_STEPS - 1)
        gamma_phi, gamma_thermal = rates(g)
        finals = [evolve(r, gamma_phi, gamma_thermal) for r in INITIAL_STATES]

        memory = sum(trace_distance(finals[a], finals[b]) for a, b in ANTIPODAL_PAIRS)
        memory /= len(ANTIPODAL_PAIRS)

        coherence = sum(math.hypot(r[0], r[1]) for r in finals) / len(finals)
        mixedness = sum(qubit_entropy(r) for r in finals) / len(finals)

        raw_record = 1.0 - math.exp(-gamma_phi * HORIZON)
        record_survival = math.exp(-0.55 * gamma_thermal * HORIZON)
        record = raw_record * record_survival

        classical_score = memory * record * (1.0 - 0.5 * mixedness)
        quantum_score = classical_score * coherence

        rows.append(
            {
                "g": g,
                "gamma_phi": gamma_phi,
                "gamma_thermal": gamma_thermal,
                "memory": memory,
                "record": record,
                "coherence": coherence,
                "mixedness": mixedness,
                "classical_score": classical_score,
                "quantum_score": quantum_score,
                "regime": classify(record, memory, mixedness),
            }
        )

    return rows


def write_csv(rows: list[dict[str, float | str]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def line_path(
    rows: list[dict[str, float | str]],
    key: str,
    x0: int,
    y0: int,
    width: int,
    height: int,
) -> str:
    pts = []
    for row in rows:
        x = x0 + width * float(row["g"]) / G_MAX
        y = y0 + height * (1.0 - clamp(float(row[key])))
        pts.append(f"{x:.1f},{y:.1f}")
    return " ".join(pts)


def write_svg(rows: list[dict[str, float | str]]) -> None:
    x0, y0, width, height = 70, 40, 780, 420
    colors = {
        "memory": "#2364aa",
        "record": "#f15a24",
        "coherence": "#2e7d32",
        "mixedness": "#7b2cbf",
        "classical_score": "#111111",
        "quantum_score": "#d00000",
    }

    best_classical = max(rows, key=lambda r: float(r["classical_score"]))
    best_quantum = max(rows, key=lambda r: float(r["quantum_score"]))

    productive = [r for r in rows if r["regime"] == "productive"]
    if productive:
        g_lo = min(float(r["g"]) for r in productive)
        g_hi = max(float(r["g"]) for r in productive)
    else:
        g_lo = g_hi = 0.0

    def sx(g: float) -> float:
        return x0 + width * g / G_MAX

    shaded_x = sx(g_lo)
    shaded_w = max(0.0, sx(g_hi) - shaded_x)

    legend = []
    for n, (key, color) in enumerate(colors.items()):
        y = y0 + height + 54 + n * 22
        legend.append(
            f'<line x1="660" y1="{y}" x2="710" y2="{y}" stroke="{color}" '
            f'stroke-width="3"/><text x="720" y="{y + 5}" '
            f'font-size="14">{key}</text>'
        )

    lines = []
    for key, color in colors.items():
        lines.append(
            f'<polyline points="{line_path(rows, key, x0, y0, width, height)}" '
            f'fill="none" stroke="{color}" stroke-width="3"/>'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="920" height="650" viewBox="0 0 920 650">
  <rect width="920" height="650" fill="#ffffff"/>
  <text x="70" y="24" font-size="20" font-family="Arial">Monitored qubit ACP scan</text>
  <rect x="{shaded_x:.1f}" y="{y0}" width="{shaded_w:.1f}" height="{height}" fill="#ffe8a3" opacity="0.42"/>
  <line x1="{x0}" y1="{y0 + height}" x2="{x0 + width}" y2="{y0 + height}" stroke="#222"/>
  <line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0 + height}" stroke="#222"/>
  <text x="{x0 + width / 2 - 90}" y="{y0 + height + 36}" font-size="16" font-family="Arial">coupling strength g</text>
  <text x="14" y="{y0 + height / 2}" font-size="16" font-family="Arial" transform="rotate(-90 14,{y0 + height / 2})">normalized metric</text>
  <text x="{sx(float(best_classical["g"])) - 55:.1f}" y="{y0 + 18}" font-size="13" font-family="Arial">best classical g={float(best_classical["g"]):.2f}</text>
  <text x="{sx(float(best_quantum["g"])) - 45:.1f}" y="{y0 + 36}" font-size="13" font-family="Arial">best quantum g={float(best_quantum["g"]):.2f}</text>
  <text x="{shaded_x + 8:.1f}" y="{y0 + height - 12}" font-size="13" font-family="Arial">productive band</text>
  {''.join(lines)}
  <text x="70" y="{y0 + height + 58}" font-size="14" font-family="Arial">Peak classical score: {float(best_classical["classical_score"]):.3f} at g={float(best_classical["g"]):.3f}</text>
  <text x="70" y="{y0 + height + 80}" font-size="14" font-family="Arial">Peak quantum score: {float(best_quantum["quantum_score"]):.3f} at g={float(best_quantum["g"]):.3f}</text>
  <text x="70" y="{y0 + height + 112}" font-size="13" font-family="Arial">Crystallization: record near zero. Dissolution: memory erased or mixedness high.</text>
  {''.join(legend)}
</svg>
"""

    SVG_PATH.write_text(svg)


def main() -> None:
    rows = scan()
    write_csv(rows)
    write_svg(rows)

    best_classical = max(rows, key=lambda r: float(r["classical_score"]))
    best_quantum = max(rows, key=lambda r: float(r["quantum_score"]))
    productive = [r for r in rows if r["regime"] == "productive"]

    print(f"wrote {CSV_PATH}")
    print(f"wrote {SVG_PATH}")
    print(
        "productive band: "
        f"g={float(productive[0]['g']):.3f}..{float(productive[-1]['g']):.3f}"
        if productive
        else "productive band: none"
    )
    print(
        "peak classical score: "
        f"{float(best_classical['classical_score']):.4f} at g={float(best_classical['g']):.3f}"
    )
    print(
        "peak quantum score: "
        f"{float(best_quantum['quantum_score']):.4f} at g={float(best_quantum['g']):.3f}"
    )


if __name__ == "__main__":
    main()
