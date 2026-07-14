from pathlib import Path
import yaml

ROOT=Path("knowledge/extracted")
OUT=Path("knowledge/graphs")
OUT.mkdir(exist_ok=True)

GROUPS={

"plugin":[
"plugins",
"commands",
"hooks",
"skills"
],

"agent":[
"agents",
"prompt"
],

"runtime":[
"runtime",
"workflow",
"config"
],

"memory":[
"memory"
],

"mcp":[
"mcp"
]

}

for f in ROOT.glob("*.yaml"):

    d=yaml.safe_load(f.read_text())

    graph={}

    for g,items in GROUPS.items():

        graph[g]={}

        total=0

        for item in items:

            value=len(d.get(item,[]))

            graph[g][item]=value
            total+=value

        graph[g]["total"]=total

    with open(OUT/f.name,"w") as fp:
        yaml.dump(graph,fp,sort_keys=False)

    print(f.stem)
