import ast
from pathlib import Path
from collections import defaultdict


class DependencyGraph:

    def __init__(self):
        self._graph = defaultdict(set)

    def build(self, root):

        self._graph.clear()

        root = Path(root)

        for file in root.rglob("*.py"):

            if ".git" in file.parts:
                continue

            try:
                tree = ast.parse(
                    file.read_text(encoding="utf-8")
                )
            except Exception:
                continue

            module = str(file.relative_to(root))

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):

                    for alias in node.names:
                        self._graph[module].add(alias.name)

                elif isinstance(node, ast.ImportFrom):

                    if node.module:
                        self._graph[module].add(node.module)

    def modules(self):
        return sorted(self._graph.keys())

    def imports(self, module):
        return sorted(self._graph.get(module, []))

    def size(self):
        return len(self._graph)
