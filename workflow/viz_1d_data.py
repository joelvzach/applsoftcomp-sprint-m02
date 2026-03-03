import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ── 1. Load formatted data ─────────────────────────────────────────────────────
df = pd.read_csv("data/1d-data-formatted.csv")
print("── Loaded formatted data ──")
print(df.head(10))

# ── 2. Separate groups ─────────────────────────────────────────────────────────
control = df[df["group"] == "control"]["value"]
case    = df[df["group"] == "case"]["value"]

# ── 3. Assign x-positions for strip plot ──────────────────────────────────────
np.random.seed(42)
x_control = np.random.uniform(0.75, 1.25, size=len(control))
x_case     = np.random.uniform(1.75, 2.25, size=len(case))

# ── 4. Build figure ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 7))

# ── 5. Box plot (no fliers — points drawn manually in strip plot) ──────────────
bp = ax.boxplot(
    [control, case],
    positions=[1, 2],
    widths=0.35,
    patch_artist=True,
    showfliers=False,
    medianprops=dict(color="black", linewidth=2),
    boxprops=dict(facecolor="lightsteelblue", alpha=0.5),
    whiskerprops=dict(linewidth=1.5),
    capprops=dict(linewidth=1.5),
)

# Different box colours per group
bp["boxes"][0].set_facecolor("#A8D5BA")   # control → green tint
bp["boxes"][1].set_facecolor("#F4A9A8")   # case    → red tint

# ── 6. Strip plot (jittered individual points) ────────────────────────────────
ax.scatter(x_control, control, color="#2E8B57", alpha=0.8,
           edgecolors="white", s=60, zorder=3, label="control")
ax.scatter(x_case,    case,    color="#C0392B", alpha=0.8,
           edgecolors="white", s=60, zorder=3, label="case")

# ── 7. Log scale on y-axis ────────────────────────────────────────────────────
ax.set_yscale("log")
ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)

# ── 8. Labels, ticks, title ───────────────────────────────────────────────────
ax.set_xticks([1, 2])
ax.set_xticklabels(["Control", "Case"], fontsize=12)
ax.set_xlabel("Group", fontsize=13)
ax.set_ylabel("Value (log scale)", fontsize=13)
ax.set_title("1D Data: Control vs Case\n(strip plot + box plot, log scale)",
             fontsize=13, fontweight="bold")

# ── 9. Annotate n per group ───────────────────────────────────────────────────
ax.text(1, ax.get_ylim()[0], f"n={len(control)}",
        ha="center", va="bottom", fontsize=10, color="#2E8B57")
ax.text(2, ax.get_ylim()[0], f"n={len(case)}",
        ha="center", va="bottom", fontsize=10, color="#C0392B")

# ── 10. Legend & layout ───────────────────────────────────────────────────────
ax.legend(title="Group", fontsize=10, title_fontsize=10, loc="upper right")
ax.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()

# ── 11. Save figure ───────────────────────────────────────────────────────────
plt.savefig("figs/fig-1d-data.png", dpi=150, bbox_inches="tight")
print("\n── Saved → figs/fig-1d-data.png ──")
plt.show()