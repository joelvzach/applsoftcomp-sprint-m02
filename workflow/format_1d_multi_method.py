"""Load and format 1d-multi-method-data.csv: sort methods by mean AUC-ROC."""

import pandas as pd

df = pd.read_csv("data/1d-multi-method-data.csv")

print("Shape:", df.shape)
print("Methods:", sorted(df["method"].unique()))
print("Missing values:", df.isnull().sum().sum())

# Compute mean AUC-ROC per method and derive sort order
method_means = df.groupby("method")["AUCROC"].mean().sort_values(ascending=False)
print("\nMethods ranked by mean AUC-ROC:")
print(method_means.to_string())

# Add sort-order column for use in visualization
method_order = method_means.index.tolist()
df["rank"] = df["method"].map({m: i for i, m in enumerate(method_order)})

print("\nSort order (best to worst):", method_order)
print("\nData ready — no cleaning needed, sorting order derived.")
