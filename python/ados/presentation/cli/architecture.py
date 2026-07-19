import subprocess

def run(args=None):
    subprocess.run(
        ["python3",
         "python/ados/intelligence/architecture.py"],
        check=False
    )
