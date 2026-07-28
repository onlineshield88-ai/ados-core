import json
from pathlib import Path
from uuid import uuid4

ROOT=Path.home()/".ados/sessions"

class Session:

    def __init__(self):

        ROOT.mkdir(parents=True,exist_ok=True)

        self.id=str(uuid4())

        self.path=ROOT/self.id

        self.path.mkdir(exist_ok=True)

        self.history=self.path/"history.json"

        if not self.history.exists():
            self.history.write_text("[]")

    def append(self,role,text):

        data=json.loads(self.history.read_text())

        data.append({

            "role":role,
            "text":text

        })

        self.history.write_text(
            json.dumps(data,indent=2)
        )

    def load(self):

        return json.loads(
            self.history.read_text()
        )
