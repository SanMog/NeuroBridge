
***

# NeuroBridge v1.0 — Cognitive I/O Platform

> **"The fingers are the bottleneck of the mind. NeuroBridge expands that bandwidth."**

NeuroBridge is a minimalist, high-performance interface designed for systems architects, developers, and power users who need to bridge the gap between human thought and digital execution. It treats the OS as a fluid layer, replacing manual typing with low-latency neural transcription and high-speed auditory consumption.

## 🏛 Philosophy: Bandwidth Expansion

NeuroBridge is built on the premise that we can think and read much faster than we can type. 

*   **Fast Data Dump (Input):** Instant voice-to-cursor transcription allows you to offload complex thoughts without losing the state of "Flow."
*   **Fast Content Ingestion (Output):** High-speed (2x+) auditory consumption paired with visual reinforcement (Edge Reader) accelerates information processing.

---

## 🛡 Engineering & Privacy

NeuroBridge employs a hybrid architecture to balance absolute privacy with high-quality synthesis:

1.  **Sovereign Local Input (100% Secure):** Speech-to-Text (STT) is handled entirely on your local GPU using the `Faster-Whisper` pipeline. Your private technical discussions, passwords, and code logic never leave your machine. **Zero-telemetry.**
2.  **Edge-Neural Output:** Text-to-Speech (TTS) utilizes Microsoft’s advanced neural engines via the Edge API for superior phonetic clarity.
3.  **Zero-UI Interaction:** No buttons, no windows, no visual noise. The system lives in your system tray and is controlled via global hotkeys.

---

## 🚀 Key Features (v1.0)

### 🎙 Neural Voice Input (Hold `F4`)
*   **Engine:** `Faster-Whisper` (large-v3-turbo model).
*   **Mechanism:** Push-to-talk logic. Once you release the hotkey, the audio is processed and the text is instantly injected directly into your active cursor position (IDE, Terminal, Slack, etc.) via hardware-level simulation.
*   **Performance:** Highly optimized for NVIDIA GPUs (CUDA), achieving near-instantaneous inference.

### 🔊 High-Speed Auditory Bridge (Press `Ctrl + Q`)
*   **Mechanism:** Captures the current clipboard content, sanitizes metadata, and launches the Microsoft Edge Neural Reader.
*   **Workflow:** Allows for "Visual-Auditory Anchoring." You can listen to documentation at 2x speed in the background or follow the highlighted text in the HUD for maximum retention.

---

## ⚠️ Known Limitations (v1.0)

*   **Language Switching:** Language detection is performed on the entire text block before processing.
    *   If the text is predominantly Russian, the "Svetlana" voice is used.
    *   If the text is predominantly English, the "Jenny" voice is used.
*   **Phonetic Accuracy:** In mixed-language blocks (e.g., Russian text with English technical terms), the system will use the primary language's voice, which may result in accented pronunciation of foreign terms. Seamless on-the-fly voice switching is a roadmap feature for v2.0.

---

## 🛠 Technical Stack

*   **Runtime:** Python 3.12 (Optimized for Windows 10/11)
*   **ML Core:** `CTranslate2` / `Faster-Whisper` (GPU-bound)
*   **Acceleration:** `CUDA 12.x` / `cuDNN` (Requires NVIDIA RTX 30/40 series)
*   **I/O Logic:** Win32 API, `pystray` for state management, `edge-tts` synchronization.

---

## 📦 Installation & Deployment

### 1. Requirements
*   Windows 10/11
*   NVIDIA GPU with CUDA support (Recommended)
*   Python 3.10+

### 2. Setup
```bash
# Clone the repository
git clone https://github.com/SanMog/NeuroBridge.git
cd NeuroBridge

# Initialize environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Execution
The system includes a **Stealth Launcher (VBS)** to run modules as background services without persistent console windows.
*   Run `NeuroLauncher.vbs` to initialize the bridge.

---

## 🕹 Usage Protocol

| Command | Action | System Response |
| :--- | :--- | :--- |
| **Record** | Hold `F4` | Speech is typed instantly at cursor position. |
| **Listen** | `Ctrl + Q` | Clipboard is read aloud via Edge Neural HUD. |
| **Manage** | Right-Click Tray | Restart engines or exit system safely. |

---

**Architect:** Alexander Mogilin  
**Status:** 🟢 Operational | v1.1  
**License:** MIT  

*"The system lives where your focus is."*

***

