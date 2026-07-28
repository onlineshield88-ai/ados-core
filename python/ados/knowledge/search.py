from typing import List, Dict, Any
from .loader import IndexLoader
from .function import FunctionIndex
from .class_index import ClassIndex
from .module_index import ModuleIndex
from .import_index import ImportIndex

class SymbolSearcher:
    def __init__(self, index_loader: IndexLoader):
        self.loader = index_loader
        self.data = index_loader.load_all()
        
        self.function_index = FunctionIndex()
        self.function_index.functions = self.data.get('functions', [])
        
        self.class_index = ClassIndex()
        self.class_index.classes = self.data.get('classes', [])
        
        self.module_index = ModuleIndex()
        self.module_index.modules = self.data.get('modules', [])
        
        self.import_index = ImportIndex()
        self.import_index.imports = self.data.get('imports', [])

    def search_symbol(self, query: str) -> Dict[str, List[Dict[str, Any]]]:
        return {
            'functions': self.function_index.search(query),
            'classes': self.class_index.search(query),
            'modules': self.module_index.search(query),
            'imports': self.import_index.search(query)
        }

    def search_by_type(self, symbol_type: str, query: str) -> List[Dict[str, Any]]:
        if symbol_type == 'function':
            return self.function_index.search(query)
        elif symbol_type == 'class':
            return self.class_index.search(query)
        elif symbol_type == 'module':
            return self.module_index.search(query)
        elif symbol_type == 'import':
            return self.import_index.search(query)
        return []
