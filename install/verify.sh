#!/data/data/com.termux/files/usr/bin/bash

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo
echo "VERIFY"

echo

tree "$ROOT/install"

echo

echo "Python"

python3 --version || true

echo

echo "Git"

git --version || true
