#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 6.3"
echo " Repository Knowledge Extractor"
echo "======================================"

mkdir -p \
python/ados/research \
knowledge/extracted \
knowledge/components \
knowledge/architecture \
knowledge/plugins \
knowledge/agents

####################################################
echo "[1] extractor"

cat > python/ados/research/extract.py <<'PY'
from pathlib import Path
import yaml

ROOT=Path("external/cache")

KEYWORDS={

"plugins":"plugins",

"agents":"agents",

"commands":"commands",

"hooks":"hooks",

"skills":"skills",

"runtime":"runtime",

"prompt":"prompt",

"memory":"memory",

"workflow":"workflow",

"template":"template",

"mcp":"mcp",

"config":"config"

}

for repo in ROOT.iterdir():

    if not repo.is_dir():
        continue

    result={}

    for k in KEYWORDS:

        result[k]=[]

    for f in repo.rglob("*"):

        p=str(f)

        lower=p.lower()

        for k,v in KEYWORDS.items():

            if v in lower:

                result[k].append(p)

    out=Path("knowledge/extracted")

    out.mkdir(exist_ok=True)

    with open(out/f"{repo.name}.yaml","w") as fp:

        yaml.dump(result,fp,sort_keys=False)

    print(repo.name,"done")
PY

####################################################
echo "[2] summary"

cat > python/ados/research/summary.py <<'PY'
from pathlib import Path
import yaml

base=Path("knowledge/extracted")

for f in sorted(base.glob("*.yaml")):

    d=yaml.safe_load(f.read_text())

    print("="*60)

    print(f.stem)

    for k,v in d.items():

        print(f"{k:12}",len(v))
PY

####################################################
echo "[3] launcher"

cat > scripts/extract-knowledge.sh <<'SH'
#!/usr/bin/env bash

python3 python/ados/research/extract.py

echo

python3 python/ados/research/summary.py
SH

chmod +x scripts/extract-knowledge.sh

echo
echo "DONE"
