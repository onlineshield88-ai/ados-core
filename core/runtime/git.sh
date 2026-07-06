#!/data/data/com.termux/files/usr/bin/bash

runtime_git_root() {

git rev-parse --show-toplevel

}

runtime_is_git() {

git rev-parse --show-toplevel >/dev/null 2>&1

}
