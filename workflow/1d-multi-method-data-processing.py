import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv("../data/1d-multi-method-data.csv")

# Ensure Proposed appears first
methods = ["Proposed"] + sorted(
    [m for m in df["method"].unique() if m != "Proposed"]
)

# Group data
grouped_data = [df[df["method"] == m]["AUCROC"].values for m in methods]

# Create figure
plt.figure(figsize=(10, 6))

box = plt.boxplot(
    grouped_data,
    patch_artist=True,
    widths=0.6,
    showfliers=True
)

# Apply styling
for i, (patch, method) in enumerate(zip(box["boxes"], methods)):
    if method == "Proposed":
        patch.set_facecolor("#1f77b4")  # strong blue
        patch.set_edgecolor("black")
        patch.set_linewidth(2.5)
    else:
        patch.set_facecolor("#d3d3d3")  # light gray
        patch.set_edgecolor("gray")
        patch.set_linewidth(1)

# Style medians
for median, method in zip(box["medians"], methods):
    if method == "Proposed":
        median.set_color("black")
        median.set_linewidth(2)
    else:
        median.set_color("gray")

# Axis formatting
plt.xticks(range(1, len(methods) + 1), methods, rotation=45)
plt.ylabel("AUC-ROC")
plt.xlabel("Method")
plt.ylim(0, 1)
plt.title("Comparison of AUC-ROC Across Methods")

# Bold the Proposed tick label
xtick_labels = plt.gca().get_xticklabels()
xtick_labels[0].set_fontweight("bold")

plt.tight_layout()

plt.savefig("../figs/1d-multi-method.png", dpi=300, bbox_inches="tight")

plt.show()