#!/usr/bin/env bash
set -e

echo "========================================="
echo " ADOS STAGE 5 - RESEARCH ENGINE"
echo "========================================="

mkdir -p \
python/ados/research \
knowledge/repositories \
knowledge/research \
knowledge/comparisons \
knowledge/licenses \
knowledge/components \
knowledge/summaries \
external/cache \
external/index

############################################
echo "[1] research package"

cat > python/ados/research/__init__.py <<'PY'
PY

############################################
echo "[2] repository model"

cat > python/ados/research/model.py <<'PY'
from dataclasses import dataclass

@dataclass
class Repository:

    name:str
    url:str

    language:str=""
    stars:int=0

    architecture:int=0
    cli:int=0
    plugins:int=0
    memory:int=0
    testing:int=0
    docs:int=0

    total:int=0
PY

############################################
echo "[3] scoring"

cat > python/ados/research/scoring.py <<'PY'
def score(repo):

    total=(
        repo.architecture+
        repo.cli+
        repo.plugins+
        repo.memory+
        repo.testing+
        repo.docs
    )

    repo.total=total
    return total
PY

############################################
echo "[4] compare"

cat > python/ados/research/compare.py <<'PY'
import yaml
from pathlib import Path

base=Path("knowledge/repositories")

for f in sorted(base.glob("*.yaml")):
    d=yaml.safe_load(f.read_text())

    print("="*60)
    print(d.get("name"))
    print(d.get("repository"))
    print("Category :",d.get("category",""))
    print()
PY

############################################
echo "[5] github scanner"

cat > scripts/github-scan.sh <<'SH'
#!/usr/bin/env bash

mkdir -p knowledge/repositories

URL=$1

if [ -z "$URL" ]; then
    echo "usage:"
    echo "./scripts/github-scan.sh https://github.com/owner/repo"
    exit
fi

NAME=$(basename "$URL")

cat > knowledge/repositories/${NAME}.yaml <<EOF
name: ${NAME}
repository: ${URL}

status: pending

license: unknown

architecture: unknown

cli: unknown

plugin: unknown

memory: unknown

workflow: unknown

compare: pending
EOF

echo "registered ${NAME}"
SH

chmod +x scripts/github-scan.sh

############################################
echo "[6] research cli"

cat > scripts/research.sh <<'SH'
#!/usr/bin/env bash

echo
echo "Repositories"
echo

ls knowledge/repositories/*.yaml 2>/dev/null || true

echo

python3 python/ados/research/compare.py
SH

chmod +x scripts/research.sh

############################################
echo "[7] queue"

cat > knowledge/research/queue.yaml <<EOF
queue:

- https://github.com/anthropics/claude-code
- https://github.com/Moh4696/open-source-ai-goldmine
- https://github.com/Aider-AI/aider
- https://github.com/All-Hands-AI/OpenHands
- https://github.com/block/goose
- https://github.com/continuedev/continue
EOF

############################################
echo "[8] done"

echo
echo "Examples:"
echo

echo "./scripts/github-scan.sh https://github.com/anthropics/claude-code"

echo "./scripts/github-scan.sh https://github.com/block/goose"

echo "./scripts/research.sh"
