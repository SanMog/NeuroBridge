
***

# 🧠 NeuroBridge (Cognitive Layer)

**NeuroBridge** — is a high-bandwidth, minimalist interface designed for Systems Architects and Developers. It eliminates the cognitive friction of manual typing by decoupling input/output streams and leveraging local GPU acceleration.

![AI-Powered](https://img.shields.io/badge/AI--Powered-FF6F00?style=for-the-badge&logo=openai&logoColor=white)
![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NVIDIA CUDA](https://img.shields.io/badge/NVIDIA%20CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![License MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> *"The fingers are the bottleneck of the mind. NeuroBridge expands that bandwidth."*

---

## ✨ Key Features

*   🎙️ **Neural Voice Input:** Instant voice-to-cursor transcription using `Faster-Whisper` (large-v3-turbo).
*   🔊 **High-Speed Auditory Bridge:** Rapid content ingestion via Microsoft Edge Neural TTS at 2x+ speed.
*   🛡️ **Privacy First:** 100% local voice processing on your GPU. Your technical thoughts never leave your machine.
*   ⚙️ **Zero-UI Interaction:** No windows, no buttons. Operates as an invisible layer of the OS via global hotkeys.
*   🚀 **Visual-Auditory Anchoring:** Parallel consumption of text through audio and Edge's visual "Heads-Up Display".

---

## 🏛 Philosophy: Bandwidth Expansion

NeuroBridge treats the Operating System as a fluid layer. It is built for those who think and read faster than they can type.

*   **Fast Data Dump:** Offload complex architectural thoughts directly into your IDE/Terminal without breaking the state of "Flow".
*   **Rapid Ingestion:** Consume documentation and articles through high-fidelity neural voices while maintaining visual focus.

---

## 🛠 Technical Stack

*   **Runtime:** Python 3.12 (Optimized for Windows 11)
*   **ML Core:** CTranslate2 / Faster-Whisper (GPU-bound)
*   **Acceleration:** CUDA 12.x / cuDNN (Optimized for NVIDIA RTX 30/40 series)
*   **OS Bridge:** Win32 API, `pystray` background state-machine.

---

## 🚀 Installation

### 1. Clone the repository:
```bash
git clone https://github.com/SanMog/NeuroBridge.git
cd NeuroBridge
```

### 2. Initialize environment:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Hardware Setup:
*   Ensure **NVIDIA CUDA Toolkit** is installed.
*   The system will automatically download the `large-v3-turbo` model on the first run.

---

## 🕹 Usage Protocol

| Command | Action | System Response |
| :--- | :--- | :--- |
| **Record** | Hold `F4` | Speech is typed instantly at cursor position. |
| **Listen** | `Ctrl + Q` | Clipboard content is read aloud in HUD mode. |
| **Manage** | Right-Click Tray | Restart engines or exit system safely. |

---

## 🎓 Professional Impact
NeuroBridge demonstrates architectural innovation in Human-Computer Interaction (HCI) by reducing task-switching latency and implementing secure, air-gapped transcription pipelines for sensitive engineering data.

**Architect:** Alexander Mogilin  
**Status:** 🟢 Operational | v1.1  
**License:** MIT

*"The system lives where your focus is."*

***
