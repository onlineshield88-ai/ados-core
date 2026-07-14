#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 7.1"
echo " Framework Intelligence"
echo "======================================"

mkdir -p \
python/ados/intelligence \
knowledge/frameworks

##################################################
echo "[1] framework detector"

cat > python/ados/intelligence/framework_detector.py <<'PY'
from pathlib import Path
import yaml

ROOT=Path("external/cache")
OUT=Path("knowledge/frameworks")
OUT.mkdir(exist_ok=True)

FRAMEWORKS={

"react":[
"package.json",
"react"
],

"nextjs":[
"next.config.js",
"next.config.ts"
],

"vue":[
"vue.config.js"
],

"angular":[
"angular.json"
],

"fastapi":[
"fastapi"
],

"flask":[
"flask"
],

"django":[
"django"
],

"laravel":[
"artisan"
],

"spring":[
"pom.xml"
],

"express":[
"express"
],

"node":[
"package.json"
],

"docker":[
"Dockerfile"
],

"kubernetes":[
"deployment.yaml"
],

"terraform":[
".tf"
]

}

for repo in ROOT.iterdir():

    if not repo.is_dir():
        continue

    found=[]

    for fw,patterns in FRAMEWORKS.items():

        hit=False

        for f in repo.rglob("*"):

            name=str(f.name).lower()

            if any(p.lower() in name for p in patterns):
                hit=True
                break

        if hit:
            found.append(fw)

    with open(OUT/f"{repo.name}.yaml","w") as fp:

        yaml.dump({
            "repository":repo.name,
            "frameworks":found
        },fp,sort_keys=False)

    print(repo.name,found)
PY

##################################################
echo "[2] launcher"

cat > scripts/frameworks.sh <<'SH'
#!/usr/bin/env bash
python3 python/ados/intelligence/framework_detector.py
SH

chmod +x scripts/frameworks.sh

echo
echo "DONE"
