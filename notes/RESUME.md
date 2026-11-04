# 📌 AI Engineering — Resume Next Session

**Date Updated:** November 4, 2026  
**Curriculum:** AI Engineering from Scratch  
**Status:** Phase 00 (Lessons 01–10 Complete ✅)  
**Last Session:** Lesson 10: Terminal & Shell (All 4 hands-on exercises complete: tmux, aliases, log parsing, SSH config)  
**Next Session:** Phase 00, Lesson 11: Linux for AI  
**Package Manager Rule:** Always use `uv` (`uv pip install ...`).  

---

### 📝 Lesson 10 Recap: Terminal & Shell
- **tmux Multiplexer:** Built a 3-pane workflow (`htop` + background timer + script runner). Mastered prefix key `Ctrl + b`, detaching (`Ctrl + b d`), listing sessions (`tmux ls`), and reattaching (`tmux attach -t training`).
- **AI Shell Aliases:** Added production aliases (`ae` for venv activation, `uvvenv`, `tls`, `psg`) to `~/.zshrc`.
- **Log Parsing Pipelines:** Built stream-filtering pipelines with `grep`, `awk '{print $NF}'`, and `tail` to extract raw loss metrics from 100-epoch training logs.
- **Output Redirection:** Mastered stdout/stderr redirection (`> output.log 2>&1`) to preserve full training and error logs.
- **SSH & Port Forwarding:** Configured `~/.ssh/config` for alias resolution (`ssh gpu-practice`) and reviewed local port forwarding (`ssh -L 8888:localhost:8888`) for remote Jupyter/TensorBoard access.

---

### 🚀 Commands to Resume Next Session:

1. **Open Terminal and navigate to the project repository:**
   ```bash
   cd "/Users/ponti/Desktop/AI from scratch/ai-engineering-from-scratch"
   ```

2. **Activate the Python virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

3. **Check Git status:**
   ```bash
   git status
   ```

4. **Prompt to start the session:**
   > *"I'm ready for Phase 00, Lesson 11: Linux for AI!"*
