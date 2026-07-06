#!/data/data/com.termux/files/usr/bin/bash

ADOS_VERSION=$(cat VERSION)

runtime_banner() {
    echo ""
    echo "======================================"
    echo " ADOS Runtime"
    echo "======================================"
    echo "Version : $ADOS_VERSION"
    echo ""
}

runtime_check_git() {

    git rev-parse --show-toplevel >/dev/null 2>&1

}

runtime_root() {

    git rev-parse --show-toplevel

}
