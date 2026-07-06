#!/data/data/com.termux/files/usr/bin/bash

set -e

echo ""
echo "========================================"
echo " ADOS Workspace Initialization"
echo "========================================"
echo ""

ROOT=$(git rev-parse --show-toplevel 2>/dev/null || true)

if [ -z "$ROOT" ]; then
    echo "[ERROR] Bukan repository Git."
    exit 1
fi

echo "[OK] Repository : $ROOT"

mkdir -p "$ROOT"/workspace
mkdir -p "$ROOT"/projects
mkdir -p "$ROOT"/logs
mkdir -p "$ROOT"/cache
mkdir -p "$ROOT"/tmp

echo "[OK] Workspace created."

echo ""
echo "Directory:"
echo "workspace/"
echo "projects/"
echo "logs/"
echo "cache/"
echo "tmp/"

echo ""
echo "Initialization Complete."
