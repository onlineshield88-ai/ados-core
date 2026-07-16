from .kernel import ADOSKernel


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
