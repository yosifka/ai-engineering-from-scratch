# Lesson 09: Data Management

**Phase:** 00 — Setup & Tooling  
**Status:** Completed ✅ (100% Quiz Score)  
**Date:** November 4, 2026  
**Package Manager Rule:** Always use `uv` (`uv pip install ...`).  

---

## 1. Core Concepts

### Hugging Face Hub & `datasets` Library
- **The Hub:** Global open-source registry for datasets, model weights, and AI demos.
- **Repository Naming:** Modern Hugging Face Hub enforces namespace notation (`owner/dataset_name`, e.g., `nyu-mll/glue`, `allenai/c4`, `stanfordnlp/imdb`).
- **Local Caching:** `load_dataset` downloads datasets once to `~/.cache/huggingface/datasets/` and loads instantly on subsequent runs.

### Streaming Datasets (`streaming=True`)
- **The Problem:** Many AI datasets (C4, Wikipedia, Common Crawl) are hundreds of gigabytes or terabytes and cannot fit on a single laptop disk.
- **Solution:** `streaming=True` returns an `IterableDataset`. Rows are fetched over HTTP on demand without saving the full dataset to disk, keeping RAM and disk usage constant and near zero.

### File Formats: CSV vs. Parquet vs. Arrow
- **CSV:** Row-based text format. Inefficient storage (numbers serialized as ASCII strings) and slow column-filtered reading.
- **Parquet:** Columnar compressed binary format (Snappy/ZSTD). The industry standard for on-disk ML dataset storage. Much smaller file sizes and fast column reads.
- **Arrow:** In-memory columnar format used by Hugging Face `datasets` for zero-copy memory-mapped operations.

### Reproducible Splits & Seeds
- Standard ML requires **Train (learns patterns)**, **Validation (tunes hyperparameters)**, and **Test (unbiased final evaluation)**.
- **`seed` parameter:** Machine learning relies on pseudo-randomness. Setting `seed=42` guarantees mathematical reproducibility so models are evaluated on identical test splits across all machines.

### Managing Large Files
- GitHub blocks individual files > 100 MB.
- **`.gitignore`:** Keep large files local (`*.pt`, `*.safetensors`, `*.parquet`, `data/`). Best for course and personal projects.
- **Git LFS:** Tracks text pointers in Git; binary blobs stored on an LFS server.
- **DVC (Data Version Control):** Connects Git commits to cloud storage (S3/GCS) with `.dvc` tracking files for production data lineage and experiment reproducibility.

---

## 2. Hands-on Exercises Completed

1. **Exercise 1 (Load & Inspect):**
   - Loaded `nyu-mll/glue` with config `mrpc` (3,668 train rows).
   - Inspected sentence pairs and paraphrase classification labels (`1` vs `0`).
2. **Exercise 2 (Streaming Throughput):**
   - Streamed `allenai/c4` (800 GB dataset) with `streaming=True`.
   - Processed **64,141 examples in 10.13 seconds (~6,334 examples/sec)** with zero disk consumption.
3. **Exercise 3 (Format Comparison):**
   - Exported MRPC dataset to CSV (915,219 bytes) and Parquet (623,315 bytes).
   - Confirmed Parquet is **1.47x smaller** on text and verified row count preservation (3,668 rows).
4. **Exercise 4 (70 / 15 / 15 Data Splits):**
   - Two-step splitting with `seed=42`: first 30% holdout, then split holdout 50/50.
   - Result: Train = 2,567 (70.0%), Val = 550 (15.0%), Test = 551 (15.0%).
   - Verified data integrity with `assert` ($2567 + 550 + 551 = 3668$) and confirmed deterministic row ordering.

---

## 3. Editor Configurations Applied
- Added `"jupyter.widgetScriptSources": ["jsdelivr.com", "unpkg.com"]` to enable interactive download progress bars in notebooks.
- Added `"notebook.formatOnSave.enabled": true` so `Cmd + S` formats notebook cells automatically.
- Observed Ruff's automatic import-sorting in action.
