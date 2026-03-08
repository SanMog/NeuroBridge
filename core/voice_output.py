import os
import re
import subprocess
import sys
import threading
import time
from pathlib import Path

import keyboard
import pyperclip
import pystray
from PIL import Image, ImageDraw
from pystray import MenuItem as item

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
sys.path.insert(0, str(ROOT))
import config

HOTKEY = "ctrl+q"
TEMP_HTML = config.TEMP_DIR / "neuro_read.html"
LOG_FILE = config.LOGS_DIR / "voice_output.log"


def log_msg(msg):
    """Write to console and logs/voice_output.log."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] [NeuroBridge] {msg}"
    print(line, flush=True)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


def get_edge_path():
    if config.EDGE_PATH and os.path.isfile(config.EDGE_PATH):
        return config.EDGE_PATH
    edge_default = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if os.path.isfile(edge_default):
        return edge_default
    return "msedge"


class NeuroVoiceOutput:
    def __init__(self):
        self.icon = None
        self.colors = {"idle": (103, 58, 183), "processing": (255, 193, 7), "error": (244, 67, 54)}

    def create_image(self, color):
        image = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
        dc = ImageDraw.Draw(image)
        dc.ellipse((4, 4, 60, 60), fill=color, outline=(220, 220, 220), width=4)
        return image

    def set_status(self, status):
        if self.icon:
            self.icon.icon = self.create_image(self.colors.get(status, self.colors["idle"]))

    def on_restart(self, icon, _):
        log_msg("Restarting...")
        icon.stop()
        script = Path(__file__).resolve()
        subprocess.Popen([sys.executable, str(script)], cwd=str(ROOT))
        os._exit(0)

    def on_exit(self, icon, _):
        log_msg("Exiting...")
        icon.stop()
        os._exit(0)

    def process_text_to_html(self, text):
        raw_paragraphs = text.split('\n')
        clean_html_chunks = []

        for p in raw_paragraphs:
            clean_p = re.sub(r'[^a-zA-Zа-яА-ЯёЁ0-9\s.,!?]', ' ', p)
            clean_p = " ".join(clean_p.split())
            if clean_p:
                lang = "ru-RU" if re.search(r"[а-яА-ЯёЁ]", clean_p) else "en-US"
                clean_html_chunks.append(f'<p lang="{lang}">{clean_p}</p>')

        return "\n".join(clean_html_chunks)

    def prepare_html(self, text):
        content_html = self.process_text_to_html(text)
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ background-color: #1e1e1e; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; 
                       font-size: 30px; padding: 50px; line-height: 1.6; margin: 0; word-wrap: break-word; }}
                p {{ margin-bottom: 25px; text-align: left; }}
                ::selection {{ background: #4a4a4a; color: #fff; }}
            </style>
            <title>NeuroBridge Reader</title>
        </head>
        <body>{content_html}</body>
        </html>
        """
        with open(TEMP_HTML, "w", encoding="utf-8") as f:
            f.write(html_content)

    def open_in_edge_and_read(self):
        try:
            raw_text = pyperclip.paste().strip()
            if not raw_text: return

            self.set_status("processing")
            self.prepare_html(raw_text)
            edge_path = get_edge_path()
            subprocess.Popen([edge_path, "--new-window", str(TEMP_HTML)])

            time.sleep(1.5)
            keyboard.press_and_release('ctrl+shift+u')

            self.set_status("idle")
        except Exception as e:
            log_msg(f"Error: {e}")
            self.set_status("error")
            time.sleep(2)
            self.set_status("idle")

    def trigger(self):
        threading.Thread(target=self.open_in_edge_and_read, daemon=True).start()

    def run(self):
        config.TEMP_DIR.mkdir(parents=True, exist_ok=True)
        keyboard.add_hotkey(HOTKEY, self.trigger)
        menu = pystray.Menu(item("Restart", self.on_restart), item("Exit", self.on_exit))
        self.icon = pystray.Icon(
            "NeuroBridgeOutput",
            self.create_image(self.colors["idle"]),
            "NeuroBridge — Playback (Ctrl+Q)",
            menu=menu,
        )
        log_msg("Ready. Press Ctrl+Q to read clipboard aloud.")
        self.icon.run()


if __name__ == "__main__":
    NeuroVoiceOutput().run()