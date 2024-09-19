#!/usr/bin/python3
import sys

argv = sys.argv[1:]
argc = len(argv)

if argc == 0:
    print(f"{argc} arguments.")
elif argc == 1:
    print(f"{argc} argument:")
else:
    print(f"{argc} arguments:")

for i, arg in enumerate(argv, 1):
    print(f"{i}: {arg}")
