def readFile(day: int, toList: bool = True) -> list[str]:
    res = []
    with open(f"day_{day:02}/day_{day:02}.txt", "r") as f:
        for line in f:
            if toList:
                line = list(line)
            res.append(line)
    return res