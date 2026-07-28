from typing import List, Dict, Any
from .parser import CodeParser
from .types import ModuleRecord

class ModuleIndex:
    def __init__(self):
        self.modules: List[Dict[str, Any]] = []

    def index_file(self, file: str, content: str):
        parser = CodeParser(file, content)
        module = parser.parse_module()
        if module:
            self.modules.append({
                'name': module.name,
                'file': module.file,
                'imports': module.imports,
                'classes': module.classes,
                'functions': module.functions,
                'docstring': module.docstring
            })

    def search(self, query: str) -> List[Dict[str, Any]]:
        results = []
        query_lower = query.lower()
        for module in self.modules:
            module_name = module.get('name', '').lower()
            if query_lower in module_name:
                results.append(module)
        return results

    def to_dict(self) -> List[Dict[str, Any]]:
        return self.modules
