#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "======================================"
echo " ADOS STAGE 15.2"
echo " External Intelligence Integration"
echo "======================================"

mkdir -p python/ados/integrations

cat > python/ados/integrations/__init__.py <<'PY'
from .registry import IntegrationRegistry
PY

cat > python/ados/integrations/registry.py <<'PY'
import importlib

class IntegrationRegistry:

    MODULES = {
        "networkx": "networkx",
        "radon": "radon",
        "ruff": "ruff",
        "libcst": "libcst",
        "jedi": "jedi",
        "tree_sitter": "tree_sitter",
    }

    def status(self):

        result = {}

        for name,module in self.MODULES.items():

            try:
                importlib.import_module(module)
                result[name]="READY"

            except Exception:
                result[name]="MISSING"

        return result
PY

python3 -m pip install --upgrade pip

python3 -m pip install \
networkx \
radon \
ruff \
libcst \
jedi \
tree-sitter || true

echo
echo "Installed."
echo
