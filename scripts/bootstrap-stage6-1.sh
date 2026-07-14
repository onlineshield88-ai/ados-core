#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 6.1"
echo " Github Research Module"
echo "======================================"

mkdir -p \
python/ados/research \
python/ados/research/providers \
python/ados/research/models \
python/ados/research/utils

########################################
echo "[1] requirements"

grep -q requests python/requirements.txt || echo requests >> python/requirements.txt

pip install -r python/requirements.txt

########################################
echo "[2] __init__"

cat > python/ados/research/__init__.py <<'PY'
PY

########################################
echo "[3] github provider"

cat > python/ados/research/providers/github.py <<'PY'
import requests

class Github:

    API="https://api.github.com/repos"

    def repository(self,url):

        owner_repo="/".join(url.rstrip("/").split("/")[-2:])

        api=f"{self.API}/{owner_repo}"

        r=requests.get(api,timeout=20)

        r.raise_for_status()

        return r.json()
PY

########################################
echo "[4] model"

cat > python/ados/research/models/repository.py <<'PY'
from dataclasses import dataclass

@dataclass
class Repository:

    name:str

    full_name:str=""

    description:str=""

    language:str=""

    stars:int=0

    forks:int=0

    license:str=""

    topics:list=None
PY

########################################
echo "[5] CLI"

cat > python/ados/research/info.py <<'PY'
import sys

from providers.github import Github

url=sys.argv[1]

g=Github()

d=g.repository(url)

print("="*60)

print("Name :",d["full_name"])

print("Language :",d["language"])

print("Stars :",d["stargazers_count"])

print("Forks :",d["forks_count"])

print("License :",d["license"]["spdx_id"] if d["license"] else "None")

print("="*60)
PY

########################################
echo "[6] launcher"

cat > scripts/repo-info.sh <<'SH'
#!/usr/bin/env bash

cd python/ados/research

python info.py "$1"
SH

chmod +x scripts/repo-info.sh

echo
echo "DONE"
