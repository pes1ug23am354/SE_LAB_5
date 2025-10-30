# SE_LAB_5 — Static Code Analysis for inventory_system

Author: Vivan Jeevan Naik (SRN: pes1ug23am354), Section F  
Date: 2025-10-30

## Purpose
This repo demonstrates static analysis and remediation for a small inventory example (`inventory_system.py`). I fixed runtime and type-safety issues, added validation and logging, and produced security and style reports.

## Files
- `inventory_system.py` — original file (unchanged).
- `cleaned_inventory_system.py` — cleaned, validated, and logged version (submit this).
- `pylint_report.txt` — Pylint output for `cleaned_inventory_system.py`.
- `flake8_report.txt` — Flake8 output for `cleaned_inventory_system.py`.
- `bandit_report.txt` — Bandit security scan for the repo.
- `README.md` — this file.
- `reflection.md` — short reflection answers.

## How to run
(Assuming macOS/Linux with Python 3)

```bash
# optional: create & activate venv
python3 -m venv venv
source venv/bin/activate

# install tools
pip install --upgrade pip
pip install pylint flake8 bandit

# run the cleaned program
python3 cleaned_inventory_system.py

# generate static analysis reports (overwrite previous)
pylint cleaned_inventory_system.py > pylint_report.txt 2>&1
flake8 cleaned_inventory_system.py > flake8_report.txt 2>&1
bandit -r . --exclude venv > bandit_report.txt 2>&1
