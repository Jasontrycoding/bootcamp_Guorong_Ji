# HW2 – Reproducible Tooling Setup

This folder contains a reproducible Python scaffold for the ETF premium/discount vs. liquidity project.
It includes a pinned environment (`requirements.txt`), a secrets template (`.env.example`), a minimal
config loader (`src/config.py`), and a Jupyter notebook to verify environment & config. Follow the README
to reproduce: create/activate env → `pip install -r requirements.txt` → copy `.env.example` to `.env` and run
`notebooks/00_project_setup.ipynb` top-to-bottom.
