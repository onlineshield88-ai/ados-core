from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]

class Knowledge:

    def folders(self):
        base=ROOT/"knowledge"

        return [x.name for x in base.iterdir() if x.is_dir()]
