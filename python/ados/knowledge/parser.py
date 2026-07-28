import ast
from typing import List, Dict, Any, Optional
from .types import FunctionRecord, ClassRecord, ModuleRecord, ImportRecord

class CodeParser:
    def __init__(self, file: str, content: str):
        self.file = file
        self.content = content
        self.module_name = file.replace('/', '.').replace('.py', '')
        self.tree = None
        try:
            self.tree = ast.parse(content)
        except:
            pass

    def parse_module(self) -> Optional[ModuleRecord]:
        if not self.tree:
            return None
        
        docstring = ast.get_docstring(self.tree)
        imports = []
        classes = []
        functions = []
        
        for node in self.tree.body:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append({
                        'type': 'import',
                        'module': alias.name,
                        'name': None,
                        'alias': alias.asname
                    })
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ''
                for alias in node.names:
                    imports.append({
                        'type': 'from',
                        'module': module,
                        'name': alias.name,
                        'alias': alias.asname
                    })
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)
            elif isinstance(node, ast.FunctionDef):
                functions.append(node.name)
            elif isinstance(node, ast.AsyncFunctionDef):
                functions.append(node.name)
        
        return ModuleRecord(
            name=self.module_name,
            file=self.file,
            imports=imports,
            classes=classes,
            functions=functions,
            docstring=docstring
        )

    def parse_functions(self) -> List[FunctionRecord]:
        if not self.tree:
            return []
        
        functions = []
        
        def extract_functions(nodes, parent_class=None):
            for node in nodes:
                if isinstance(node, ast.FunctionDef):
                    args = [arg.arg for arg in node.args.args]
                    return_annotation = None
                    if node.returns:
                        return_annotation = ast.unparse(node.returns)
                    
                    key = f"{self.module_name}.{parent_class}.{node.name}" if parent_class else f"{self.module_name}.{node.name}"
                    func = FunctionRecord(
                        key=key,
                        name=node.name,
                        module=self.module_name,
                        file=self.file,
                        line=node.lineno,
                        args=args,
                        return_annotation=return_annotation,
                        docstring=ast.get_docstring(node),
                        decorators=[ast.unparse(d) for d in node.decorator_list],
                        is_async=False,
                        parent_class=parent_class
                    )
                    functions.append(func)
                elif isinstance(node, ast.AsyncFunctionDef):
                    args = [arg.arg for arg in node.args.args]
                    return_annotation = None
                    if node.returns:
                        return_annotation = ast.unparse(node.returns)
                    
                    key = f"{self.module_name}.{parent_class}.{node.name}" if parent_class else f"{self.module_name}.{node.name}"
                    func = FunctionRecord(
                        key=key,
                        name=node.name,
                        module=self.module_name,
                        file=self.file,
                        line=node.lineno,
                        args=args,
                        return_annotation=return_annotation,
                        docstring=ast.get_docstring(node),
                        decorators=[ast.unparse(d) for d in node.decorator_list],
                        is_async=True,
                        parent_class=parent_class
                    )
                    functions.append(func)
                elif isinstance(node, ast.ClassDef):
                    extract_functions(node.body, parent_class=node.name)
        
        extract_functions(self.tree.body)
        return functions

    def parse_classes(self) -> List[ClassRecord]:
        if not self.tree:
            return []
        
        classes = []
        for node in self.tree.body:
            if isinstance(node, ast.ClassDef):
                bases = [ast.unparse(b) for b in node.bases]
                methods = []
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        methods.append(item.name)
                
                key = f"{self.module_name}.{node.name}"
                cls = ClassRecord(
                    key=key,
                    name=node.name,
                    module=self.module_name,
                    file=self.file,
                    line=node.lineno,
                    bases=bases,
                    methods=methods,
                    docstring=ast.get_docstring(node),
                    decorators=[ast.unparse(d) for d in node.decorator_list]
                )
                classes.append(cls)
        
        return classes
