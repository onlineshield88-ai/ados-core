#!/usr/bin/env python3

import sys

def banner():
    print("=" * 40)
    print("ADOS Python Runtime")
    print("Version : 0.2.0-alpha")
    print("=" * 40)

def main():
    banner()

    if len(sys.argv) == 1:
        print("Usage:")
        print("  ados workspace scan")
        return

    print("Arguments:", sys.argv[1:])

if __name__ == "__main__":
    main()
