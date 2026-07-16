import ast
from pathlib import Path


class SymbolReferenceResolver:

    def __init__(self):
        self._symbols = {}
        self._calls = {}

    def build(self, root):

        root = Path(root)

        for file in root.rglob("*.py"):

            if ".git" in file.parts:
                continue

            try:
                tree = ast.parse(
                    file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )
                )
            except Exception:
                continue

            module = str(file.relative_to(root))

            for node in ast.walk(tree):

                if isinstance(node, ast.FunctionDef):

                    self._symbols.setdefault(
                        node.name,
                        set()
                    ).add(module)

                elif isinstance(node, ast.AsyncFunctionDef):

                    self._symbols.setdefault(
                        node.name,
                        set()
                    ).add(module)

                elif isinstance(node, ast.Call):

                    name = None

                    if isinstance(node.func, ast.Name):
                        name = node.func.id

                    elif isinstance(node.func, ast.Attribute):
                        name = node.func.attr

                    if name:

                        self._calls.setdefault(
                            name,
                            set()
                        ).add(module)

    def symbols(self):
        return sorted(self._symbols.keys())

    def callers(self, name):
        return sorted(self._calls.get(name, set()))

    def count(self):
        return len(self._symbols)
