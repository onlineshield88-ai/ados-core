from pathlib import Path


class SearchEngine:

    def __init__(self, root="."):
        self.root = Path(root)

    def search(self, keyword):

        results = []

        for file in self.root.rglob("*"):

            if not file.is_file():
                continue

            if ".git" in file.parts:
                continue

            try:
                lines = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).splitlines()
            except Exception:
                continue

            for lineno, line in enumerate(lines, start=1):

                if keyword.lower() in line.lower():

                    results.append({
                        "file": str(file.relative_to(self.root)),
                        "line": lineno,
                        "text": line.strip()
                    })

        return results


# ==========================================
# Backward compatibility
# ==========================================

SemanticSearch = SearchEngine
