# Git and GitHub Workflow — Step by Step

Run these commands in PowerShell. Replace the GitHub URL with your own repository URL.

## 1. Create and clone the GitHub repository
1. On GitHub, create a repository named `ai-training-week1`.
2. Do not initialize it with a README if you want to use the commands below exactly.
3. In PowerShell:

```powershell
cd $HOME\Desktop
git clone https://github.com/YOUR-USERNAME/ai-training-week1.git
cd ai-training-week1
```

If the repository already has a README, clone it and continue from step 2.

## 2. Add and commit .gitignore
Copy this project's `.gitignore` into the cloned repository, then:

```powershell
git add .gitignore
git commit -m "Add Python-focused gitignore"
git push origin main
```

If your default branch is named `master`, use `master` instead of `main`.

## 3. Create the chart feature branch and commit the chart
Copy `src/charts.py` and `requirements.txt` into the repository. Then:

```powershell
git switch -c feature/add-charts
python -m pip install -r requirements.txt
python src/charts.py
git add src/charts.py requirements.txt outputs/four_charts.png
git commit -m "Add four-chart training dashboard"
git push -u origin feature/add-charts
```

## 4. Open and merge a Pull Request
1. Open the repository on GitHub.
2. Choose **Compare & pull request** for `feature/add-charts`.
3. Base: `main`; compare: `feature/add-charts`.
4. Use title: `Add four-chart training dashboard`.
5. Create the PR, review it, then select **Merge pull request** and confirm.
6. Back in PowerShell:

```powershell
git switch main
git pull origin main
```

Save the PR URL in `README.md`.

## 5. Create a deliberate README merge conflict

Start from an updated `main`:

```powershell
git switch main
git pull origin main
git switch -c conflict/first
```

Edit `README.md` and add this line near the end:

`Conflict exercise: README wording from branch FIRST.`

Then commit it:

```powershell
git add README.md
git commit -m "Add first README conflict version"
git switch main
git switch -c conflict/second
```

Edit the same location in `README.md`, but use a different line:

`Conflict exercise: README wording from branch SECOND.`

Commit it:

```powershell
git add README.md
git commit -m "Add second README conflict version"
```

Merge the first branch into the second branch:

```powershell
git merge conflict/first
```

Git should report a conflict because both branches changed the same line. Open `README.md` and find markers similar to:

```text
<<<<<<< HEAD
Conflict exercise: README wording from branch SECOND.
=======
Conflict exercise: README wording from branch FIRST.
>>>>>>> conflict/first
```

Resolve the conflict by deleting all marker lines and keeping one final sentence, for example:

`Conflict exercise: Both branch changes were reviewed and this final wording resolves the conflict.`

Then finish the merge:

```powershell
git add README.md
git commit -m "Resolve README merge conflict"
git push -u origin conflict/second
```

Open a second Pull Request from `conflict/second` into `main`, then merge it on GitHub. Finally:

```powershell
git switch main
git pull origin main
```

## 6. Capture the Git history graph
Run:

```powershell
git log --oneline --graph --decorate --all
```

Take a screenshot showing the graph and save it as:

`outputs/git-log-graph.png`

You can use **Win + Shift + S** on Windows, then save the screenshot at that path.

## 7. Verify and submit
```powershell
git status
git log --oneline --graph --decorate --all
git remote -v
```

The working tree should be clean. Submit:
- GitHub repository URL
- Merged Pull Request URL (include both PRs if your instructor expects the conflict-resolution PR too)
- `outputs/git-log-graph.png`

## Important notes
- A local deletion does not automatically delete a file from GitHub. GitHub changes only after you commit and push the deletion.
- Do not commit `.env`, `.venv/`, `__pycache__/`, or log files.
- The chart data is sample data for demonstrating chart types; replace it if your assignment provides a dataset.
