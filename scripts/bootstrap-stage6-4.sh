#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 6.4"
echo " Architecture Graph Builder"
echo "======================================"

mkdir -p \
knowledge/graphs \
python/ados/research

########################################

cat > python/ados/research/graph.py <<'PY'
from pathlib import Path
import yaml

ROOT=Path("knowledge/extracted")
OUT=Path("knowledge/graphs")
OUT.mkdir(exist_ok=True)

GROUPS={

"plugin":[
"plugins",
"commands",
"hooks",
"skills"
],

"agent":[
"agents",
"prompt"
],

"runtime":[
"runtime",
"workflow",
"config"
],

"memory":[
"memory"
],

"mcp":[
"mcp"
]

}

for f in ROOT.glob("*.yaml"):

    d=yaml.safe_load(f.read_text())

    graph={}

    for g,items in GROUPS.items():

        graph[g]={}

        total=0

        for item in items:

            value=len(d.get(item,[]))

            graph[g][item]=value
            total+=value

        graph[g]["total"]=total

    with open(OUT/f.name,"w") as fp:
        yaml.dump(graph,fp,sort_keys=False)

    print(f.stem)
PY

########################################

cat > scripts/build-graph.sh <<'SH'
#!/usr/bin/env bash

python3 python/ados/research/graph.py
SH

chmod +x scripts/build-graph.sh

echo
echo DONE
