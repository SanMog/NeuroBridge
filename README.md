# NeuroBridge

**A zero-UI, privacy-first voice interface for high-bandwidth thinkers.**  
Local GPU transcription and instant insertion. No cloud. No dashboards.

---

## Why NeuroBridge

Engineers and power users often hit a ceiling: **typing is too slow**. In flow state—debugging, designing, or drafting—the gap between thought and text becomes a bottleneck. NeuroBridge is an engineered interface that keeps you in flow: speak on a hotkey, get text at the cursor; copy text, hear it read aloud. All with **zero UI** (system tray only) and **zero cloud dependency** for transcription.

---

## Principles

| Principle | What it means |
|-----------|----------------|
| **Zero-UI** | No windows, no dialogs. System tray icons and global hotkeys only. |
| **Privacy (local GPU)** | Voice is transcribed on your machine with **Faster-Whisper**. No audio is sent to the cloud. |
| **High speed** | **large-v3-turbo** on CUDA for near-instant, high-quality transcription. |

---

## What it does

- **Voice input (F4)** — Hold F4, speak; release. Speech is transcribed locally and **pasted at the current cursor** (Ctrl+V). One tray icon.
- **Voice output (Ctrl+Q)** — Copies clipboard into a clean HTML view and opens it in Edge with **Read Aloud** (Neural Voices). Second tray icon.

Two independent processes, two tray icons. Input and output do not block each other.

---

## Requirements

- **Python** 3.10+
- **Windows** (system tray, hotkeys, Edge integration)
- **NVIDIA GPU** with CUDA (recommended for fast transcription)

---

## Quick start

```bash
git clone https://github.com/your-org/NeuroBridge.git
cd NeuroBridge
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Optional: copy `env.example` to `.env` and set `EDGE_PATH` if Edge is not in the default location.

**Run (two terminals or background one):**

```bash
# Terminal 1 — voice input (F4 = record → transcribe → paste)
python core/voice_input.py

# Terminal 2 — voice output (Ctrl+Q = read clipboard aloud)
python core/voice_output.py
```

You should see **two tray icons**: **NeuroBridge — Recording (F4)** and **NeuroBridge — Playback (Ctrl+Q)**.

---

## Hotkeys

| Action | Hotkey |
|--------|--------|
| Record voice (then paste at cursor) | **F4** (hold to record, release to transcribe) |
| Read clipboard aloud | **Ctrl+Q** |

---

## Project layout

```
NeuroBridge/
├── config.py              # Paths (logs/, temp/), optional EDGE_PATH from .env
├── core/
│   ├── voice_input.py     # F4 → Whisper → paste at cursor
│   └── voice_output.py    # Ctrl+Q → clipboard → Edge Read Aloud
├── logs/                  # voice_input.log, voice_output.log (created at run)
├── temp/                  # Temporary HTML for reader (created at run)
├── env.example            # Example .env (copy to .env)
└── requirements.txt
```

All paths (logs, temp) are defined in `config.py` using `Path(__file__).parent`.

---

## Configuration

- **Logs** — `config.LOGS_DIR` (default: `logs/`). All runtime log output goes here.
- **Temp** — `config.TEMP_DIR` (default: `temp/`). Used by the reader window.
- **Edge** — Set `EDGE_PATH` in `.env` if Edge is not installed in the default path.

---

## Tech stack

- **Transcription:** Faster-Whisper (CTranslate2), **large-v3-turbo**, CUDA.
- **I/O:** `sounddevice`, `pynput`, `keyboard`, `pyperclip`, `pystray`, Pillow.
- **Output:** Microsoft Edge, Read Aloud (Neural Voices), with automatic RU/EN language tags.

---

## License

MIT. Use and extend as you like.
