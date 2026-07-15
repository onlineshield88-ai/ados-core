#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 7.0"
echo " Repository Validation Engine"
echo "======================================"

mkdir -p \
python/ados/validation \
knowledge/contracts \
knowledge/validation

########################################################

echo "[1] validator"

cat > python/ados/validation/validator.py <<'PY'
#!/usr/bin/env python3

from pathlib import Path
import yaml

ROOT=Path("knowledge")

required=[

    "analysis",
    "features",
    "architecture",
    "graphs"

]

print("="*70)
print("ADOS Repository Validation")
print("="*70)

ok=True

for folder in required:

    p=ROOT/folder

    if not p.exists():

        print(f"[FAIL] {folder} missing")

        ok=False

        continue

    files=list(p.glob("*.yaml"))

    print(f"{folder:15} {len(files):4} yaml")

if ok:
    print()
    print("STATUS : OK")
else:
    print()
    print("STATUS : FAILED")
PY

chmod +x python/ados/validation/validator.py

########################################################

echo "[2] launcher"

cat > scripts/validate.sh <<'SH'
#!/usr/bin/env bash

python3 python/ados/validation/validator.py
SH

chmod +x scripts/validate.sh

echo
echo "DONE"
