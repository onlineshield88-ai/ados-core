#!/usr/bin/env bash
set -e

echo "======================================"
echo " ADOS STAGE 7.4"
echo " Unified CLI Router"
echo "======================================"

mkdir -p python/ados/cli

########################################################
echo "[1] doctor cli"

cat > python/ados/cli/doctor.py <<'PY'
from ados.runtime.doctor import doctor

def run(args=None):
    doctor()
PY

########################################################
echo "[2] architecture cli"

cat > python/ados/cli/architecture.py <<'PY'
import subprocess

def run(args=None):
    subprocess.run(
        ["python3",
         "python/ados/intelligence/architecture.py"],
        check=False
    )
PY

########################################################
echo "[3] framework cli"

cat > python/ados/cli/framework.py <<'PY'
import subprocess

def run(args=None):
    subprocess.run(
        ["python3",
         "python/ados/intelligence/framework_detector.py"],
        check=False
    )
PY

########################################################
echo "[4] dependency cli"

cat > python/ados/cli/dependency.py <<'PY'
import subprocess

def run(args=None):
    subprocess.run(
        ["python3",
         "python/ados/intelligence/dependency_detector.py"],
        check=False
    )
PY

echo
echo DONE
