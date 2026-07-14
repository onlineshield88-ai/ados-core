#!/data/data/com.termux/files/usr/bin/bash

set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo
echo "ADOS Bootstrap"
echo

while read module
do

[ -z "$module" ] && continue

SCRIPT="$ROOT/install/modules/$module.sh"

if [ -f "$SCRIPT" ]; then

echo "[RUN] $module"

bash "$SCRIPT"

else

echo "[SKIP] $module"

fi

done < "$ROOT/install/manifest.conf"

echo
echo "Bootstrap Finished."
