#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 4 - KNOWLEDGE REGISTRY"
echo "======================================"

mkdir -p \
external/repositories \
external/research \
external/prompts \
external/specifications \
knowledge/external \
knowledge/research \
knowledge/references \
knowledge/index \
state/current

########################################
echo "[1] Claude Code Registry"

cat > external/repositories/claude-code.yaml <<YAML
name: Claude Code
repository: https://github.com/anthropics/claude-code
category: reference
status: tracked

areas:
  - cli
  - command-router
  - agent-runtime
  - prompt-system
  - plugins

import_policy:
  source_code: forbidden
  architecture: allowed
  ideas: allowed
  documentation: allowed

last_review: pending
YAML

########################################
echo "[2] AI Goldmine Registry"

cat > external/repositories/open-source-ai-goldmine.yaml <<YAML
name: Open Source AI Goldmine
repository: https://github.com/Moh4696/open-source-ai-goldmine

type: index

contains:
  - ai frameworks
  - coding agents
  - llm runtimes
  - research

policy:
  import_code: false
  use_as_catalog: true
YAML

########################################
echo "[3] External Index"

cat > knowledge/index/external.yaml <<YAML
repositories:

- claude-code
- open-source-ai-goldmine

status: active
YAML

########################################
echo "[4] Knowledge Manifest"

cat > knowledge/manifest.yaml <<YAML
knowledge:

 raw:
 facts:
 patterns:
 rules:
 strategies:
 wisdom:

external:

 repositories:
 research:
 documentation:

version: 2
YAML

########################################
echo "[5] Research Queue"

cat > state/current/research-queue.yaml <<YAML
queue:

- claude-code
- aider
- openhands
- continue
- goose
- opencode
YAML

########################################
echo "[6] Repository Catalog"

cat > docs/specifications/EXTERNAL-KNOWLEDGE.md <<DOC
# External Knowledge

Repository eksternal hanya digunakan sebagai:

- referensi
- benchmarking
- inspirasi arsitektur

Tidak digunakan sebagai sumber copy source code.

Semua implementasi ADOS wajib original.
DOC

########################################
echo "[7] Research Tool"

cat > scripts/research.py <<'PY'
#!/usr/bin/env python3

from pathlib import Path
import yaml

base=Path("external/repositories")

print("="*60)
print("Tracked External Repositories")
print("="*60)

for f in sorted(base.glob("*.yaml")):
    data=yaml.safe_load(f.read_text())

    print(data["name"])
    print(" repo :",data["repository"])
    print()
PY

chmod +x scripts/research.py

########################################
echo "[8] AI Registry"

mkdir -p contracts/ai

for ai in chatgpt claude gemini codex aider continue opencode goose
do
cat > contracts/ai/$ai.yaml <<DOC
name: $ai
role: pending
permissions: review
status: active
DOC
done

########################################
echo "[9] Done"

python3 scripts/research.py

echo
echo "Stage-4 Complete"
