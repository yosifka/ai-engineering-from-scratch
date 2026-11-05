# Lesson 11 — Linux for AI: Personal Notes

## Key idea

Most AI training runs on Ubuntu Linux on a remote GPU box. The terminal is the only interface. This lesson is a survival guide for that moment.

---

## File system layout

Linux uses a single tree rooted at `/`. No `C:\` or `/Volumes`. Key dirs:

| Path | What it is |
|------|-----------|
| `~` / `/home/username/` | Your home — clone repos, run training here |
| `/etc/` | Config files for the system |
| `/var/log/` | Logs — check here when something breaks |
| `/tmp/` | Temporary files, wiped on reboot |
| `/usr/` | Installed programs and libraries |
| `/proc/`, `/sys/` | Virtual files — live kernel and hardware info |

---

## Commands that matter

### Navigation
```bash
pwd           # Where am I?
ls -la        # List everything, including hidden files, with details
cd ~          # Go home
cd ..         # Go up one level
```

### Files
```bash
touch file.py          # Create empty file (or update timestamp)
mkdir -p a/b/c         # Create nested dirs in one shot
cp -r src/ backup/     # Copy a directory recursively
mv old/ new/           # Rename a folder (mv does both move and rename)
rm -rf dir/            # ⚠️ Permanent delete — no trash, no undo
tail -f training.log   # Watch a log update live (Ctrl+C to stop)
```

### Search
```bash
grep -r "learning_rate" .       # Search all files in current dir
find . -name "*.ckpt" -size +1G # Find checkpoints over 1GB
```

---

## Permissions

```
-rwxr-xr-- 1 user group 2048 file.py
 ^^^          owner: read + write + execute
    ^^^       group: read + execute
       ^^     others: read only
```

Common fixes:
```bash
chmod +x train.sh       # Make executable
chmod 755 deploy.sh     # Owner full, others read+execute
chmod 644 config.yaml   # Owner read+write, others read only
```

The number breakdown: 7=rwx, 6=rw, 5=r-x, 4=r, 0=none.

When something says "Permission denied" → `chmod +x` or `sudo` fixes it.

---

## Package management (apt)

```bash
sudo apt update                  # Always do this first (syncs package list)
sudo apt install -y build-essential git curl wget tmux htop unzip python3-venv
```

This exact block sets up a fresh GPU box.

---

## Processes

```bash
htop              # Interactive monitor — sort by MEM% with F6
ps aux | grep python   # Find running Python processes
kill -9 <PID>     # Force kill a stuck process
nvidia-smi        # GPU usage, temperature, processes
```

The `|` pipe connects commands — output of one feeds into the next.

---

## Disk space

```bash
df -h                        # Available disk on all drives
du -sh ~/.cache/*            # What's eating your cache?
du -sh ~/.cache/* | sort -h  # Sort by size, biggest last
```

Watch `~/.cache/huggingface/` — it fills up fast with downloaded models.

Space savers:
```bash
pip cache purge
uv cache clean
sudo apt clean
```

---

## Networking

```bash
wget https://example.com/model.bin       # Download a file
scp file.txt user@host:~/               # Copy to remote
rsync -avP file.txt user@host:~/        # Smarter copy — only transfers changes
```

**rsync vs scp:** rsync checks what's already on the remote and only sends the diff. Run it twice on the same file — second time sends ~0 bytes.

---

## tmux — the most important tool on a remote box

Closing your laptop kills your SSH session and your training run. tmux sessions live on the server, not in your connection.

```bash
tmux new -s train       # Create session named "train"
# Ctrl+B then D         # Detach — training keeps running
tmux ls                 # List sessions
tmux attach -t train    # Reattach
exit                    # Kill session when done
```

**Golden rule:** always run long training jobs inside tmux.

---

## macOS → Linux gotchas

| macOS | Linux |
|-------|-------|
| `brew install x` | `sudo apt install x` |
| `~/.zshrc` | `~/.bashrc` (bash is default on servers) |
| Case-insensitive filesystem | Case-sensitive — `Model.py` ≠ `model.py` |
| `sed -i '' 's/a/b/' f` | `sed -i 's/a/b/' f` (no empty string) |
| `pbcopy` / `pbpaste` | Not available over SSH |

---

## Exercises done ✅

1. Created `~/linux-ai-practice/` with `model.py`, `train.sh`, `config.yaml` using `touch`. Read `ls -la` output — understood permission bits, ownership, and 0-byte size.
2. Installed `htop` with brew. Sorted by MEM% — Brave Browser was the top consumer.
3. Full tmux workflow: `new -s train` → ran `sleep 300` → detached → `tmux ls` → reattached → killed session.
4. `df -h` showed 50Gi available. `du -sh ~/.cache/* | sort -h` revealed `~/.cache/uv` at 1.3GB as the biggest cache entry.
5. Transferred `config.yaml` to localhost with `scp` (triggered SSH first-time fingerprint prompt — answered yes). Then `rsync -avP` twice: first run transferred the file, second run sent 0 bytes (file unchanged on remote).
