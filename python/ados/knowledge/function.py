from typing import List, Dict, Any
from .parser import CodeParser
from .types import FunctionRecord

class FunctionIndex:
    def __init__(self):
        self.functions: List[Dict[str, Any]] = []

    def index_file(self, file: str, content: str):
        parser = CodeParser(file, content)
        funcs = parser.parse_functions()
        for func in funcs:
            self.functions.append({
                'key': func.key,
                'name': func.name,
                'module': func.module,
                'file': func.file,
                'line': func.line,
                'args': func.args,
                'return_annotation': func.return_annotation,
                'docstring': func.docstring,
                'decorators': func.decorators,
                'is_async': func.is_async,
                'parent_class': func.parent_class
            })

    def search(self, query: str) -> List[Dict[str, Any]]:
        results = []
        query_lower = query.lower()
        for func in self.functions:
            func_name = func.get('name', '').lower()
            func_key = func.get('key', '').lower()
            if query_lower in func_name or query_lower in func_key:
                results.append(func)
        return results

    def to_dict(self) -> List[Dict[str, Any]]:
        return self.functions
