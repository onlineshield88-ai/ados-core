import yaml
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]

REGISTRY=ROOT/"engine/registry/engines.yaml"

class EngineLoader:

    def load(self):

        if not REGISTRY.exists():
            return []

        data=yaml.safe_load(REGISTRY.read_text())

        return data.get("engines",[])
