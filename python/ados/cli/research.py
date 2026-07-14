import sys
import subprocess

COMMANDS = {
    "scan": "./scripts/github-scan.sh",
    "graph": "./scripts/build-graph.sh",
    "compare": "./scripts/compare-repositories.sh",
    "features": "./scripts/features.sh",
    "extract": "./scripts/extract-knowledge.sh",
}

def run():

    if len(sys.argv) < 2:
        print("Usage:")
        print("research scan <url>")
        print("research extract")
        print("research graph")
        print("research compare")
        print("research features")
        return

    cmd = sys.argv[1]

    if cmd == "scan":

        if len(sys.argv) < 3:
            print("Repository URL required")
            return

        subprocess.run([COMMANDS["scan"], sys.argv[2]])
        return

    if cmd in COMMANDS:
        subprocess.run([COMMANDS[cmd]])
        return

    print("Unknown command")
