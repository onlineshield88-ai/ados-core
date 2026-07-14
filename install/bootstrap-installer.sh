#!/data/data/com.termux/files/usr/bin/bash

set -e

ROOT="$(git rev-parse --show-toplevel)"

echo
echo "========================================="
echo " ADOS Installer Bootstrap"
echo "========================================="
echo

mkdir -p "$ROOT/install/modules"

##########################################
# manifest
##########################################

cat > "$ROOT/install/manifest.conf" <<'MANIFEST'
001-foundation
002-python
003-workspace
004-registry
005-docs
006-tests
007-github
999-finalize
MANIFEST

##########################################
# bootstrap
##########################################

cat > "$ROOT/install/bootstrap.sh" <<'BOOT'
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
BOOT

##########################################
# verify
##########################################

cat > "$ROOT/install/verify.sh" <<'VERIFY'
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
VERIFY

##########################################
# modules
##########################################

for n in \
001-foundation \
002-python \
003-workspace \
004-registry \
005-docs \
006-tests \
007-github \
999-finalize
do

cat > "$ROOT/install/modules/$n.sh" <<MODULE
#!/data/data/com.termux/files/usr/bin/bash

echo "[OK] $n"

MODULE

chmod +x "$ROOT/install/modules/$n.sh"

done

chmod +x "$ROOT/install/bootstrap.sh"
chmod +x "$ROOT/install/verify.sh"

echo
echo "Installer Created."
echo

tree "$ROOT/install"

