#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 6.6"
echo " Feature Detector"
echo "======================================"

mkdir -p \
python/ados/research \
knowledge/features

########################################################
echo "[1] feature detector"

cat > python/ados/research/features.py <<'PY'
from pathlib import Path
import yaml

GRAPH = Path("knowledge/graphs")
OUT = Path("knowledge/features")

OUT.mkdir(exist_ok=True)

FEATURE_RULES = {
    "Plugin System": ("plugin", 1),
    "Agent Framework": ("agent", 1),
    "Runtime Engine": ("runtime", 1),
    "Memory System": ("memory", 1),
    "MCP Support": ("mcp", 1),
}

for file in sorted(GRAPH.glob("*.yaml")):

    graph = yaml.safe_load(file.read_text())

    features = {}

    for feature, (section, minimum) in FEATURE_RULES.items():
        enabled = graph.get(section, {}).get("total", 0) >= minimum
        features[feature] = enabled

    with open(OUT / file.name, "w") as fp:
        yaml.dump(features, fp, sort_keys=False)

print("Feature detection complete.")
PY

########################################################
echo "[2] feature report"

cat > python/ados/research/report.py <<'PY'
from pathlib import Path
import yaml

BASE = Path("knowledge/features")

print("=" * 72)

header = (
    f"{'Repository':18}"
    f"{'Plugin':>9}"
    f"{'Agent':>9}"
    f"{'Runtime':>10}"
    f"{'Memory':>9}"
    f"{'MCP':>7}"
)

print(header)
print("=" * 72)

for f in sorted(BASE.glob("*.yaml")):

    d = yaml.safe_load(f.read_text())

    print(
        f"{f.stem:18}"
        f"{'YES' if d['Plugin System'] else '-':>9}"
        f"{'YES' if d['Agent Framework'] else '-':>9}"
        f"{'YES' if d['Runtime Engine'] else '-':>10}"
        f"{'YES' if d['Memory System'] else '-':>9}"
        f"{'YES' if d['MCP Support'] else '-':>7}"
    )
PY

########################################################
echo "[3] launcher"

cat > scripts/features.sh <<'SH'
#!/usr/bin/env bash

python3 python/ados/research/features.py

echo

python3 python/ados/research/report.py
SH

chmod +x scripts/features.sh

echo
echo "DONE"
