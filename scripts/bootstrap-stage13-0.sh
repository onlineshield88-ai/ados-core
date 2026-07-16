#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 13.0"
echo " Repository Intelligence"
echo "======================================"

mkdir -p python/ados/repository

cat > python/ados/repository/analyzer.py <<'PY'
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
PY

cat > python/ados/repository/__init__.py <<'PY'
from .analyzer import RepositoryAnalyzer
PY

echo
echo "[1] repository analyzer"
echo "[2] exports"

echo
echo DONE
