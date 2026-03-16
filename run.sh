#!/bin/bash
uv sync

uv run python workflow/format_2d_data.py

uv run python workflow/viz_1d_data.py
uv run python workflow/viz_2d_data.py
uv run python workflow/1d-multi-method-data-processing.py
uv run python workflow/viz_digits.py
