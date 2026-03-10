
***

# 🧠 NeuroBridge v1.0 — Cognitive I/O Platform

**NeuroBridge** — is a minimalist, high-performance interface designed for systems architects and power users to bridge the gap between human thought and digital execution. It expands the bandwidth of human-computer interaction by replacing manual typing with low-latency neural transcription.

![AI-Powered](https://img.shields.io/badge/AI--Powered-FF6F00?style=for-the-badge&logo=openai&logoColor=white)
![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NVIDIA CUDA](https://img.shields.io/badge/NVIDIA%20CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![License MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> *"The fingers are the bottleneck of the mind. NeuroBridge expands that bandwidth."*

---

### ✨ Key Features

*   🎙️ **Neural Voice Input:** Instant voice-to-cursor transcription using `Faster-Whisper` (large-v3-turbo).
*   🔊 **High-Speed Auditory Bridge:** Rapid content ingestion via Microsoft Edge Neural TTS at 2x+ speed.
*   🛡️ **Privacy First:** 100% local voice processing on your GPU. Your technical thoughts never leave your machine.
*   ⚙️ **Zero-UI Interaction:** Operates as an invisible layer of the OS via global hotkeys. No windows, no clutter.

---

### 🏛 Philosophy: Bandwidth Expansion

NeuroBridge is built on the premise that we can think and read much faster than we can type.

*   **Fast Data Dump (Input):** Offload complex thoughts directly into your IDE/Terminal without breaking the state of "Flow".
*   **Rapid Ingestion (Output):** Consume documentation through high-fidelity neural voices while maintaining visual focus on the code.

---

### 🛡 Engineering & Privacy

NeuroBridge employs a hybrid architecture to balance absolute privacy with high-quality synthesis:

1.  **Sovereign Local Input (100% Secure):** Speech-to-Text (STT) is handled entirely on your local GPU. **Zero-telemetry.**
2.  **Edge-Neural Output:** Text-to-Speech (TTS) utilizes Microsoft’s advanced neural engines via the Edge API for superior phonetic clarity.
3.  **Zero-UI:** The system lives in your system tray and is controlled via global hotkeys.

---

### ⚠️ Known Limitations (v1.0)

*   **Language Switching:** Language detection is performed on the entire text block. Seamless on-the-fly switching is a roadmap feature for v2.0.
*   **Phonetic Accuracy:** In mixed-language blocks, the primary language's voice is used, which may result in accented pronunciation of foreign technical terms.

---

### 🛠 Technical Stack

*   **Runtime:** Python 3.12 (Optimized for Windows 10/11)
*   **ML Core:** CTranslate2 / Faster-Whisper (GPU-bound)
*   **Acceleration:** CUDA 12.x / cuDNN (Requires NVIDIA RTX 30/40 series)
*   **I/O Logic:** Win32 API, `pystray` for state management, `edge-tts` synchronization.

---

### 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/SanMog/NeuroBridge.git
    cd NeuroBridge
    ```

2.  **Initialize environment:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Execution:**
    Run `NeuroLauncher.vbs` to initialize the bridge as a background service.

---

### 🕹 Usage Protocol

| Command | Action | System Response |
| :--- | :--- | :--- |
| **Record** | Hold `F4` | Speech is typed instantly at cursor position. |
| **Listen** | `Ctrl + Q` | Clipboard is read aloud via Edge Neural HUD. |
| **Manage** | Right-Click Tray | Restart engines or exit system safely. |

---

**Architect:** SanMog  
**Status:** 🟢 Operational | v1.1  
**License:** MIT  

*"The system lives where your focus is."*

***

