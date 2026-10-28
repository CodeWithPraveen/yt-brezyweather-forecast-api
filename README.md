# BrezyWeather Forecast API: Parallel Agents Demo

The Code with Praveen video "Run Agents in Parallel in Claude Code" walks through each step on screen. This repository holds the small BrezyWeather forecast API the demo runs against.

## Prerequisites

- Claude Code v2.1.311 or later (the version this demo was verified on), signed in
- Python 3.10 or later (standard library only)
- git

## Folders

| Folder | What it holds |
| --- | --- |
| `brezyweather/` | The forecast API: unit conversion, wind alerts, forecast builder |
| `tests/` | Unit tests; three fail, from two bugs, until the demo's fixes land |
| `logs/` | A noisy API log for the subagent investigation |

## Warnings

- Run the demo in its own git repository. Background sessions create worktrees under `.claude/worktrees/`. If you copied this folder rather than cloning the repo, make it a git repository first:

  ```bash
  git init && git add . && git commit -m "Initial commit"
  ```

- Run `claude` once in the folder and choose **Yes, I trust this folder** before you start background sessions. `claude --bg` refuses to start in a folder you haven't trusted.

## Tear down

List the background sessions the demo started, with their IDs:

```bash
claude agents --json --all
```

Delete each session and its worktree, replacing `<id>` with a session ID from the list:

```bash
claude rm <id>
```

If `git branch` still lists `worktree-…` branches afterwards, delete each one:

```bash
git branch -D worktree-<name>
```
