# Phase 00 — Lesson 07: Docker for AI — Notes & Summary

**Date:** November 3, 2026  
**Curriculum:** AI Engineering from Scratch  
**Phase:** 00 - Setup and Tooling  
**Lesson:** 07 - Docker for AI  
**Status:** Completed ✅  
**Quiz Score:** 3 / 3 (100%)

---

## 1. Core Problem: Dependency & Environment Fragility
- AI stacks combine complex matrices of Python, PyTorch, CUDA, cuDNN, and C++ compilers.
- Code working locally frequently fails on remote servers or collaborator machines due to ABI mismatches or driver conflicts.
- Docker encapsulates runtime, libraries, system dependencies, and code into an immutable, reproducible container.

## 2. Key Architecture: Containers vs. Virtual Machines
- **Virtual Machines (VMs):** Virtualize hardware and run an entire guest operating system with a separate kernel. Heavyweight, slow boot times.
- **Containers:** Isolated user-space processes sharing the host operating system's kernel via Linux namespaces and cgroups. Starts in seconds with near-zero virtualization overhead.
- **macOS / Windows Execution:** Runs via lightweight background Linux VMs (Hypervisor framework on macOS, WSL2 on Windows). On Apple Silicon, amd64 images run under emulation via Rosetta 2 / QEMU.

## 3. Base Image Hierarchy
- `nvidia/cuda:12.4.1-devel-ubuntu22.04`: Full CUDA toolkit including `nvcc` compiler and headers. Required for compiling C++/CUDA extensions from source (e.g. `flash-attn`, `bitsandbytes`).
- `nvidia/cuda:12.4.1-runtime-ubuntu22.04`: CUDA runtime libraries only. No compilers. Optimized for serving pre-built wheels.
- `pytorch/pytorch:2.6.0-cuda12.4-cudnn9-runtime`: Pre-installed PyTorch wheel on CUDA runtime.
- `python:3.12-slim`: CPU-only minimal Debian image (~150 MB).

## 4. Hardware Passthrough: NVIDIA Container Toolkit
- Containers are isolated from host PCI devices by default.
- The NVIDIA Container Toolkit hooks the host's NVIDIA kernel driver (`/dev/nvidia*`) into the container when invoked with `--gpus all`.
- *Apple Silicon Note:* Apple Silicon uses Unified Memory and Metal Performance Shaders (`mps`). PyTorch GPU acceleration on Mac is handled natively on macOS without `--gpus all`.

## 5. Persistence via Volume Mounts
- Any files written inside an unmounted container filesystem are ephemeral and destroyed upon container shutdown.
- Large AI model weights (14+ GB) and datasets must be mounted from the host (`-v ~/models:/models`) to survive container rebuilds without re-downloading.

## 6. Multi-Service AI Architecture with Docker Compose
- AI systems pair inference runtimes with vector databases (e.g., Qdrant) or caching layers.
- Docker Compose establishes a private bridge network where services communicate seamlessly via DNS service names (e.g. `http://qdrant:6333`).
- Volumes like `qdrant_data:/qdrant/storage` persist indexed vector embeddings across service restarts.

---

## 7. Hands-on Exercises Completed

### Exercise 1: Build & Verify PyTorch
- Successfully built `ai-dev` image from `phases/00-setup-and-tooling/07-docker-for-ai/code/Dockerfile`.
- Verified execution inside the container with `python -c "import torch; print(torch.__version__)"`.
- Verified version: `2.6.0+cu124` with automatic CPU fallback on Mac.

### Exercise 2: Docker Compose & Network Resolution
- Configured and launched multi-service stack (`ai-dev` + `qdrant/qdrant:v1.12.5`).
- Entered running container via `docker compose exec ai-dev bash`.
- Verified internal network DNS by querying `curl http://qdrant:6333/collections`, receiving `status: ok`.

### Exercise 3: Custom Package & Port Mapping
- Added `flask` to Dockerfile with `--ignore-installed blinker` to resolve Ubuntu distutils system package conflicts.
- Observed layer caching in action (rebuild took under 3 seconds).
- Handled macOS port 5000 AirPlay collision by mapping host port 5001 to container port 5000 (`-p 5001:5000`).
- Tested live web server from Mac browser/curl, receiving `{"message":"Hello from inside the Docker container!","status":"success"}`.

### Exercise 4: Base Image Footprint Comparison
- Measured `devel` image content size: **7.54 GB** (includes `nvcc` and compilation tools).
- Switched base image to `runtime` (`nvidia/cuda:12.4.1-runtime-ubuntu22.04`) and built `ai-dev-runtime`.
- Measured `runtime` image content size: **5.00 GB** — saving **2.54 GB (33% smaller)** by omitting compilers.
