import subprocess
import sys

def run(cmd):
    print("\n" + "="*70)
    print("RUN :", " ".join(cmd))
    print("="*70)
    subprocess.run(cmd, check=True)

def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("pipeline <github-url>")
        return

    repo = sys.argv[1]

    steps = [
        ["./scripts/github-scan.sh", repo],
        ["./scripts/repo-analyze.sh", repo],
        ["./scripts/extract-knowledge.sh"],
        ["./scripts/build-graph.sh"],
        ["./scripts/features.sh"],
        ["./scripts/compare-repositories.sh"]
    ]

    for step in steps:
        run(step)

    print("\nPipeline completed successfully.")

if __name__ == "__main__":
    main()
