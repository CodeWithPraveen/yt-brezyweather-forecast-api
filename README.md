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
claude agents --json --all --cwd "$PWD"
```

`--cwd` limits the list to sessions started in this folder, so you don't delete work from other projects. Delete each session with `"kind": "background"` and its worktree, replacing `<id>` with its `id`:

```bash
claude rm <id>
```

Each session committed its fix in its worktree, and those commits were never pushed, so `claude rm` stops and prints a `--discard-unpushed` value instead of deleting. To throw the demo fixes away, run it again with that value:

```bash
claude rm <id> --discard-unpushed <value>
```

If `git branch` still lists `worktree-…` branches afterwards, delete each one:

```bash
git branch -D worktree-<name>
```
