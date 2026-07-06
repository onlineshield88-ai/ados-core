#!/data/data/com.termux/files/usr/bin/bash

BASE="$(git rev-parse --show-toplevel)"

source "$BASE/core/runtime/banner.sh"
source "$BASE/core/runtime/git.sh"
source "$BASE/core/runtime/filesystem.sh"
