#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 13.2"
echo " Symbol Database"
echo "======================================"

mkdir -p python/ados/database

cat > python/ados/database/symbol_db.py <<'PY'
class SymbolDatabase:

    def __init__(self):
        self._symbols = []

    def load(self, symbols):
        self._symbols = list(symbols)

    def all(self):
        return list(self._symbols)

    def find_type(self, symbol_type):
        return [
            s for s in self._symbols
            if s["type"] == symbol_type
        ]

    def find_name(self, name):
        return [
            s for s in self._symbols
            if name.lower() in s["name"].lower()
        ]

    def count(self):
        return len(self._symbols)
PY

cat > python/ados/database/__init__.py <<'PY'
from .symbol_db import SymbolDatabase
PY

echo
echo "[1] symbol database"
echo "[2] exports"

echo
echo DONE
