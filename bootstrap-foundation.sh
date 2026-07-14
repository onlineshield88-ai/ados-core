#!/usr/bin/env bash

set -e

echo
echo "=============================================="
echo " ADOS FOUNDATION NORMALIZER"
echo "=============================================="
echo

if [ ! -d ".git" ]; then
    echo "ERROR: bukan root repository git"
    exit 1
fi

echo "[1/9] Membuat struktur folder..."

dirs=(
constitution
genome
world
contracts
knowledge
knowledge/raw
knowledge/facts
knowledge/patterns
knowledge/rules
knowledge/strategies
knowledge/wisdom
memory
handover
state
decision
execution
engine
runtime
audit
logs
docs
specs
scripts
tests
tools
config
install
external
external/repositories
external/templates
external/benchmarks
external/prompts
)

for d in "${dirs[@]}"
do
    mkdir -p "$d"
done

echo "[2/9] Membuat .gitkeep..."

find constitution genome world contracts knowledge memory handover state decision execution engine runtime audit logs docs specs external tests tools config -type d | while read dir
do
    touch "$dir/.gitkeep"
done

echo "[3/9] Memindahkan installer..."

if [ -f bootstrap-installer.sh ]; then
    mv bootstrap-installer.sh install/bootstrap-installer.sh
fi

echo "[4/9] Membuat README dasar..."

for dir in constitution genome world contracts knowledge memory handover state decision execution engine runtime audit docs specs external
do
if [ ! -f "$dir/README.md" ]; then
cat > "$dir/README.md" <<EOT
# $(basename "$dir")

Placeholder.
Akan diisi pada milestone berikutnya.
EOT
fi
done

echo "[5/9] Membuat context-loader..."

cat > scripts/context-loader.py <<'PY'
#!/usr/bin/env python3
from pathlib import Path

folders=[
"constitution",
"genome",
"world",
"contracts",
"knowledge",
"memory",
"handover",
"state",
"decision",
"execution",
"engine",
"runtime",
"docs",
"specs"
]

print("="*60)
print("ADOS CONTEXT")
print("="*60)

for f in folders:
    p=Path(f)
    if p.exists():
        print(f"[OK] {f}")
    else:
        print(f"[MISSING] {f}")
PY

chmod +x scripts/context-loader.py

echo "[6/9] Membuat repository scanner..."

cat > scripts/scan.py <<'PY'
#!/usr/bin/env python3
from pathlib import Path

required=[
"constitution",
"genome",
"world",
"contracts",
"knowledge",
"memory",
"handover",
"state",
"decision",
"execution",
"engine",
"runtime",
"docs",
"specs",
"scripts"
]

missing=[]

for r in required:
    if not Path(r).exists():
        missing.append(r)

print("="*60)

if missing:
    print("Missing:")
    for m in missing:
        print(" -",m)
else:
    print("Repository Foundation OK")

print("="*60)
PY

chmod +x scripts/scan.py

echo "[7/9] Membuat .gitignore..."

if [ ! -f .gitignore ]; then
cat > .gitignore <<'EOT'
__pycache__/
*.pyc
.env
.venv
.cache
dist/
build/
*.log
EOT
fi

echo "[8/9] Struktur repository"

find . -maxdepth 2 -type d | sort

echo
echo "[9/9] Selesai"

echo
echo "Jalankan:"
echo
echo "python3 scripts/scan.py"
echo
echo "python3 scripts/context-loader.py"
echo
echo "git status"
echo
