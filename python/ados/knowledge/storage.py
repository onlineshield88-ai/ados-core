import json
from pathlib import Path
from typing import Any, Dict, List

class KnowledgeStorage:
    def __init__(self, index_dir: str):
        self.index_dir = Path(index_dir)
        self.index_dir.mkdir(parents=True, exist_ok=True)

    def save(self, name: str, data: Any):
        file_path = self.index_dir / f"{name}.json"
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)

    def load(self, name: str) -> Any:
        file_path = self.index_dir / f"{name}.json"
        if file_path.exists():
            with open(file_path) as f:
                return json.load(f)
        return None

    def exists(self, name: str) -> bool:
        return (self.index_dir / f"{name}.json").exists()
