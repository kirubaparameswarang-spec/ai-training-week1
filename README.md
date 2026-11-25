# AI Training Week 1 — Git and GitHub Workflow

## Project objective
Practice Git initialization/cloning, staging, commits, branches, pushing, pull requests,
merging, resolving a deliberate README conflict, and viewing Git history.

## Repository
Create a GitHub repository named **ai-training-week1**, then clone it locally.
Replace the placeholder links below after creating the repository and pull request.

- Repository: `PASTE_REPOSITORY_URL_HERE`
- Pull request: `PASTE_MERGED_PULL_REQUEST_URL_HERE`

## Project contents
- `.gitignore` — ignores `.env`, Python cache, virtual environments, and log files.
- `src/charts.py` — creates four charts in one figure using `plt.subplots(2, 2)`.
- `outputs/four_charts.png` — generated chart image (created when you run the script).
- `requirements.txt` — Python dependency.
- `WORKFLOW.md` — step-by-step Git/GitHub commands, including the conflict exercise.

## Setup and run
```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
python src/charts.py
```

## Submission checklist
- [ ] GitHub repository link added above
- [ ] Feature branch `feature/add-charts` pushed
- [ ] Pull request opened and merged into `main`
- [ ] Deliberate README merge conflict resolved and merged
- [ ] `git log --oneline --graph` screenshot saved as `outputs/git-log-graph.png`
