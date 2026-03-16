import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Extract data

data = pd.read_csv('data/digits-data.csv')

pixel_values = data.iloc[:,:-1].values
digits = data.iloc[:,-1].values

tSNE = TSNE(n_jobs=2,random_state=0)

print('Computing t-SNE...')

x_transformed = tSNE.fit_transform(pixel_values)

plt.figure()
plt.title('2D t-SNE Visualization of ML Written Digit Data')

scatter = plt.scatter(
    x_transformed[:, 0],
    x_transformed[:, 1],
    c=digits,
    cmap='tab10',
)

plt.colorbar(scatter, ticks=range(10), label="Digit Class")

plt.savefig('../paper/figs/fig-digits.png')

print('Figure Generating...')
plt.show()
