import pandas as pd
import numpy as np

# ── 1. Load ────────────────────────────────────────────────────────────────────
df = pd.read_csv("data/1d-data.csv")
print("── Raw Data ──")
print(df.head(10))
print(f"\nShape     : {df.shape}")
print(f"Columns   : {df.columns.tolist()}")
print(f"Dtypes    :\n{df.dtypes}")

# ── 2. Check for missing values ────────────────────────────────────────────────
print("\n── Missing Values ──")
print(df.isnull().sum())

# ── 3. Basic statistics ────────────────────────────────────────────────────────
print("\n── Descriptive Statistics (raw) ──")
print(df.describe())

# ── 4. Separate groups ────────────────────────────────────────────────────────
control = df[df["group"] == "control"]["value"]
case    = df[df["group"] == "case"]["value"]

print(f"\n── Group Counts ──")
print(df["group"].value_counts())

print(f"\n── Control Stats ──")
print(control.describe())

print(f"\n── Case Stats ──")
print(case.describe())

# ── 5. Check value range → motivates log transform ────────────────────────────
print("\n── Value Range ──")
print(f"Min  : {df['value'].min():.4f}")
print(f"Max  : {df['value'].max():.4f}")
print(f"Range spans ~{df['value'].max() / df['value'].min():.0f}x → log transform needed")

# ── 6. Apply log10 transform ──────────────────────────────────────────────────
df["log10_value"] = np.log10(df["value"])

print("\n── Log10 Transformed Stats ──")
print(df.groupby("group")["log10_value"].describe())

# ── 7. Save formatted data ────────────────────────────────────────────────────
df.to_csv("data/1d-data-formatted.csv", index=False)
print("\n── Saved → data/1d-data-formatted.csv ──")
print(df.head(10))