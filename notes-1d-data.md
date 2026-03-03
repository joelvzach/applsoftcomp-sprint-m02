# Notes: 1d-data.csv

## Data Structure

- **File:** `data/1d-data.csv`
- **Columns:** `value` (float), `group` (categorical: "cases" or "control")
- **Rows:** 20 total — 10 cases, 10 control subjects

## Key Observations

| Group   | Mean     | Min   | Max       |
|---------|----------|-------|-----------|
| cases   | 8,537    | 4.6   | 35,765    |
| control | 2,803    | 20.8  | 6,433     |

- Values span roughly 4 orders of magnitude (4 to 35,765), indicating a **heavy right-skewed distribution**
- Raw linear scale would compress smaller values and make group comparison misleading
- The cases group has a higher mean but also far more variance

## Visualization Strategy

- **Use log scale** on the y-axis to faithfully represent the wide value range without compressing the low end
- **Strip plot (jitter) + box plot overlay**: With only 10 points per group, showing individual data points avoids hiding distribution shape behind summary statistics
- **Label axes clearly**: y-axis = "Value (log scale)", x-axis = "Group"
- **Avoid** bar charts with means — with this skew and small n, means are misleading
