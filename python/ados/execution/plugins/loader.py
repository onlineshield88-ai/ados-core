from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]

class PluginLoader:

    def discover(self):

        p=ROOT/"plugins"

        if not p.exists():
            return []

        return [x.name for x in p.iterdir()]
