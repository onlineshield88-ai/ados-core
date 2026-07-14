#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "======================================="
echo " ADOS STAGE 3 - PYTHON RUNTIME"
echo "======================================="

mkdir -p \
python/ados/core \
python/ados/runtime \
python/ados/engine \
python/ados/plugins \
python/ados/state \
python/ados/knowledge \
python/ados/contracts \
python/ados/decision \
python/ados/utils

########################################
echo "[1] __init__"

find python/ados -type d | while read d
do
touch "$d/__init__.py"
done

########################################
echo "[2] Config Loader"

cat > python/ados/core/config.py <<'PY'
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[3]

def load_yaml(path):
    p=ROOT/path
    if not p.exists():
        return {}
    with open(p,"r") as f:
        return yaml.safe_load(f) or {}
PY

########################################
echo "[3] State Manager"

cat > python/ados/state/manager.py <<'PY'
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[3]
STATE=ROOT/"state/current/state.yaml"

class State:

    def load(self):
        if not STATE.exists():
            return {}

        return yaml.safe_load(STATE.read_text()) or {}

    def save(self,data):
        STATE.write_text(yaml.dump(data,sort_keys=False))
PY

########################################
echo "[4] Knowledge Manager"

cat > python/ados/knowledge/manager.py <<'PY'
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]

class Knowledge:

    def folders(self):
        base=ROOT/"knowledge"

        return [x.name for x in base.iterdir() if x.is_dir()]
PY

########################################
echo "[5] Engine Loader"

cat > python/ados/engine/loader.py <<'PY'
import yaml
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]

REGISTRY=ROOT/"engine/registry/engines.yaml"

class EngineLoader:

    def load(self):

        if not REGISTRY.exists():
            return []

        data=yaml.safe_load(REGISTRY.read_text())

        return data.get("engines",[])
PY

########################################
echo "[6] Plugin Loader"

cat > python/ados/plugins/loader.py <<'PY'
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]

class PluginLoader:

    def discover(self):

        p=ROOT/"plugins"

        if not p.exists():
            return []

        return [x.name for x in p.iterdir()]
PY

########################################
echo "[7] Doctor"

cat > python/ados/runtime/doctor.py <<'PY'
from ados.engine.loader import EngineLoader
from ados.knowledge.manager import Knowledge

def doctor():

    print("="*60)

    print("Registered Engines")

    for e in EngineLoader().load():
        print(" -",e)

    print()

    print("Knowledge")

    for k in Knowledge().folders():
        print(" -",k)

    print("="*60)
PY

########################################
echo "[8] CLI"

cat > python/ados/main.py <<'PY'
import argparse

from ados.runtime.doctor import doctor

parser=argparse.ArgumentParser()

parser.add_argument("command",nargs="?",default="doctor")

args=parser.parse_args()

if args.command=="doctor":
    doctor()
else:
    print("Unknown command")
PY

########################################
echo "[9] requirements"

cat > python/requirements.txt <<EOF
pyyaml
rich
click
EOF

########################################

echo
echo "Installing"

pip install -r python/requirements.txt

echo
echo "Testing"

cd python

python -m ados.main doctor

cd ..

echo
echo "DONE"
