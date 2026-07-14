#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 6.2"
echo " Repository Analyzer"
echo "======================================"

mkdir -p \
external/cache \
knowledge/analysis \
python/ados/research

####################################################
cat > python/ados/research/analyze.py <<'PY'
#!/usr/bin/env python3

from pathlib import Path
import subprocess
import shutil
import yaml
import os
import sys

if len(sys.argv)<2:
    print("usage:")
    print("python analyze.py https://github.com/owner/repo")
    raise SystemExit

url=sys.argv[1]

name=url.rstrip("/").split("/")[-1]

cache=Path("external/cache")/name

if cache.exists():
    shutil.rmtree(cache)

print("Cloning...")
subprocess.run(
    ["git","clone","--depth","1",url,str(cache)],
    check=True
)

keywords={
"cli":[
"click",
"argparse",
"typer",
"cobra",
"fire"
],
"agent":[
"agent",
"agents"
],
"plugin":[
"plugin",
"plugins"
],
"prompt":[
"prompt",
"prompts"
],
"memory":[
"memory",
"vector",
"embedding"
],
"runtime":[
"runtime",
"engine"
]
}

report={
"name":name,
"url":url,
"files":0,
"directories":0
}

hits={}

for k in keywords:
    hits[k]=[]

for root,dirs,files in os.walk(cache):

    report["directories"]+=1
    report["files"]+=len(files)

    low=root.lower()

    for k in keywords:

        if k in low:
            hits[k].append(root)

        for f in files:
            if any(x in f.lower() for x in keywords[k]):
                hits[k].append(str(Path(root)/f))

report["components"]=hits

out=Path("knowledge/analysis")
out.mkdir(exist_ok=True)

yaml.safe_dump(
    report,
    open(out/f"{name}.yaml","w"),
    sort_keys=False
)

with open(out/f"{name}.md","w") as f:

    f.write(f"# {name}\n\n")

    f.write(f"Repository : {url}\n\n")

    f.write(f"Files : {report['files']}\n")
    f.write(f"Directories : {report['directories']}\n\n")

    for k,v in hits.items():

        f.write(f"## {k}\n")

        if not v:
            f.write("- none\n")
        else:
            for i in sorted(set(v)):
                f.write(f"- {i}\n")

        f.write("\n")

print()
print("Analysis Complete")
print(out/f"{name}.yaml")
print(out/f"{name}.md")
PY

chmod +x python/ados/research/analyze.py

####################################################

cat > scripts/repo-analyze.sh <<'SH'
#!/usr/bin/env bash

python3 python/ados/research/analyze.py "$1"
SH

chmod +x scripts/repo-analyze.sh

echo
echo "DONE"
echo
echo "./scripts/repo-analyze.sh https://github.com/anthropics/claude-code"
