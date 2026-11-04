# Lesson 08: Editor Setup

**Phase:** 00 — Setup & Tooling  
**Status:** Completed ✅  
**Date:** November 4, 2026  

---

## 1. Core Concepts

### Language Server Protocol (LSP)
- **Problem:** Historically, each editor needed its own plugin for each language ($N$ editors $\times$ $M$ languages).
- **Solution:** A standardized protocol (JSON-RPC) where a single Language Server (like **Pylance** for Python) provides autocompletion, type diagnostics, and hover information to any LSP-compatible editor.
- **Why for AI:** Libraries like PyTorch, NumPy, and Hugging Face have deep APIs. Pylance gives instant signature help and catches invalid argument types before running expensive scripts.

### Formatters & Linters
- **Black:** An opinionated, deterministic formatter (wraps at 88 chars). Formats code on save so styling arguments never happen and Git diffs remain clean.
  - *Key behavior:* Black strictly refuses to format any file that contains a syntax error to prevent code corruption.
- **Ruff:** An extremely fast linter and import organizer written in Rust. Catches unused imports, syntax smells, and dead code.

### Interactive Debugging (`debugpy`)
- Replaces repetitive `print()` statements with interactive inspection.
- **Breakpoints (🔴):** Freeze program execution right before a specific line.
- **Controls:**
  - `F5`: Continue running to the next breakpoint.
  - `F10`: Step Over (execute the current line and advance one line).
  - `F11`: Step Into (dive inside a called function).
  - `Shift + F5`: Stop debugging session.
- **Variables Panel & Debug Console:** Inspect local variables in memory and evaluate live Python expressions while execution is paused.

### Jupyter Notebooks & Output Management
- Running `.ipynb` natively in VS Code requires **`ipykernel`** inside the virtual environment (`pip install ipykernel`).
- **Variable Viewer (`{x}`):** Inspect shapes, sizes, and values of dictionaries, matrices, and datasets without printing.
- **Output Scrolling:** `"notebook.output.scrolling": true` with `"notebook.output.textLineLimit": 30` prevents long training/epoch logs from expanding the notebook indefinitely, keeping output contained inside a scrollable box.

### Remote SSH Development
- Allows VS Code to run a headless server component on remote GPU servers or cloud instances (Lambda Labs, RunPod, AWS).
- Local UI connects seamlessly over SSH, enabling local-like file editing, debugging, and terminal access without slow GUI forwarding.

---

## 2. Key Settings Configured (`~/.Library/Application Support/Code/User/settings.json`)

```json
{
    "python.analysis.typeCheckingMode": "basic",
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        }
    },
    "black-formatter.args": ["--line-length", "88"],
    "ruff.lint.run": "onSave",
    "editor.rulers": [88, 120],
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "notebook.output.scrolling": true,
    "notebook.output.textLineLimit": 30,
    "terminal.integrated.defaultProfile.osx": "zsh",
    "terminal.integrated.scrollback": 10000
}
```

---

## 3. Installed Extensions Stack
- `ms-python.python` & `ms-python.vscode-pylance` (Language server & static types)
- `ms-python.black-formatter` (Format-on-save)
- `charliermarsh.ruff` (Linter & import sorter)
- `ms-python.debugpy` (Interactive debugging)
- `ms-toolsai.jupyter` (Notebooks)
- `ms-vscode-remote.remote-ssh` (Remote GPU servers)
- `eamodio.gitlens` (Git history & annotations)

---

## 4. Hands-on Verifications Completed
1. **Pylance & Black:** Verified syntax error detection, auto-format on save with `Cmd+S`, and static type mismatch squigglies (`str` vs `list[float]`).
2. **Debugger (`debugpy`):** Set a breakpoint at line 5, stepped through a loop with `F10`/`F5`, inspected `item` and `results` in the Locals panel, and evaluated expressions in the Debug Console.
3. **Jupyter Notebooks:** Installed `ipykernel` into `.venv`, ran notebook cells with `Shift+Enter`, explored variables in the Variable Viewer, and verified output containment with `notebook.output.scrolling`.
4. **Terminal Shortcuts:** Practiced toggling terminal (`Ctrl + \``) and splitting terminals side-by-side (`Cmd + \`).
