# %% Generate 1d synthethic data
import numpy as np
import pandas as pd

n = 10
cases = np.random.uniform(8, 64, size=n) * 0.25
control = np.random.uniform(8, 64, size=n) * 0.25

cases = 2**cases
control = 2**control

pd.DataFrame(
    {
        "value": np.concatenate([cases, control]),
        "group": ["cases"] * n + ["control"] * n,
    }
).to_csv("1d-data.csv", index=False)


# %% Generate 2D synthetic data
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

n_samples = 3000
cluster_1 = np.random.normal(loc=[2, 2], scale=0.2, size=(n_samples, 2))
cluster_2 = np.random.normal(loc=[2.4, 2.4], scale=0.2, size=(n_samples, 2))
xy = np.vstack([cluster_1, cluster_2])

pd.DataFrame(
    {
        "x": xy[:, 0],
        "y": xy[:, 1],
    }
).to_csv("2d-data.csv", index=False)

# %% Generate 1D with multiple groups
n_samples = 10
n_methods = 10
rank = np.arange(n_methods)
np.random.shuffle(rank)
data = []
for i in range(n_methods):
    if i == 0:
        method = "Proposed"
    else:
        method = "Baseline_" + str(i)
    values = np.random.uniform(
        0.25 * (rank[i] + 1), 0.25 * (rank[i] + 2), size=n_samples
    )
    values = 2**values
    data += [{"method": method, "value": v} for v in values]

vmax = max([d["value"] for d in data])
for d in data:
    d["value"] = d["value"] / vmax

pd.DataFrame(data).rename(columns={"value": "AUCROC"}).to_csv(
    "1d-multi-method-data.csv", index=False
)
# fig, ax = plt.subplots(figsize=(8, 6))
# sns.barplot(data=pd.DataFrame(data), x="method", y="value_norm", ax=ax)
# plt.show()
