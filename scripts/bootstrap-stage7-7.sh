#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 7.7"
echo " Capability Registry"
echo "======================================"

mkdir -p python/ados/kernel

########################################

echo "[1] capability registry"

cat > python/ados/kernel/capability.py <<'PY'
CAPABILITIES = {}


def register(name, capability):

    CAPABILITIES.setdefault(name, set())
    CAPABILITIES[name].add(capability)


def unregister(name):

    CAPABILITIES.pop(name, None)


def get(name):

    return sorted(CAPABILITIES.get(name, []))


def providers(capability):

    result = []

    for provider, caps in CAPABILITIES.items():

        if capability in caps:
            result.append(provider)

    return sorted(result)


def dump():

    return {
        k: sorted(v)
        for k, v in CAPABILITIES.items()
    }
PY

########################################

echo "[2] capability bootstrap"

cat > python/ados/kernel/bootstrap.py <<'PY'
from ados.kernel.capability import register

register("ados","workspace")
register("ados","research")
register("ados","architecture")
register("ados","framework")
register("ados","dependency")
register("ados","knowledge")
register("ados","graph")
register("ados","comparison")
PY

echo
echo DONE
