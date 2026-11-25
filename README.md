# AI Training Week 1 — Git and GitHub Workflow

## Project objective
Practice Git initialization, staging, commits, branches, pushing, pull requests, merging, resolving merge conflicts, and viewing Git history.

## Repository
- Repository: https://github.com/kirubaparameswarang-spec/ai-training-week1
- Pull Request #1: https://github.com/kirubaparameswarang-spec/ai-training-week1/pull/1

## Project contents
- `.gitignore` — ignores `.env`, Python cache, virtual environments, and log files.
- `src/charts.py` — creates four charts in one figure using `plt.subplots(2, 2)`.
- `outputs/four_charts.png` — generated chart image.
- `requirements.txt` — Python dependency.
- `WORKFLOW.md` — Git workflow instructions.

## Setup and run

```powershell
python -m pip install -r requirements.txt
python src/charts.py
```

## Four charts
1. Line chart
2. Bar chart
3. Scatter plot
4. Pie chart

## Git and GitHub workflow completed
- Created and cloned `ai-training-week1`.
- Added and committed `.gitignore`.
- Created `feature/add-charts`.
- Committed and pushed the chart files.
- Created and merged Pull Request #1.
- Created two branches to demonstrate a README merge conflict.
- Resolved the README conflict and preserved the original documentation.

## Conflict resolution record

Conflict exercise: Both branch changes were reviewed and this final wording resolves the conflict.

## Submission checklist
- [x] GitHub repository created.
- [x] `.gitignore` committed.
- [x] Feature branch and chart script committed.
- [x] Pull Request #1 merged.
- [x] README merge conflict created.
- [x] README conflict resolution completed.
- [ ] Conflict-resolution branch merged into `main`.
- [ ] Git graph screenshot saved as `outputs/git-log-graph.png`.
