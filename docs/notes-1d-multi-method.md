# Visualization Approach and Design Decisions

## Objective

The goal of this visualization is to compare AUC-ROC measurements across multiple methods while clearly highlighting the **"Proposed"** method using preattentive visual encoding. The visualization must:

1. Clearly label axes
2. Avoid misleading representations
3. Effectively emphasize "Proposed" without distorting the data

---

## Concept

- AUC-ROC stands for Area Under Curve - Receiver Operating Characteristic.
- It is a performance metric for binary classification models (spam/not-spam)
- It plots true positive rate against flase positive rate
- Higher value means the model is more reliable.

## Data Characteristics

- **Metric:** AUC-ROC (continuous, bounded between 0 and 1)
- **Groups:** 10 methods (Proposed + Baseline_1 to Baseline_9)
- **Samples per method:** 10 measurements
- **Structure:** One-dimensional quantitative data grouped by category

Because the dataset contains multiple measurements per method, the focus is on comparing **distributions**, not just summary statistics.

---

## Choice of Visualization

### Why Boxplot?

A boxplot was chosen because it:

- Shows distribution (median, quartiles, variability)
- Works well with small sample sizes
- Avoids binning artifacts (unlike histograms)
- Allows clear comparison across categories
- Is standard for model performance comparison

Histograms were not used because:
- They are better suited for examining a single distribution
- Overlaying multiple histograms would create clutter
- The small sample size (n=10 per method) makes histogram binning unreliable

---

## Preattentive Visual Encoding Strategy

The goal was to make the **"Proposed"** method stand out immediately without altering the data.

The following preattentive cues were used:

### 1. Color Contrast
- **Proposed:** Strong saturated blue
- **Baselines:** Neutral light gray

Color contrast draws immediate attention while preserving visual clarity.

### 2. Border Thickness
- Proposed box has a thicker outline
- Baselines have thinner outlines

This reinforces emphasis without exaggerating magnitude.

### 3. Position
- Proposed is placed first (leftmost position)

Position is a strong perceptual cue that naturally attracts attention.

### 4. Bold Labeling
- The x-axis label for "Proposed" is bolded

This strengthens emphasis without altering the data representation.

---

## Ensuring Non-Misleading Design

Several steps were taken to avoid misleading interpretation:

- The y-axis spans the full valid AUC range (0–1)
- No axis truncation was used
- No distortion or scaling exaggeration
- All methods are plotted using identical boxplot geometry
- No additional visual effects imply superiority

The visualization highlights "Proposed" visually, but does not manipulate scale or structure to suggest it performs better than the data indicates.

---

## Design Decisions Summary

| Decision | Rationale |
|----------|------------|
| Boxplot | Best for comparing grouped distributions |
| Neutral baselines | Avoid visual clutter |
| Strong color for Proposed | Immediate perceptual emphasis |
| Full 0–1 axis | Prevent distortion |
| Clean layout | Improve interpretability |

---

## AI Usage Disclosure

AI assistance was used to:

- Clarify visualization best practices
- Refine understanding of preattentive encoding principles
- Improve code structure and formatting
- Strengthen explanation clarity

All design decisions, interpretation, and final implementation choices were critically reviewed and verified to ensure correctness and adherence to visualization principles.

No automated generation was used to fabricate results or alter data representation.

---

## Files in `docs/`

All required documentation files in the `docs/` directory are complete and include:

- Final visualization output
- Source code
- This explanatory write-up
- Any additional required artifacts

---
