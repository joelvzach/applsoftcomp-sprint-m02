"""Visualize 1d-data.csv: strip plot + box plot on log scale."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("data/1d-data.csv")

fig, ax = plt.subplots(figsize=(5, 5))

# Box plot without outlier markers (we'll show all points via strip)
sns.boxplot(
    data=df,
    x="group",
    y="value",
    order=["control", "cases"],
    width=0.4,
    color="white",
    linecolor="black",
    flierprops=dict(marker="none"),
    ax=ax,
)
# Strip plot to show individual data points
sns.stripplot(
    data=df,
    x="group",
    y="value",
    hue="group",
    order=["control", "cases"],
    hue_order=["control", "cases"],
    jitter=True,
    size=7,
    palette={"control": "#4C72B0", "cases": "#DD8452"},
    legend=False,
    ax=ax,
)

ax.set_yscale("log")
ax.set_xlabel("Group", fontsize=13)
ax.set_ylabel("Value (log scale)", fontsize=13)
ax.set_title("Treatment Effect by Group (n=10 per group)", fontsize=13)
ax.set_xticks([0, 1])
ax.set_xticklabels(["Control", "Cases"], fontsize=12)

plt.tight_layout()
plt.savefig("paper/figs/1d-data.png", dpi=150)
print("Saved paper/figs/1d-data.png")
