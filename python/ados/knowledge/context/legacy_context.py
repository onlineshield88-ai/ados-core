from typing import Dict, Any, List
from .loader import IndexLoader

class ContextBuilder:
    def __init__(self, index_loader: IndexLoader):
        self.loader = index_loader
        self.data = index_loader.load_all()

    def build_context(self, symbol_name: str) -> Dict[str, Any]:
        context = {
            'symbol': symbol_name,
            'related': self._find_related(symbol_name),
            'imports': self._find_imports(symbol_name),
            'usages': self._find_usages(symbol_name)
        }
        return context

    def _find_related(self, symbol_name: str) -> List[Dict[str, Any]]:
        related = []
        classes = self.data.get('classes', [])
        for cls in classes:
            if symbol_name in cls.get('methods', []):
                related.append({'type': 'class', 'name': cls.get('name')})
        return related

    def _find_imports(self, symbol_name: str) -> List[Dict[str, Any]]:
        return self.data.get('imports', [])

    def _find_usages(self, symbol_name: str) -> List[Dict[str, Any]]:
        usages = []
        modules = self.data.get('modules', [])
        for mod in modules:
            if any(symbol_name in imp.get('module', '') for imp in mod.get('imports', [])):
                usages.append({'type': 'module', 'name': mod.get('name')})
        return usages
