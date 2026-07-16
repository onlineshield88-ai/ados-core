#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 14.1.1"
echo " Reverse Dependency Graph"
echo "======================================"

cat > python/ados/graph/reverse_dependency.py <<'PY'
class ReverseDependencyGraph:

    def __init__(self, dependency_graph):

        self.forward = dependency_graph
        self.reverse = {}

    def build(self):

        self.reverse = {}

        for module in self.forward.modules():

            self.reverse.setdefault(module, [])

        for module in self.forward.modules():

            try:
                imports = self.forward.imports(module)
            except Exception:
                imports = []

            for dep in imports:

                dep_file = dep.replace(".", "/") + ".py"

                for target in self.forward.modules():

                    if target.endswith(dep_file):

                        self.reverse.setdefault(target, [])

                        if module not in self.reverse[target]:
                            self.reverse[target].append(module)

        return self

    def imported_by(self, module):

        return sorted(
            self.reverse.get(module, [])
        )

    def modules(self):

        return sorted(
            self.reverse.keys()
        )

    def size(self):

        return len(self.reverse)
PY

grep -q "ReverseDependencyGraph" python/ados/graph/__init__.py 2>/dev/null || cat >> python/ados/graph/__init__.py <<'PY'
from .reverse_dependency import ReverseDependencyGraph
PY

python3 <<'PY'
from pathlib import Path

boot = Path("python/ados/kernel/bootstrap.py")

text = boot.read_text()

if "reverse_dependency_graph" not in text:

    text = text.replace(
        "from ados.repository import RepositoryKnowledge",
        "from ados.repository import RepositoryKnowledge\nfrom ados.graph import ReverseDependencyGraph"
    )

    text = text.replace(
        'k.memory.put("reference_resolver", repo.references)',
        '''k.memory.put("reference_resolver", repo.references)

    reverse = ReverseDependencyGraph(
        repo.dependencies
    ).build()

    k.memory.put(
        "reverse_dependency_graph",
        reverse
    )'''
    )

    boot.write_text(text)

print("bootstrap updated")
PY

echo
echo "[1] reverse dependency graph"
echo "[2] kernel integration"

echo
echo "DONE"

