# Notes: 1d-multi-method-data.csv

## Data Structure

- **File:** `data/1d-multi-method-data.csv`
- **Columns:** `method` (categorical), `AUCROC` (float, 0–1)
- **Rows:** 100 total — 10 observations per method, 10 methods (1 "Proposed" + 9 baselines)

## Key Observations

| Method     | Mean AUC-ROC | Rank |
|------------|-------------|------|
| Baseline_2 | 0.917       | 1st  |
| Baseline_1 | 0.767       | 2nd  |
| **Proposed** | **0.661** | **3rd** |
| Baseline_9 | 0.557       | 4th  |
| ...        | ...         | ...  |
| Baseline_8 | 0.192       | 10th |

- "Proposed" ranks 3rd overall — better than 7 of 9 baselines
- AUC-ROC values range from ~0.19 (Baseline_8) to ~0.92 (Baseline_2)

## Visualization Strategy

- **Goal:** Highlight "Proposed" using preattentive encoding so it pops out immediately without cognitive effort
- **Preattentive features used:**
  - **Color**: Baselines in neutral gray; "Proposed" in a vivid contrasting color (e.g., orange/red)
  - **Size**: Slightly larger markers for "Proposed"
  - **Z-order**: "Proposed" drawn on top
- **Chart type:** Strip plot (dot plot) with each method on x-axis, sorted by mean AUC-ROC
  - Shows all 10 observations per method
  - Avoids bar chart which would imply start-from-zero comparison
- **Sorting:** Order methods by mean AUC-ROC so relative performance is clear at a glance
- Label both axes; add a horizontal reference line or annotation for "Proposed"
