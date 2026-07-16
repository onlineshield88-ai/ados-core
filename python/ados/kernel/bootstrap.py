from .kernel import ADOSKernel
from ados.repository import RepositoryKnowledge
from ados.graph import ReverseDependencyGraph

_KERNEL = None


def kernel():

    global _KERNEL

    if _KERNEL is None:
        _KERNEL = ADOSKernel()

    return _KERNEL


def initialize(root="."):

    k = kernel()

    k.memory.put("status", "running")

    repo = RepositoryKnowledge().build(root)

    k.memory.put("workspace", repo.workspace)
    k.memory.put("repository", repo.repository)
    k.memory.put("symbols", repo.symbols)
    k.memory.put("dependency_graph", repo.dependencies)
    k.memory.put("reference_resolver", repo.references)

    reverse = ReverseDependencyGraph(
        repo.dependencies
    ).build()

    k.memory.put(
        "reverse_dependency_graph",
        reverse
    )

    


    from ados.reasoning import (
        ComplexityAnalyzer,
        MaintainabilityAnalyzer,
        DeadCodeDetector,
        UnusedImportDetector,
        CircularDependencyDetector,
    )

    k.memory.put(
        "complexity_summary",
        ComplexityAnalyzer(k).summary()
    )

    k.memory.put(
        "maintainability_summary",
        MaintainabilityAnalyzer(k).summary()
    )

    k.memory.put(
        "deadcode_summary",
        DeadCodeDetector(k).summary()
    )

    k.memory.put(
        "unused_imports_summary",
        UnusedImportDetector(k).summary()
    )

    k.memory.put(
        "cycle_summary",
        CircularDependencyDetector(k).summary()
    )

    return k


def shutdown():

    global _KERNEL
    _KERNEL = None
