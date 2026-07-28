import json
from pathlib import Path
from typing import Dict, List, Any

class IndexLoader:
    def __init__(self, index_dir: str):
        self.index_dir = Path(index_dir)

    def load_all(self) -> Dict[str, Any]:
        result = {}
        for name in ['files', 'functions', 'classes', 'modules', 'imports', 'graph', 'summary']:
            file_path = self.index_dir / f"{name}.json"
            if file_path.exists():
                with open(file_path) as f:
                    result[name] = json.load(f)
        return result

    def load(self, name: str) -> Any:
        file_path = self.index_dir / f"{name}.json"
        if file_path.exists():
            with open(file_path) as f:
                return json.load(f)
        return None
