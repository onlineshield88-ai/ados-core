#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 13.5"
echo " Repository Knowledge Bootstrap"
echo "======================================"

mkdir -p python/ados/repository

cat > python/ados/repository/knowledge.py <<'PY'
from ados.workspace import WorkspaceScanner
from ados.repository import RepositoryAnalyzer
from ados.indexer import PythonIndexer
from ados.graph import DependencyGraph
from ados.reference import SymbolReferenceResolver


class RepositoryKnowledge:

    def __init__(self):

        self.workspace = {}
        self.repository = {}
        self.symbols = []
        self.dependencies = None
        self.references = None

    def build(self, root="."):

        scanner = WorkspaceScanner()
        analyzer = RepositoryAnalyzer()
        indexer = PythonIndexer()

        self.workspace = scanner.scan(root)

        self.repository = analyzer.analyze(root)

        self.symbols = indexer.index(root)

        dep = DependencyGraph()
        dep.build(root)
        self.dependencies = dep

        ref = SymbolReferenceResolver()
        ref.build(root)
        self.references = ref

        return self

    def summary(self):

        return {
            "root": self.workspace.get("root"),
            "files": self.repository.get("total_files"),
            "languages": self.repository.get("languages"),
            "symbols": len(self.symbols),
            "modules": self.dependencies.size(),
            "references": len(self.references.symbols()),
        }
PY

grep -q "RepositoryKnowledge" python/ados/repository/__init__.py 2>/dev/null || \
cat >> python/ados/repository/__init__.py <<'PY'
from .knowledge import RepositoryKnowledge
PY

echo
echo "[1] repository knowledge"
echo "[2] bootstrap"

echo
echo DONE
