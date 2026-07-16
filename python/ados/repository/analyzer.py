from pathlib import Path
from collections import Counter


class RepositoryAnalyzer:

    EXTENSIONS = {
        ".py": "Python",
        ".md": "Markdown",
        ".sh": "Shell",
        ".json": "JSON",
        ".yaml": "YAML",
        ".yml": "YAML",
        ".toml": "TOML",
        ".ini": "INI",
        ".txt": "Text",
        ".html": "HTML",
        ".css": "CSS",
        ".js": "JavaScript",
    }

    def analyze(self, root):

        root = Path(root)

        languages = Counter()

        files = []

        for f in root.rglob("*"):

            if ".git" in f.parts:
                continue

            if not f.is_file():
                continue

            files.append(str(f.relative_to(root)))

            ext = f.suffix.lower()

            languages[self.EXTENSIONS.get(ext, "Other")] += 1

        return {
            "total_files": len(files),
            "languages": dict(sorted(languages.items())),
            "files": files,
        }
