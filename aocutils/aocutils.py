import time
from multipledispatch import dispatch

def readFile(day: int, splitOn: str = "", isTest: bool = False, toList: bool = True) -> list[str]:
    res = []
    filename = f"day_{day:02}/day_{day:02}.txt" if not isTest else f"day_{day:02}/test.txt"
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if splitOn:
                line = line.split(splitOn)
            if toList:
                line = list(line)
            res.append(line)
    return res

def readFileWithNewline(day: int, splitOn: str = "", isTest: bool = False, toList: bool = True) -> list[str]:
    beforeNewline = []
    afterNewLine = []
    isAfterNewline = False
    filename = f"day_{day:02}/day_{day:02}.txt" if not isTest else f"day_{day:02}/test.txt"
    with open(filename, "r") as f:
        for line in f:
            if line == "\n":
                isAfterNewline = True
                continue

            line = line.strip()

            if splitOn:
                line = line.split(splitOn)
            if toList:
                line = list(line)

            if not isAfterNewline:
                beforeNewline.append(line)
            else:
                afterNewLine.append(line)
    return beforeNewline, afterNewLine

@dispatch(int, int, int, int, int, int)
def outOfBounds(i: int, j: int, iMin: int, jMin: int, iMax: int, jMax: int) -> bool:
    return i < iMin or i > iMax or j < jMin or j > jMax

@dispatch(int, int, int, int)
def outOfBounds(i: int, j: int, iMax: int, jMax: int) -> bool:
    return i < 0 or i > iMax or j < 0 or j > jMax

def printParts(part1, part2):
    print("Part 1: " + str(part1))
    print("Part 2: " + str(part2))

def timeFunction(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        res = func(*args, **kwargs)
        print(f"Time taken: {time.time() - startTime}")
        return res
    return wrapper

def getLRUD():
    return [(-1, 0), (1, 0), (0, -1), (0, 1)]