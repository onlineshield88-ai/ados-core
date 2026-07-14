from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[3]
STATE=ROOT/"state/current/state.yaml"

class State:

    def load(self):
        if not STATE.exists():
            return {}

        return yaml.safe_load(STATE.read_text()) or {}

    def save(self,data):
        STATE.write_text(yaml.dump(data,sort_keys=False))
