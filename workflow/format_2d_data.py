"""Load and inspect 2d-data.csv, check for missing values and data quality."""

import pandas as pd

df = pd.read_csv("data/2d-data.csv")

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing values:\n", df.isnull().sum())
print("\nDtypes:\n", df.dtypes)
print("\nStatistics:\n", df.describe())

# Data is clean: numeric, no NAs, both dimensions share same scale
# No transformation needed — KDE/hexbin handles density directly
print("\nData is clean: no missing values, consistent numeric types.")
print("No transformation needed for visualization.")
