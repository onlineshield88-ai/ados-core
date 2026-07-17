#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "======================================"
echo " FIX STAGE 15.2 TERMUX"
echo "======================================"

pkg update -y

pkg install -y \
python \
clang \
rust \
git \
libxml2 \
libxslt

python3 -m ensurepip --default-pip >/dev/null 2>&1 || true

python3 -m pip install \
networkx \
radon \
ruff \
libcst \
jedi \
tree-sitter \
--break-system-packages

echo
echo "======================================"
echo "VERIFY"
echo "======================================"

PYTHONPATH=python python3 - <<'PY'
from pprint import pprint
from ados.integrations import IntegrationRegistry

pprint(IntegrationRegistry().status())
PY

echo
echo "DONE"
