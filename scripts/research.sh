#!/usr/bin/env bash

echo
echo "Repositories"
echo

ls knowledge/repositories/*.yaml 2>/dev/null || true

echo

python3 python/ados/research/compare.py
