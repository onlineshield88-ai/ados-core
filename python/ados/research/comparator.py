from pathlib import Path
import yaml

GRAPH_DIR = Path("knowledge/graphs")
OUT = Path("knowledge/comparison")

OUT.mkdir(exist_ok=True)

rows=[]

for f in sorted(GRAPH_DIR.glob("*.yaml")):

    g=yaml.safe_load(f.read_text())

    row={

        "repository":f.stem,

        "plugin":g["plugin"]["total"],

        "agent":g["agent"]["total"],

        "runtime":g["runtime"]["total"],

        "memory":g["memory"]["total"],

        "mcp":g["mcp"]["total"]

    }

    row["total"]=sum([
        row["plugin"],
        row["agent"],
        row["runtime"],
        row["memory"],
        row["mcp"]
    ])

    rows.append(row)

rows.sort(key=lambda x:x["total"],reverse=True)

with open(OUT/"repositories.yaml","w") as fp:
    yaml.dump(rows,fp,sort_keys=False)

print("="*70)
print(f"{'Repository':20} {'Plugin':>8} {'Agent':>8} {'Runtime':>8} {'MCP':>6} {'Total':>8}")
print("="*70)

for r in rows:

    print(
        f"{r['repository']:20}"
        f"{r['plugin']:8}"
        f"{r['agent']:8}"
        f"{r['runtime']:8}"
        f"{r['mcp']:6}"
        f"{r['total']:8}"
    )
