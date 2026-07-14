from pathlib import Path
import yaml

CONFIG_DIR = Path.home() / ".ados"

def load_workspace():
    workspace = CONFIG_DIR / "workspace.yaml"

    if not workspace.exists():
        raise FileNotFoundError(workspace)

    with open(workspace,"r",encoding="utf-8") as f:
        return yaml.safe_load(f)
