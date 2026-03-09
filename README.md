# Spotify Genre Classification — MSIN0097 Predictive Analytics

**Research question:** Does a learned autoencoder latent representation 
of Spotify audio features outperform raw features for 10-class genre 
classification?

**Short answer:** No. LightGBM on 13 raw features scores test macro-F1 = 
0.6565. The same model on autoencoder-encoded features scores 0.5790 — a 
drop of 0.0975. The encoder compresses away the multi-axis structure the 
classifier needs. This failure is the most informative result in the project.

---

## Setup
```bash
pip install -r requirements.txt
```

Python 3.10+ required.

---

## Data

Download the Spotify Tracks Dataset (CC0) from Kaggle:
https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset

Place the CSV at: `data/dataset.csv`

A 200-row sample is available in `data/` for pipeline validation.
Full download instructions in `data/README.md`.

---

## Run
```bash
jupyter notebook notebooks/01_full_pipeline_FINAL_v3.ipynb
```

Run cells In[1] → In[37] in order. Expected runtime: 8–12 minutes.

| Stage | Cells | Description |
|---|---|---|
| 1 — Problem Framing | In[1]–In[2] | Config, data load, registered predictions |
| 2 — EDA | In[3]–In[9] | Distributions, correlation, PCA |
| 3 — Preprocessing | In[10]–In[12] | Stratified split, scaling, leakage checks |
| 4 — Model Comparison | In[13]–In[26] | CV, t-test, tuning, feature importance |
| 5 — Autoencoder | In[27]–In[31] | Bottleneck sweep, latent PCA |
| 6 — Final Evaluation | In[32]–In[37] | Test set, confusion matrix, model card |

All random states controlled via `config.RANDOM_SEED = 42`.

Run tests with:
```bash
pytest tests/
```

---

## Key Results

| Model | CV Macro-F1 | Val Macro-F1 |
|---|---|---|
| Dummy baseline | — | 0.018 |
| Logistic Regression | 0.4396 | 0.4295 |
| MLP | 0.5648 | 0.5787 |
| Random Forest | 0.6610 | 0.6748 |
| **LightGBM (selected)** | **0.6695** | **0.6750** |
| LightGBM on autoencoder features | — | 0.5790 |
| **LightGBM test (held-out)** | — | **0.6565** |

Per-class test F1: classical 0.930 → indie 0.498 (43 percentage point spread).

---

## Repository Structure

```
├── notebooks/
│   └── 01_full_pipeline_FINAL_v3.ipynb   # Full pipeline, Stages 1–6
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── models.py
│   ├── evaluation.py
│   └── visualisation.py
├── tests/
│   ├── test_models.py
│   └── test_preprocessing.py
├── figures/                               # All 16 saved figures
├── data/
│   └── README.md                         # Download instructions
├── config.py                             # All hyperparameters and seeds
├── requirements.txt
└── README.md
```

---

## Agent Governance

Developed with Google Antigravity for code scaffolding and documentation drafting. Three interventions required human correction:

**1. MLP convergence (Cell In[22])** — agent used `max_iter=200`; 
loss sat at 0.607 with ConvergenceWarning raised. Raised to `max_iter=2000`; 
convergence at iteration 611, final loss 0.257.

**2. Model selection criterion (Cell In[26])** — agent proposed single-split 
val F1. Overridden: CV mean adopted, paired t-test added (t=3.657, p=0.022). 
Chart title records the decision explicitly.

**3. Bottleneck dimension (Cell In[29])** — agent declared dim=6 optimal via 
PCA heuristic. Rejected. Sweep across {4,6,8,10} run: dim=10 selected 
(F1=0.5775 vs 0.5261 for dim=6).

Full decision register and notebook screenshots in AppendixA_AgentLog.docx 
(submitted separately via Moodle).
