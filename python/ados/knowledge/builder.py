from pathlib import Path
from typing import Dict, Any
from .scanner import ProjectScanner
from .function import FunctionIndex
from .class_index import ClassIndex
from .module_index import ModuleIndex
from .import_index import ImportIndex
from .graph import DependencyGraph
from .storage import KnowledgeStorage

class IndexBuilder:
    def __init__(self, root: str, index_dir: str):
        self.root = root
        self.index_dir = index_dir
        self.scanner = ProjectScanner(root)
        self.function_index = FunctionIndex()
        self.class_index = ClassIndex()
        self.module_index = ModuleIndex()
        self.import_index = ImportIndex()
        self.graph = DependencyGraph()
        self.storage = KnowledgeStorage(index_dir)

    def build(self) -> Dict[str, Any]:
        print("Scanning project...")
        files_info = self.scanner.scan()
        
        print("Indexing Python files...")
        for py_file in files_info['python']:
            content = self.scanner.read_file(py_file)
            if content:
                self.function_index.index_file(py_file, content)
                self.class_index.index_file(py_file, content)
                self.module_index.index_file(py_file, content)
                self.import_index.index_file(py_file, content)

        self.graph.build_from_imports(self.import_index.to_dict())

        print("Saving indices...")
        self.storage.save('files', files_info)
        self.storage.save('functions', self.function_index.to_dict())
        self.storage.save('classes', self.class_index.to_dict())
        self.storage.save('modules', self.module_index.to_dict())
        self.storage.save('imports', self.import_index.to_dict())
        self.storage.save('graph', self.graph.to_dict())

        summary = {
            'python_files': len(files_info['python']),
            'doc_files': len(files_info['docs']),
            'config_files': len(files_info['config']),
            'total_functions': len(self.function_index.functions),
            'total_classes': len(self.class_index.classes),
            'total_modules': len(self.module_index.modules),
            'total_imports': len(self.import_index.imports)
        }
        self.storage.save('summary', summary)

        return summary
