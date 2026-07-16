#!/data/data/com.termux/files/usr/bin/bash
set -e

python3 <<'PY'
from pathlib import Path

boot = Path("python/ados/kernel/bootstrap.py")

text = boot.read_text()

start = text.find("from ados.reasoning import (")
end = text.rfind("return k")

if start != -1 and end != -1:
    text = text[:start] + text[end:]

insert = '''
    from ados.reasoning import (
        ComplexityAnalyzer,
        MaintainabilityAnalyzer,
        DeadCodeDetector,
        UnusedImportDetector,
        CircularDependencyDetector,
    )

    k.memory.put(
        "complexity_summary",
        ComplexityAnalyzer(k).summary()
    )

    k.memory.put(
        "maintainability_summary",
        MaintainabilityAnalyzer(k).summary()
    )

    k.memory.put(
        "deadcode_summary",
        DeadCodeDetector(k).summary()
    )

    k.memory.put(
        "unused_imports_summary",
        UnusedImportDetector(k).summary()
    )

    k.memory.put(
        "cycle_summary",
        CircularDependencyDetector(k).summary()
    )

'''

idx = text.rfind("return k")

text = text[:idx] + insert + text[idx:]

boot.write_text(text)

print("bootstrap repaired")
PY
