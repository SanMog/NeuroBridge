"""
NeuroBridge — central config. All paths relative to project root (Path(__file__).parent).
"""
from pathlib import Path
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

ROOT_DIR = Path(__file__).resolve().parent
LOGS_DIR = ROOT_DIR / "logs"
TEMP_DIR = ROOT_DIR / "temp"

LOGS_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)

# Optional: override Edge executable path (for voice output)
EDGE_PATH = os.environ.get("EDGE_PATH", "").strip() or None
