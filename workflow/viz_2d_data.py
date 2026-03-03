import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/2d-data.csv")

fig, ax = plt.subplots(figsize=(6, 5))

hb = ax.hexbin(df["x"], df["y"], gridsize=45, mincnt=1)
ax.scatter(df["x"], df["y"], s=2, alpha=0.08)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("2D data density")

cbar = fig.colorbar(hb, ax=ax)
cbar.set_label("count")

fig.tight_layout()
fig.savefig("figs/fig-2d-data.png", dpi=300)
