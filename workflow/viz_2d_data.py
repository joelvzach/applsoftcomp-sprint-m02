"""Visualize 2d-data.csv: KDE contour plot with scatter underlay."""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("data/2d-data.csv")

fig, ax = plt.subplots(figsize=(5, 5))

# Scatter underlay with very low alpha to hint at raw density
ax.scatter(df["x"], df["y"], alpha=0.05, s=3, color="steelblue", rasterized=True)

# KDE contour fills on top
sns.kdeplot(
    data=df,
    x="x",
    y="y",
    fill=True,
    cmap="Blues",
    alpha=0.6,
    levels=8,
    ax=ax,
)
# Contour lines for clarity
sns.kdeplot(
    data=df,
    x="x",
    y="y",
    color="navy",
    linewidths=0.8,
    levels=8,
    ax=ax,
)

ax.set_aspect("equal")
ax.set_xlabel("x", fontsize=13)
ax.set_ylabel("y", fontsize=13)
ax.set_title("2D Sample Distribution (n=6,000)", fontsize=13)

plt.tight_layout()
plt.savefig("paper/figs/2d-data.png", dpi=150)
print("Saved paper/figs/2d-data.png")
