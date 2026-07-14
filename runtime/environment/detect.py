#!/usr/bin/env python3

import os
import platform

print("="*60)
print("ADOS ENVIRONMENT")
print("="*60)

print("OS :", platform.system())
print("Release :", platform.release())
print("Machine :", platform.machine())

if os.path.exists("/data/data/com.termux"):
    print("Platform : TERMUX")
else:
    print("Platform : STANDARD")

print("="*60)
