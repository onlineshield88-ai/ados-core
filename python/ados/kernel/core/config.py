from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[3]

def load_yaml(path):
    p=ROOT/path
    if not p.exists():
        return {}
    with open(p,"r") as f:
        return yaml.safe_load(f) or {}
