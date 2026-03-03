"""Load and inspect 1d-data.csv, apply log transformation for visualization."""

import numpy as np
import pandas as pd

df = pd.read_csv("data/1d-data.csv")

# Inspect
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Groups:", df["group"].unique())
print("\nRaw statistics:")
print(df.groupby("group")["value"].describe())

# Log-transform for visualization (natural log)
df["log_value"] = np.log(df["value"])
print("\nLog-transformed statistics:")
print(df.groupby("group")["log_value"].describe())

print("\nData ready for visualization with log scale.")
