# 📌 AI Engineering — Resume Next Session

**Date Updated:** November 3, 2026  
**Curriculum:** AI Engineering from Scratch  
**Status:** Phase 00 (Lessons 01–07 Complete ✅)  
**Last Session:** Lesson 07: Docker for AI (All 4 hands-on exercises + quiz complete 100%)  
**Next Session:** Phase 00, Lesson 08: Editor Setup  

---

### 📝 Lesson 07 Recap: Docker for AI
- **Container vs VM:** Isolated user-space process sharing host kernel vs. full virtualized guest OS.
- **Base Images:** `-devel` (7.54 GB with `nvcc` and compilation toolchains) vs. `-runtime` (5.00 GB clean execution, saving 2.54 GB).
- **Hardware Passthrough:** NVIDIA Container Toolkit bridges host GPUs to containers (`--gpus all`). (Apple Silicon runs natively with MPS on macOS).
- **Volumes:** Volume mounts (`-v ~/models:/models`) ensure large AI weights and datasets persist across container stops/rebuilds.
- **Docker Compose:** Spawns multi-service topologies (AI runtime + Qdrant vector database) connected via internal DNS.
- **Port Mapping:** `-p <HOST_PORT>:<CONTAINER_PORT>` (mapped host port 5001 to container port 5000 to avoid Mac AirPlay conflicts on 5000).

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
   > *"I'm ready for Phase 00, Lesson 08: Editor Setup!"*
