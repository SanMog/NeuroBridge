
---

# ⌨️ NeuroBridge — A Zero-UI Cognitive Interface

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GPU](https://img.shields.io/badge/acceleration-CUDA-orange.svg)

**NeuroBridge** is a high-bandwidth, minimalist voice-to-logic interface engineered for Systems Architects and Senior Developers. By decoupling input/output streams and leveraging local GPU acceleration, it eliminates the cognitive friction of typing and manual context switching.

> *"The fingers are the bottleneck of the mind. NeuroBridge expands that bandwidth."*

---

## 🏛 The Philosophy of "Invisible" Interaction

Traditional AI interfaces force the user into a browser tab or a dedicated application window, breaking the state of **Flow**. **NeuroBridge** operates as an invisible layer of the operating system, living entirely in your system tray and your ears.

### 🛡 Core Engineering Pillars:
*   **Sovereign Local Compute:** Voice transcription is handled locally via `Faster-Whisper` running on a dedicated CUDA-accelerated pipeline. Your private technical thoughts never leave your local environment.
*   **Zero-UI Interaction:** Global hotkeys and minimalist system tray indicators replace traditional buttons and windows, reducing visual noise and mental load.
*   **Dual-Neural Synthesis:** An intelligent language detection engine switches between specific neural voices (Svetlana/Jenny) to ensure perfect phonetic clarity for multi-language technical environments (RU/EN).

---

## 🚀 Key Features

### 🎙 Neural Voice Input (F4)
*   **Engine:** Powered by `Faster-Whisper (large-v3-turbo)` for real-time, high-fidelity transcription.
*   **Logic:** Speech-to-Text conversion is coupled with an automatic hardware-level cursor insertion (Ctrl+V simulation).
*   **Workflow:** Hold **F4**, speak your thought, release. The text appears instantly at your cursor, whether you are in an IDE, terminal, or document.

### 🔊 Edge-Neural Output Bridge (Ctrl+Q)
*   **Mechanism:** Captures clipboard data, sanitizes digital noise (emojis, markup, metadata), and generates a clean-room HTML HUD (Heads-Up Display).
*   **Acoustics:** Leverages Microsoft’s advanced **Neural Online Voices** for a human-like auditory experience.
*   **Intelligent Switching:** Automatically detects language blocks to prevent "accented" reading, providing native-level pronunciation for both Russian and English.

---

## 🛠 Technical Stack

*   **Runtime:** Python 3.12 (Optimized for Windows 11)
*   **Core ML:** CTranslate2 / Faster-Whisper (GPU-bound)
*   **Acceleration:** CUDA 12.x / cuDNN (Optimized for NVIDIA RTX 30/40 series)
*   **Interface:** Win32 API, `pystray` for background state-machine, `edge-tts` synchronization.

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
The project includes a **Stealth Launcher** (VBS) to run both Input and Output modules as background services without persistent console windows.

*   Run **`NeuroLauncher.vbs`** to start the system.

---

## 🕹 Usage Protocol

| Command | Action | System Response |
| :--- | :--- | :--- |
| **Record** | `Hold F4` | Speech is typed instantly at cursor position. |
| **Listen** | `Ctrl + Q` | Clipboard content is read aloud in HUD mode. |
| **Manage** | `Right-Click Tray` | Restart engines or exit system safely. |

---

## 🎓 Professional Impact (O-1 Visa Context)

NeuroBridge is an **Original Contribution** to the field of Human-Computer Interaction (HCI). It demonstrates architectural innovation in reducing task-switching latency and implementing secure, air-gapped transcription pipelines for sensitive engineering data.

---

**Architect:** [Alexander Mogilin](https://github.com/SanMog)  
**Status:** 🟢 Operational | v1.1  
**License:** MIT

---
*"The system lives where your focus is."*

---
