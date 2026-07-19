from ados.knowledge.workspace import WorkspaceScanner
from ados.knowledge.repository import RepositoryAnalyzer
from ados.knowledge.indexer import PythonIndexer
from ados.knowledge.graph import DependencyGraph
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
