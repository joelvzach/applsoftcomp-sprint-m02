# Notes regarding 1D Multi Method Data

## Data Structure

- **File:** `data/1d-multi-method-data.csv`
- **Columns:** `method` (categorical), `AUCROC` (float, 0-1)
- **Rows:** 100 total — 10 observations per method, 10 methods (1 "Proposed" + 9 baselines)

## Observations

- "Proposed" ranks 3rd overall — better than 7 of 9 baselines
- AUC-ROC values range from ~0.19 (Baseline_8) to ~0.92 (Baseline_2)

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

