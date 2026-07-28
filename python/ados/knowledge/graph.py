from typing import Dict, List, Set
import json

class DependencyGraph:
    def __init__(self):
        self.modules: Dict[str, Set[str]] = {}
        self.classes: Dict[str, Set[str]] = {}
        self.functions: Dict[str, Set[str]] = {}

    def add_module_dependency(self, from_module: str, to_module: str):
        if from_module not in self.modules:
            self.modules[from_module] = set()
        self.modules[from_module].add(to_module)

    def add_class_dependency(self, from_class: str, to_class: str):
        if from_class not in self.classes:
            self.classes[from_class] = set()
        self.classes[from_class].add(to_class)

    def add_function_dependency(self, from_func: str, to_func: str):
        if from_func not in self.functions:
            self.functions[from_func] = set()
        self.functions[from_func].add(to_func)

    def build_from_imports(self, imports: List[Dict]):
        for imp in imports:
            module = imp.get('module', '')
            file = imp.get('file', '')
            if module and file:
                file_module = file.replace('/', '.').replace('.py', '')
                self.add_module_dependency(file_module, module)

    def to_dict(self):
        return {
            'modules': {k: list(v) for k, v in self.modules.items()},
            'classes': {k: list(v) for k, v in self.classes.items()},
            'functions': {k: list(v) for k, v in self.functions.items()}
        }
