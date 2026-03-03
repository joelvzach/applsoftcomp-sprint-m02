# %% Generate UCI ML hand-written digits dataset
# This script loads the digits dataset from scikit-learn and saves it as a CSV.
# The digits dataset contains 8x8 pixel images of handwritten digits (0-9).
# Each row is a flattened 64-dimensional feature vector plus the digit label.

import numpy as np
import pandas as pd
from sklearn.datasets import load_digits

digits = load_digits()
X = digits.data  # (1797, 64) - pixel intensities 0-16
y = digits.target  # (1797,) - digit labels 0-9

# Create column names for the 64 pixel features
pixel_cols = [f"pixel_{i}" for i in range(X.shape[1])]

df = pd.DataFrame(X, columns=pixel_cols)
df["digit"] = y

df.to_csv("digits-data.csv", index=False)
print(f"Saved {len(df)} samples with {X.shape[1]} features and {len(np.unique(y))} classes")
