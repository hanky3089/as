import sys

def readLines():
    for line in sys.stdin:
        line = line.strip()
        num = int(line)
        print(line)

readLines()