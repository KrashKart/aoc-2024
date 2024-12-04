def readFile(day: int, toList: bool = True) -> list[str]:
    res = []
    with open(f"day_{day:02}/day_{day:02}.txt", "r") as f:
        for line in f:
            if toList:
                line = list(line)
            res.append(line)
    return res

def outOfBounds(i: int, j: int, iMin: int, jMin: int, iMax: int, jMax: int) -> bool:
    return i < iMin or i > iMax or j < jMin or j > jMax

def printParts(part1, part2):
    print("Part 1: " + str(part1))
    print("Part 2: " + str(part2))