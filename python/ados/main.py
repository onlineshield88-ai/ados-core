import argparse

from ados.runtime.doctor import doctor

parser=argparse.ArgumentParser()

parser.add_argument("command",nargs="?",default="doctor")

args=parser.parse_args()

if args.command=="doctor":
    doctor()
else:
    print("Unknown command")
