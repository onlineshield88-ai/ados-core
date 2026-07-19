from pathlib import Path


class SourceIndexer:

    def __init__(self, root="."):
        self.root = Path(root)

    def build(self):

        files = []

        for f in self.root.rglob("*"):

            if not f.is_file():
                continue

            if ".git" in f.parts:
                continue

            files.append(
                str(f.relative_to(self.root))
            )

        return sorted(files)
