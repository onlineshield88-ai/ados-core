from typing import List, Dict, Any
from .parser import CodeParser
from .types import ClassRecord

class ClassIndex:
    def __init__(self):
        self.classes: List[Dict[str, Any]] = []

    def index_file(self, file: str, content: str):
        parser = CodeParser(file, content)
        classes = parser.parse_classes()
        for cls in classes:
            self.classes.append({
                'key': cls.key,
                'name': cls.name,
                'module': cls.module,
                'file': cls.file,
                'line': cls.line,
                'bases': cls.bases,
                'methods': cls.methods,
                'docstring': cls.docstring,
                'decorators': cls.decorators
            })

    def search(self, query: str) -> List[Dict[str, Any]]:
        results = []
        query_lower = query.lower()
        for cls in self.classes:
            cls_name = cls.get('name', '').lower()
            cls_key = cls.get('key', '').lower()
            if query_lower in cls_name or query_lower in cls_key:
                results.append(cls)
        return results

    def to_dict(self) -> List[Dict[str, Any]]:
        return self.classes
