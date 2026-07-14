#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "====================================="
echo " ADOS STAGE-2 BOOTSTRAP"
echo "====================================="

mkdir -p \
engine/registry \
engine/manifests \
decision/registry \
decision/history \
runtime/context \
runtime/environment \
runtime/session \
state/history \
state/current \
contracts/ai \
contracts/modules \
audit/history \
audit/reports \
docs/rfc \
docs/adr \
docs/specifications \
specs/schema \
specs/templates \
config/default \
config/environments

#################################################

cat > engine/registry/engines.yaml <<EOF
version: 1

engines:

- knowledge
- decision
- execution
- runtime
- evolution
- truth
- reflection
- memory
- genome
- cost
- capability
- audit
- handover
EOF

#################################################

cat > contracts/ai/chatgpt.yaml <<EOF
name: ChatGPT

permissions:

- architecture
- audit
- planning

restrictions:

- cannot_merge_main
- cannot_delete_history
EOF

#################################################

cat > contracts/ai/claude.yaml <<EOF
name: Claude

permissions:

- implementation
- refactor
- testing

restrictions:

- cannot_change_genome
EOF

#################################################

cat > contracts/ai/gemini.yaml <<EOF
name: Gemini

permissions:

- research
- benchmarking

restrictions:

- readonly_repository
EOF

#################################################

cat > state/current/state.yaml <<EOF
version: 1

phase: M0

status: bootstrap

engine_status:

knowledge: inactive
decision: inactive
execution: inactive
runtime: inactive
EOF

#################################################

cat > specs/schema/knowledge.schema.yaml <<EOF
id:
title:
status:
confidence:
environment:
compatibility:
evidence:
history:
owner:
updated:
EOF

#################################################

cat > runtime/environment/detect.py <<'EOF'
#!/usr/bin/env python3

import os
import platform

print("="*60)
print("ADOS ENVIRONMENT")
print("="*60)

print("OS :", platform.system())
print("Release :", platform.release())
print("Machine :", platform.machine())

if os.path.exists("/data/data/com.termux"):
    print("Platform : TERMUX")
else:
    print("Platform : STANDARD")

print("="*60)
EOF

chmod +x runtime/environment/detect.py

#################################################

cat > scripts/doctor.py <<'EOF'
#!/usr/bin/env python3

from pathlib import Path

required = [
"constitution",
"genome",
"knowledge",
"engine",
"decision",
"runtime",
"contracts",
"docs",
"specs",
"python",
"install"
]

missing=[]

for i in required:
    if not Path(i).exists():
        missing.append(i)

print("="*60)

if missing:
    print("Missing")
    for m in missing:
        print("-",m)
else:
    print("Repository Healthy")

print("="*60)
EOF

chmod +x scripts/doctor.py

#################################################

cat > docs/rfc/RFC-0001.md <<EOF
# RFC-0001

Repository Constitution

Status: Draft
EOF

#################################################

cat > docs/adr/ADR-0001.md <<EOF
# ADR-0001

Initial Architecture

Status: Accepted
EOF

#################################################

cat > engine/manifests/core.yaml <<EOF
name: core

engines:

- knowledge
- decision
- runtime
- execution
EOF

#################################################

echo
echo "Running validation..."
echo

python3 runtime/environment/detect.py

python3 scripts/doctor.py

echo
echo "Stage-2 selesai."
