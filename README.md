# CFM2: Pedestrian Dynamics, WS 2026/27

Your personal repository for the assignments and the project.
Only you and the lecturer can see it.

## Install (once, on your own laptop)

You need Python 3.10 or newer and git.

### macOS and Linux

```bash
git clone <your-repo-url>
cd <your-repo>
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python check_setup.py
```

### Windows (PowerShell)

```powershell
git clone <your-repo-url>
cd <your-repo>
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python check_setup.py
```

If PowerShell refuses to run the activation script, run
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once.

The last line printed must be `Setup OK`. If it is not, post the full
error message in the Moodle forum before the lecture.

### Start working

Activate the environment (see above), then:

```bash
jupyter lab
```

## Submitting an assignment

Each assignment is submitted as a pull request (PR) in this repository.

```bash
git switch -c assignment1
# work on assignment1/assignment1.ipynb
git add assignment1/
git commit -m "Solve assignment 1 counter-flow test"
git push -u origin assignment1
```

Then open a pull request from `assignment1` to `main` on GitHub.
Feedback is given as comments in the PR. Answer the comments and push
fixes to the same branch; do not merge the PR yourself.

Commit early and often: the history shows how your solution developed.

## Rules

- Write your own code. In the oral exam you explain every line of it.
- Keep results reproducible: fixed random seeds, repetitions, plots with
  axis labels and units.
