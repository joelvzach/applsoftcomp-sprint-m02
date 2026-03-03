#!/bin/bash
set -e
python3 workflow/format_2d_data.py
python3 workflow/viz_2d_data.py
