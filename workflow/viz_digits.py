import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

data = pd.read_csv('../data/digits-data.csv')

# Extract data
pixel_values = data.iloc[:,:-1].values
pixels = data.columns.tolist()
pixels.pop()

tSNE = TSNE(n_jobs=2,random_state=0)
