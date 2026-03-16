import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# load the formatted data (has log10 column already)
df = pd.read_csv("data/1d-data-formatted.csv")
print("Loaded formatted data:")
print(df.head(10))

# split into groups
control = df[df["group"] == "control"]["value"]
case    = df[df["group"] == "case"]["value"]

# jitter x positions so points don't overlap
np.random.seed(42)
x_control = np.random.uniform(0.75, 1.25, size=len(control))
x_case     = np.random.uniform(1.75, 2.25, size=len(case))

fig, ax = plt.subplots(figsize=(6, 7))

# box plot as background summary, hide outlier markers since we plot points manually
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

# color each box differently so groups are easy to tell apart
bp["boxes"][0].set_facecolor("#A8D5BA")  # control - green
bp["boxes"][1].set_facecolor("#F4A9A8")  # case - red

# overlay individual points as a strip plot
ax.scatter(x_control, control, color="#2E8B57", alpha=0.8,
           edgecolors="white", s=60, zorder=3, label="control")
ax.scatter(x_case,    case,    color="#C0392B", alpha=0.8,
           edgecolors="white", s=60, zorder=3, label="case")

# log scale because values span ~4 orders of magnitude
ax.set_yscale("log")
ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)

# labels and title
ax.set_xticks([1, 2])
ax.set_xticklabels(["Control", "Case"], fontsize=12)
ax.set_xlabel("Group", fontsize=13)
ax.set_ylabel("Value (log scale)", fontsize=13)
ax.set_title("1D Data: Control vs Case\n(strip plot + box plot, log scale)",
             fontsize=13, fontweight="bold")

# show sample size under each group
ax.text(1, ax.get_ylim()[0], f"n={len(control)}",
        ha="center", va="bottom", fontsize=10, color="#2E8B57")
ax.text(2, ax.get_ylim()[0], f"n={len(case)}",
        ha="center", va="bottom", fontsize=10, color="#C0392B")

ax.legend(title="Group", fontsize=10, title_fontsize=10, loc="upper right")
ax.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()

# save figure
plt.savefig("figs/fig-1d-data.png", dpi=150, bbox_inches="tight")
print("\nSaved -> figs/fig-1d-data.png")
plt.show()