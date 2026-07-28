from typing import List, Dict, Any
from .parser import CodeParser
from .types import ImportRecord

class ImportIndex:
    def __init__(self):
        self.imports: List[Dict[str, Any]] = []

    def index_file(self, file: str, content: str):
        parser = CodeParser(file, content)
        module = parser.parse_module()
        if module:
            for imp in module.imports:
                self.imports.append({
                    'type': imp.get('type', 'import'),
                    'module': imp.get('module', ''),
                    'name': imp.get('name'),
                    'alias': imp.get('alias'),
                    'file': file
                })

    def search(self, query: str) -> List[Dict[str, Any]]:
        results = []
        query_lower = query.lower()
        for imp in self.imports:
            module = imp.get('module', '').lower()
            if query_lower in module:
                results.append(imp)
        return results

    def to_dict(self) -> List[Dict[str, Any]]:
        return self.imports
