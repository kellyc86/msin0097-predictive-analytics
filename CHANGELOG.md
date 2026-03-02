# CHANGELOG — MSIN0097 Predictive Analytics
# Spotify Genre Classification — Autoencoder + Classifier Pipeline
# GitHub: kellyc86/msin0097-predictive-analytics

## HOW TO USE
Update at the end of every Antigravity session.

---

## PROJECT ARCHITECTURE (locked 02/03/2026)

Research Question: Can a learned autoencoder latent representation of 
Spotify audio features outperform raw features for genre classification?

Dataset: maharshipandya/-spotify-tracks-dataset (Kaggle)
Target: track_genre — top 10 genres, ~15k rows
Primary metric: macro-F1
Split: 70/15/15 stratified, random_seed=42
Test set: LOCKED throughout development

Model pipeline:
0. Dummy classifier (baseline)
1. Logistic Regression
2. Random Forest
3. XGBoost/LightGBM
4. MLP end-to-end (Keras)
5. Autoencoder + Classifier (main contribution)

---

## SESSION LOG

### SESSION 001 — 02/03/2026
Tool: Manual setup
Stage: Project initialisation
What was done:
- Created GitHub repo: msin0097-predictive-analytics
- Scaffolded full folder structure
- Created config.py, requirements.txt, README.md,
  data/README.md, appendix/agent_usage_log.md
Commits: 4fe0f17
Next steps:
- [ ] Create notebook structure in Antigravity
- [ ] Download dataset from Kaggle
- [ ] Begin EDA

---

### SESSION 002 — 02/03/2026
Tool: Antigravity
Stage:
What was done:

Agent contributions:

Agent mistakes caught:

Commits:

Next steps: