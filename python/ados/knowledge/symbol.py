import ast
from typing import Optional, List, Dict
from .types import Symbol, SymbolType, FunctionDef, ClassDef

class SymbolExtractor:
    def __init__(self, file: str, content: str):
        self.file = file
        self.content = content
        self.tree = None
        self.symbols: List[Symbol] = []
        try:
            self.tree = ast.parse(content)
        except:
            pass

    def extract(self) -> List[Symbol]:
        if not self.tree:
            return []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                self._extract_function(node)
            elif isinstance(node, ast.AsyncFunctionDef):
                self._extract_async_function(node)
            elif isinstance(node, ast.ClassDef):
                self._extract_class(node)
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                self._extract_import(node)
        return self.symbols

    def _extract_function(self, node):
        docstring = ast.get_docstring(node)
        args = [arg.arg for arg in node.args.args]
        return_annotation = None
        if node.returns:
            return_annotation = ast.unparse(node.returns)
        decorators = [ast.unparse(d) for d in node.decorator_list]
        
        sym = Symbol(
            type=SymbolType.FUNCTION,
            name=node.name,
            file=self.file,
            line=node.lineno,
            docstring=docstring,
            metadata={
                'args': args,
                'return_annotation': return_annotation,
                'decorators': decorators,
                'is_async': False
            }
        )
        self.symbols.append(sym)

    def _extract_async_function(self, node):
        docstring = ast.get_docstring(node)
        args = [arg.arg for arg in node.args.args]
        return_annotation = None
        if node.returns:
            return_annotation = ast.unparse(node.returns)
        decorators = [ast.unparse(d) for d in node.decorator_list]
        
        sym = Symbol(
            type=SymbolType.ASYNC_FUNCTION,
            name=node.name,
            file=self.file,
            line=node.lineno,
            docstring=docstring,
            metadata={
                'args': args,
                'return_annotation': return_annotation,
                'decorators': decorators,
                'is_async': True
            }
        )
        self.symbols.append(sym)

    def _extract_class(self, node):
        docstring = ast.get_docstring(node)
        bases = [ast.unparse(b) for b in node.bases]
        decorators = [ast.unparse(d) for d in node.decorator_list]
        methods = []
        
        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                methods.append(item.name)
        
        sym = Symbol(
            type=SymbolType.CLASS,
            name=node.name,
            file=self.file,
            line=node.lineno,
            docstring=docstring,
            metadata={
                'bases': bases,
                'decorators': decorators,
                'methods': methods
            }
        )
        self.symbols.append(sym)

    def _extract_import(self, node):
        if isinstance(node, ast.Import):
            sym = Symbol(
                type=SymbolType.IMPORT,
                name=', '.join([alias.name for alias in node.names]),
                file=self.file,
                line=node.lineno,
                metadata={
                    'names': [(alias.name, alias.asname) for alias in node.names]
                }
            )
        else:
            module = node.module or ''
            sym = Symbol(
                type=SymbolType.IMPORT_FROM,
                name=f"from {module} import ...",
                file=self.file,
                line=node.lineno,
                metadata={
                    'module': module,
                    'names': [(alias.name, alias.asname) for alias in node.names]
                }
            )
        self.symbols.append(sym)
