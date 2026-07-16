#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 13.6"
echo " Kernel Knowledge Integration"
echo "======================================"

cat > python/ados/kernel/bootstrap.py <<'PY'
from .kernel import ADOSKernel
from ados.repository import RepositoryKnowledge

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

    return k


def shutdown():

    global _KERNEL
    _KERNEL = None
PY

echo
echo "[1] kernel bootstrap updated"
echo "[2] repository knowledge integrated"

echo
echo DONE
