# msin0097-predictive-analytics
## MSIN0097 Predictive Analytics — Individual Coursework

**Research Question:** Can a learned autoencoder latent representation of
Spotify audio features outperform raw features for genre classification,
and what does the latent space reveal about musical similarity?

## Setup
pip install -r requirements.txt

## Data
Follow instructions in data/README.md to download the dataset from Kaggle.

## Run
jupyter notebook notebooks/01_full_pipeline.ipynb

All random seeds fixed in config.py. Results are fully reproducible.

## Repository Structure
config.py          — all pipeline constants and hyperparameters
src/               — modular pipeline code
notebooks/         — main analysis notebook
tests/             — validation checks (run with: pytest tests/)
data/              — data access instructions
appendix/          — agent usage log and decision register

## Agent Tooling
Google Antigravity used throughout.
See appendix/agent_usage_log.md for full log of contributions
and verification decisions.
