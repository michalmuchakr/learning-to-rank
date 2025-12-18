# Learning-to-Rank (E-commerce Search) — Take-home Solution

LightGBM LambdaRank solution for an e-commerce Learning-to-Rank task: rank products per search session and export the required artifacts (`results.json`, `predictions.csv`, `solution_summary.md`).

## Repository overview

- **`INSTRUCTIONS.md`**: Original task description and required output formats/metrics.
- **`search_sessions.csv`**: Input dataset (sessions, products, positions, clicks, product/user attributes).
- **`solution.ipynb`**: Main notebook (feature engineering, training, evaluation, export).
- **`extended_eda.ipynb`**: Additional exploratory analysis.
- **`results.json`**: Final metrics + business summary in the required JSON schema.
- **`predictions.csv`**: Model scores on the test split (as required by the task).
- **`solution_summary.md`**: Short write-up / conclusions.
- **`expected_format.json`**: Example of the required `results.json` structure.
- **`candidate_checker.py`**: Helper script that checks the *format/completeness* of the submission artifacts.
- **`requirements.txt`**: Python dependencies for notebooks/scripts.

## Environment setup

### Option A — Conda

```bash
conda create -n erli_task python=3.11 -y
conda activate erli_task
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Option B — pip + venv

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Quick checks / usage

- Run notebooks:

```bash
jupyter notebook
```

- Validate artifact format (optional):

```bash
python candidate_checker.py .
```

## Notes on evaluation
- `ndcg_at_5` in `results.json` is computed on the **test split** and follows a common LTR convention: **sessions with no positive labels (no-click sessions) are excluded** from the NDCG average (otherwise the metric is dominated by ~50% no-click sessions in this dataset).
- The notebook prints both variants for transparency.


