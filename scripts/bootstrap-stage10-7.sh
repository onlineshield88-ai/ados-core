#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 10.7"
echo " Kernel Bootstrap"
echo "======================================"

cat > python/ados/kernel/bootstrap.py <<'PY'
from ados.kernel import ADOSKernel


_KERNEL = None


def kernel():

    global _KERNEL

    if _KERNEL is None:
        _KERNEL = ADOSKernel()

    return _KERNEL


def initialize():

    k = kernel()

    k.memory.put("status", "running")

    return k


def shutdown():

    global _KERNEL

    _KERNEL = None
PY

echo
echo "[1] bootstrap"
echo "[2] singleton"

echo
echo DONE
