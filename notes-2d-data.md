# Notes: 2d-data.csv

## Data Structure

- **File:** `data/2d-data.csv`
- **Columns:** `x` (float), `y` (float)
- **Rows:** 6,000 samples

## Key Observations

| Stat   | x      | y      |
|--------|--------|--------|
| mean   | 2.20   | 2.20   |
| std    | 0.28   | 0.29   |
| min    | 1.24   | 1.36   |
| max    | 3.10   | 3.18   |

- Both dimensions are centered near 2.2 with similar spread (~0.28 std)
- Range is ~1.2 to ~3.2 for both axes — roughly symmetric
- 6,000 points is too dense for a plain scatter plot (severe overplotting)

## Visualization Strategy

- **KDE contour plot (density contours)**: Reveals the 2D distribution shape without overplotting. Shows where samples concentrate.
- **Hexbin or 2D histogram**: Alternative approach that bins points into hexagonal cells, encoding density with color.
- Chosen: **KDE contour with scatter underlay** — contours show overall density structure, and a low-alpha scatter plot underneath gives a sense of individual points.
- Label axes as "x" and "y" since no domain-specific names are given.
- Use equal aspect ratio so the x and y scales are visually comparable.
