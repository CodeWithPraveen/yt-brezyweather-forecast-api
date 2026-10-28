# BrezyWeather Forecast API

Demo repository for the Code with Praveen video "Run Agents in Parallel in Claude Code". A small Python forecast API with two bugs that make three tests fail.

## Requirements

- Claude Code v2.1.311 or later, signed in
- Python 3.10 or later
- git

## Setup

Clone this repository (background sessions need a git repository for their worktrees). Then run `claude` once in the folder and choose **Yes, I trust this folder**, or `claude --bg` won't start.

```bash
python3 -m unittest   # 3 failures until the fixes land
```

## Tear down

```bash
claude agents --json --all --cwd "$PWD"     # IDs of this folder's background sessions
claude rm <id>                              # prints a --discard-unpushed value
claude rm <id> --discard-unpushed <value>   # deletes the session, its worktree, and its unpushed fix
git branch -D worktree-<name>               # only if a worktree- branch is left
```
