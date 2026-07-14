#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 6.9"
echo " Knowledge Schema Normalizer"
echo "======================================"

mkdir -p \
python/ados/research \
knowledge/schema

########################################
echo "[1] schema"

cat > knowledge/schema/features.schema.yaml <<'EOF'
repository: string

plugin: bool
agent: bool
runtime: bool
memory: bool
mcp: bool

plugins: int
agents: int
commands: int
hooks: int
skills: int
workflow: int
template: int
config: int
EOF

########################################
echo "[2] normalizer"

cat > python/ados/research/normalize_features.py <<'EOF'
#!/usr/bin/env python3

from pathlib import Path
import yaml

FEATURES=Path("knowledge/features")

for f in FEATURES.glob("*.yaml"):

    lines=f.read_text().splitlines()

    data={}

    mapping={

        "Plugin System":"plugin",
        "Agent Framework":"agent",
        "Runtime Engine":"runtime",
        "Memory System":"memory",
        "MCP Support":"mcp"

    }

    for line in lines:

        if ":" not in line:
            continue

        k,v=line.split(":",1)

        k=k.strip()
        v=v.strip()

        if k in mapping:

            data[mapping[k]]=(
                v.lower()=="true"
            )

    defaults={

        "plugins":0,
        "agents":0,
        "commands":0,
        "hooks":0,
        "skills":0,
        "workflow":0,
        "template":0,
        "config":0

    }

    for k,v in defaults.items():
        data.setdefault(k,v)

    data["repository"]=f.stem

    with open(f,"w") as fp:
        yaml.dump(
            data,
            fp,
            sort_keys=False
        )

    print(f.stem,"normalized")
EOF

chmod +x python/ados/research/normalize_features.py

########################################
echo "[3] launcher"

cat > scripts/normalize-features.sh <<'EOF'
#!/usr/bin/env bash

python3 python/ados/research/normalize_features.py
EOF

chmod +x scripts/normalize-features.sh

echo
echo "DONE"
