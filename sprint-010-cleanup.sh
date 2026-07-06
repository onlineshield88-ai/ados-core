#!/data/data/com.termux/files/usr/bin/bash

set -e

ROOT="$(git rev-parse --show-toplevel)"

echo "====================================="
echo " ADOS Sprint-010 Cleanup"
echo "====================================="

cd "$ROOT"

# ------------------------------------------------------------------
# 1. Hapus file version.sh yang salah lokasi
# ------------------------------------------------------------------

if [ -f version.sh ]; then
    echo "[FIX] Removing root version.sh"
    rm version.sh
fi

# ------------------------------------------------------------------
# 2. Hapus folder docs/decisions lama
# ------------------------------------------------------------------

if [ -d docs/decisions ]; then
    echo "[FIX] Removing docs/decisions"
    rm -rf docs/decisions
fi

# ------------------------------------------------------------------
# 3. Pastikan folder runtime lengkap
# ------------------------------------------------------------------

mkdir -p core/runtime
mkdir -p core/runtime/system
mkdir -p core/runtime/config
mkdir -p core/runtime/services

# ------------------------------------------------------------------
# 4. Runtime Banner
# ------------------------------------------------------------------

cat > core/runtime/banner.sh <<'EOT'
#!/data/data/com.termux/files/usr/bin/bash

runtime_banner() {

VERSION=$(cat VERSION)

echo
echo "====================================="
echo " ADOS Development Operating System"
echo "====================================="
echo "Version : $VERSION"
echo

}
EOT

# ------------------------------------------------------------------
# 5. Runtime Git
# ------------------------------------------------------------------

cat > core/runtime/git.sh <<'EOT'
#!/data/data/com.termux/files/usr/bin/bash

runtime_git_root() {

git rev-parse --show-toplevel

}

runtime_is_git() {

git rev-parse --show-toplevel >/dev/null 2>&1

}
EOT

# ------------------------------------------------------------------
# 6. Runtime Filesystem
# ------------------------------------------------------------------

cat > core/runtime/filesystem.sh <<'EOT'
#!/data/data/com.termux/files/usr/bin/bash

runtime_workspace() {

mkdir -p workspace
mkdir -p projects
mkdir -p cache
mkdir -p logs
mkdir -p tmp

}
EOT

# ------------------------------------------------------------------
# 7. Runtime Loader
# ------------------------------------------------------------------

cat > core/runtime/runtime.sh <<'EOT'
#!/data/data/com.termux/files/usr/bin/bash

BASE="$(git rev-parse --show-toplevel)"

source "$BASE/core/runtime/banner.sh"
source "$BASE/core/runtime/git.sh"
source "$BASE/core/runtime/filesystem.sh"
EOT

chmod +x core/runtime/*.sh

echo
echo "Cleanup Complete."
echo
echo "Repository Status:"
echo
find core/runtime -maxdepth 1 -type f | sort

