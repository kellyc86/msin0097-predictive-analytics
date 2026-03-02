# Agent Usage Log + Decision Register
# MSIN0097 Predictive Analytics
# Agent tool: Google Antigravity

---

## Decision Register

| # | Date | Stage | What I asked | Agent output | Decision | Verification | Rationale |
|---|------|-------|--------------|--------------|----------|--------------|-----------|
| 1 | 02/03/2026 | Stage 2 EDA | Generate EDA plots and data quality checks | 5 plots with stratified sampling code | Accepted with modification | Verified stratified sampling, added EDA-only scaler comment, fixed pandas bug | Mechanical code generation appropriate for agent delegation |

---

## Agent Mistakes Caught

| # | Date | Stage | What went wrong | How I caught it | How I corrected it |
|---|------|-------|-----------------|-----------------|-------------------|
| 1 | 02/03/2026 | Stage 2 EDA | groupby().apply() pandas compatibility error | Runtime ValueError on execution | Replaced with version-safe pd.concat() stratified sampling |
---

## Verification Standards Applied
- Primary metric verified as macro-F1 on every model
- Test set confirmed untouched during development
- Random seeds checked in all stochastic operations
- Scaler confirmed fitted on training data only
