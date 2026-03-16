import pandas as pd
import numpy as np

# load the raw data
df = pd.read_csv("data/1d-data.csv")
print("Raw data:")
print(df.head(10))
print(f"\nShape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Dtypes:\n{df.dtypes}")

# check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# quick summary stats on raw values
print("\nDescriptive stats:")
print(df.describe())

# split by group for separate inspection
control = df[df["group"] == "control"]["value"]
case    = df[df["group"] == "case"]["value"]

print("\nGroup counts:")
print(df["group"].value_counts())

print("\nControl stats:")
print(control.describe())

print("\nCase stats:")
print(case.describe())

# values span several orders of magnitude, so log scale makes sense for viz
print("\nValue range:")
print(f"Min: {df['value'].min():.4f}")
print(f"Max: {df['value'].max():.4f}")
print(f"Range spans ~{df['value'].max() / df['value'].min():.0f}x -> log transform needed")

# add log10 column for use in visualization
df["log10_value"] = np.log10(df["value"])

print("\nLog10 stats by group:")
print(df.groupby("group")["log10_value"].describe())

# save formatted data with the new log10 column
df.to_csv("data/1d-data-formatted.csv", index=False)
print("\nSaved -> data/1d-data-formatted.csv")
print(df.head(10))