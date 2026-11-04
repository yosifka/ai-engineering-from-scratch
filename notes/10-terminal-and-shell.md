# Lesson 10: Terminal & Shell

**Phase:** 00 — Setup & Tooling  
**Status:** Completed ✅  
**Date:** November 4, 2026  
**Package Manager Rule:** Always use `uv` (`uv pip install ...`).  

---

## 1. Core Concepts

### Piping & Redirection
- **Conveyor Belt (`|`):** Connects the standard output (`stdout`) of one command directly to the standard input (`stdin`) of the next command in memory.
  - *Example:* `cat train.log | grep "loss" | wc -l`
- **Redirects:**
  - `>`: Overwrite file with `stdout`.
  - `>>`: Append to file with `stdout`.
  - `2>`: Redirect error messages (`stderr`).
  - `2>&1`: Redirect `stderr` to the same destination as `stdout`.
  - `python train.py > output.log 2>&1`: Captures both normal prints and crash tracebacks in one file.

### Terminal Hangups & `tmux`
- **The SIGHUP Problem:** Closing a terminal or dropping SSH sends `SIGHUP` to child processes, terminating running training jobs.
- **`tmux` (Terminal Multiplexer):** Creates persistent server-backed sessions independent of terminal windows.
  - Prefix Key: **`Ctrl + b`**
  - Split Horizontally: `Ctrl + b` then `"`
  - Split Vertically: `Ctrl + b` then `%`
  - Switch Panes: `Ctrl + b` then Arrow Key
  - Detach: `Ctrl + b` then `d` (job keeps running in the background)
  - Reattach: `tmux attach -t <session_name>`
  - List sessions: `tmux ls`

### Process Monitoring
- **`htop`:** Visual interactive process and system resource monitor (CPU, memory, threads).
- **`kill` / `pkill`:** Terminate processes by PID or name pattern (e.g., `pkill -f "python.*train"`).

### Remote SSH & Port Forwarding
- **`~/.ssh/config`:** Aliases complex remote connection strings into simple names (e.g. `ssh gpu`).
- **Local Port Forwarding (`ssh -L 8888:localhost:8888 user@gpu`):** Creates an encrypted tunnel forwarding local port 8888 to the remote server's port 8888, enabling local browser access to remote Jupyter or TensorBoard dashboards.

---

## 2. Hands-on Verifications Completed

1. **Installed Tooling:** Installed `tmux` (v3.8) and `htop` via Homebrew on Apple Silicon Mac.
2. **`tmux` Multi-Pane Session:**
   - Created session `training`.
   - Created 3 panes: top pane running `htop`, bottom pane running a background timer loop (`while true; do date; sleep 1; done`).
   - Detached with `Ctrl + b d`, verified persistence with `tmux ls`, and reattached with `tmux attach -t training`.
3. **Shell Aliases Configured:**
   - Appended `source shell_aliases.sh` to `~/.zshrc`.
   - Key aliases: `ae` (activate venv), `uvvenv` (create/activate with uv), `tls`, `ta`, `psg`.
4. **Log Processing Pipeline:**
   - Generated 100-epoch simulated log `fake_train.log`.
   - Extracted clean numerical loss values using `grep "loss:" fake_train.log | awk '{print $NF}' | tail -n 5`.
5. **Mac Keyboard Fix:**
   - Configured `"terminal.integrated.macOptionIsMeta": false` in VS Code settings so Option keys correctly output `|` and brackets on European keyboard layouts.
6. **SSH Config Entry:**
   - Created `~/.ssh/config` with host entry `gpu-practice` and verified with `ssh -G gpu-practice`.
