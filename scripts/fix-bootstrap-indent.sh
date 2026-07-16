#!/data/data/com.termux/files/usr/bin/bash
set -e

python3 <<'PY'
from pathlib import Path

boot = Path("python/ados/kernel/bootstrap.py")

lines = boot.read_text().splitlines()

fixed = []

for line in lines:
    if line.strip() == "return k":
        fixed.append("    return k")
    else:
        fixed.append(line)

boot.write_text("\n".join(fixed) + "\n")

print("bootstrap indentation fixed")
PY
