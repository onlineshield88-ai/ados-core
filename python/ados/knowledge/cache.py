import json
from pathlib import Path
from typing import Any, Optional

class IndexCache:
    def __init__(self, cache_dir: str):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def get(self, key: str) -> Optional[Any]:
        cache_file = self.cache_dir / f"{key}.cache"
        if cache_file.exists():
            try:
                with open(cache_file) as f:
                    return json.load(f)
            except:
                return None
        return None

    def set(self, key: str, value: Any):
        cache_file = self.cache_dir / f"{key}.cache"
        with open(cache_file, 'w') as f:
            json.dump(value, f)

    def clear(self):
        for cache_file in self.cache_dir.glob("*.cache"):
            cache_file.unlink()
