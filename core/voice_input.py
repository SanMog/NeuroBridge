import os
import sys
import site
import threading
import sounddevice as sd
import numpy as np
import time
import pyperclip
from faster_whisper import WhisperModel
from pynput import keyboard
from PIL import Image, ImageDraw
import pystray
from pathlib import Path

# [ABSOLUTE PATH SETUP]
ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
sys.path.insert(0, str(ROOT))

# [PATH INTEGRITY] Import config.py
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config

LOG_FILE = config.LOGS_DIR / "voice_input.log"


def log(msg):
    """Write to console and logs/voice_input.log."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] [NeuroBridge] {msg}"
    print(line, flush=True)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


log("Starting NeuroBridge voice input...")
kb_controller = keyboard.Controller()

# NVIDIA CUDA paths (critical for GPU-accelerated Whisper)
try:
    venv_path = site.getsitepackages()[0]
    os.environ["PATH"] += os.pathsep + os.path.join(venv_path, "nvidia", "cublas", "bin")
    os.environ["PATH"] += os.pathsep + os.path.join(venv_path, "nvidia", "cudnn", "bin")
    log(f"NVIDIA paths configured from: {venv_path}")
except Exception as e:
    log(f"Warning: Could not configure NVIDIA paths: {e}")

MODEL_SIZE = "large-v3-turbo"
DEVICE = "cuda"
HOTKEY = keyboard.Key.f4
SAMPLE_RATE = 16000
log(f"Model: {MODEL_SIZE}, Device: {DEVICE}, Hotkey: F4")


class NeuralVoiceBridge:
    def __init__(self):
        log(f"Loading Whisper model: {MODEL_SIZE} on {DEVICE}...")
        self.model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type="float16")
        log("Model loaded.")
        self.is_recording = False
        self.recording_data = []
        self.running = True
        self.listener = None

    def transcribe_and_insert(self, audio_data):
        audio_np = np.frombuffer(b''.join(audio_data), dtype=np.int16).astype(np.float32) / 32768.0
        rms = np.sqrt(np.mean(audio_np ** 2))
        if rms < 0.005: return

        segments, _ = self.model.transcribe(audio_np, beam_size=5, initial_prompt="Технический текст.")
        text = "".join([s.text for s in segments]).strip()

        if text and len(text) > 1:
            old_clip = pyperclip.paste()
            pyperclip.copy(text + " ")
            time.sleep(0.05)
            with kb_controller.pressed(keyboard.Key.ctrl):
                kb_controller.press(keyboard.KeyCode.from_vk(86))
                kb_controller.release(keyboard.KeyCode.from_vk(86))
            threading.Timer(1.5, lambda: pyperclip.copy(old_clip)).start()

    def audio_callback(self, indata, frames, time_info, status):
        if self.is_recording:
            self.recording_data.append(indata.copy())

    def on_press(self, key):
        if key == HOTKEY and not self.is_recording:
            self.is_recording = True
            self.recording_data = []

    def on_release(self, key):
        if key == HOTKEY and self.is_recording:
            self.is_recording = False
            if self.recording_data:
                threading.Thread(target=self.transcribe_and_insert, args=(self.recording_data.copy(),)).start()

    def create_icon_image(self):
        image = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.ellipse((8, 8, 56, 56), fill=(0, 120, 215), outline=(255, 255, 255), width=2)
        return image

    def quit_action(self, icon):
        self.running = False
        self.listener.stop()
        icon.stop()
        os._exit(0)

    def run_tray(self):
        icon = pystray.Icon("NeuroBridgeInput", self.create_icon_image(), "NeuroBridge — Recording (F4)")
        icon.menu = pystray.Menu(pystray.MenuItem("Exit", self.quit_action))
        icon.run()

    def run(self):
        log("Starting keyboard listener...")
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        log("Creating system tray icon...")
        threading.Thread(target=self.run_tray, daemon=True).start()
        log("Ready. Press F4 to record voice input.")

        with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='int16', callback=self.audio_callback):
            while self.running:
                time.sleep(1)


if __name__ == "__main__":
    bridge = NeuralVoiceBridge()
    bridge.run()