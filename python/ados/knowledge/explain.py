from typing import Dict, Any, Optional
from .loader import IndexLoader

class SymbolExplainer:
    def __init__(self, index_loader: IndexLoader):
        self.loader = index_loader
        self.data = index_loader.load_all()

    def explain_module(self, module_name: str) -> Optional[Dict[str, Any]]:
        modules = self.data.get('modules', [])
        for mod in modules:
            if mod.get('name') == module_name:
                return mod
        return None

    def explain_class(self, class_name: str) -> Optional[Dict[str, Any]]:
        classes = self.data.get('classes', [])
        for cls in classes:
            if cls.get('name') == class_name:
                return cls
        return None

    def explain_function(self, function_name: str) -> Optional[Dict[str, Any]]:
        functions = self.data.get('functions', [])
        for func in functions:
            if func.get('name') == function_name:
                return func
        return None
