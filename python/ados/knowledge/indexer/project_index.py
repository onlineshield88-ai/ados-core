import ast
import json
from pathlib import Path

class ProjectIndexer:

    def __init__(self, root="."):
        self.root=Path(root)

    def scan(self):

        files=[]

        for f in self.root.rglob("*.py"):

            try:

                tree=ast.parse(f.read_text())

            except Exception:
                continue

            classes=[]
            funcs=[]
            imports=[]

            for node in ast.walk(tree):

                if isinstance(node,ast.ClassDef):
                    classes.append(node.name)

                elif isinstance(node,ast.FunctionDef):
                    funcs.append(node.name)

                elif isinstance(node,ast.Import):
                    imports.extend(
                        n.name
                        for n in node.names
                    )

                elif isinstance(node,ast.ImportFrom):

                    if node.module:
                        imports.append(node.module)

            files.append({

                "path":str(f),
                "classes":sorted(set(classes)),
                "functions":sorted(set(funcs)),
                "imports":sorted(set(imports))
            })

        return files

    def save(self):

        out=Path(".ados")
        out.mkdir(exist_ok=True)

        target=out/"index.json"

        target.write_text(

            json.dumps(
                {
                    "files":self.scan()
                },
                indent=2
            )
        )

        print(target)

if __name__=="__main__":

    ProjectIndexer().save()
