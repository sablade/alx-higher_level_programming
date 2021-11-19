#!/usr/bin/python3
import sys
argc = len(sys.argv)
i = 1
argsum = 0
while (i >= 1 and i < argc):
    argsum += int(sys.argv[i])
    i += 1
print(argsum)
