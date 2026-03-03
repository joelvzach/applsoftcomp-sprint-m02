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
