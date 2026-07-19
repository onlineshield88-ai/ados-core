import subprocess

def run(args=None):
    subprocess.run(
        ["python3",
         "python/ados/intelligence/framework_detector.py"],
        check=False
    )
