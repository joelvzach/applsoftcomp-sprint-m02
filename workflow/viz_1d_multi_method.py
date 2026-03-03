"""Visualize 1d-multi-method-data.csv: highlight Proposed with preattentive encoding."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

df = pd.read_csv("data/1d-multi-method-data.csv")

# Sort methods by mean AUC-ROC (descending)
method_means = df.groupby("method")["AUCROC"].mean().sort_values(ascending=False)
method_order = method_means.index.tolist()

fig, ax = plt.subplots(figsize=(8, 5))

# Preattentive encoding: color and size differentiate Proposed from baselines
PROPOSED_COLOR = "#E84B30"   # vivid red-orange
BASELINE_COLOR = "#AAAAAA"   # neutral gray

for i, method in enumerate(method_order):
    vals = df[df["method"] == method]["AUCROC"].values
    is_proposed = method == "Proposed"

    color = PROPOSED_COLOR if is_proposed else BASELINE_COLOR
    size = 70 if is_proposed else 30
    zorder = 3 if is_proposed else 2
    alpha = 1.0 if is_proposed else 0.7

    # Jitter x positions slightly
    jitter = np.random.default_rng(i).uniform(-0.18, 0.18, size=len(vals))
    ax.scatter(
        np.full(len(vals), i) + jitter,
        vals,
        color=color,
        s=size,
        alpha=alpha,
        zorder=zorder,
        edgecolors="white" if is_proposed else "none",
        linewidths=0.5,
    )
    # Mean marker
    ax.scatter(
        i,
        vals.mean(),
        color=color,
        s=120 if is_proposed else 60,
        marker="D",
        zorder=4,
        edgecolors="black",
        linewidths=0.8,
    )

ax.set_xticks(range(len(method_order)))
ax.set_xticklabels(
    [m.replace("_", " ") for m in method_order],
    rotation=35,
    ha="right",
    fontsize=10,
)
ax.set_xlabel("Method (sorted by mean AUC-ROC)", fontsize=12)
ax.set_ylabel("AUC-ROC", fontsize=12)
ax.set_title("AUC-ROC by Method: Proposed vs Baselines", fontsize=13)
ax.set_ylim(0, 1.05)
ax.axhline(0.5, color="black", linewidth=0.8, linestyle="--", alpha=0.4, label="Chance (0.5)")

# Legend
proposed_patch = mpatches.Patch(color=PROPOSED_COLOR, label="Proposed")
baseline_patch = mpatches.Patch(color=BASELINE_COLOR, label="Baselines")
ax.legend(handles=[proposed_patch, baseline_patch], fontsize=10, loc="upper right")

plt.tight_layout()
plt.savefig("paper/figs/1d-multi-method-data.png", dpi=150)
print("Saved paper/figs/1d-multi-method-data.png")
