import aocutils
from gridutils import Grid, Pos, Direction

# This solution runs in 3.7 MINUTES!!
# Not optimised with multiprocessing

gridRaw = aocutils.readFile(6)

grid = Grid(gridRaw)

startPos = grid.find("^")
grid.replace(startPos, "X")

def traverse(pos: Pos, dir=Direction.UP, isPart1=True):
    total = 0
    moves = 0
    while (not grid.outOfGrid(pos) and moves <= grid.height * grid.width):
        if grid.get(pos) == "#":
            pos = pos.backtrack(dir)
            dir = Direction.turn90Right(dir)
        elif grid.get(pos) == ".":
            grid.replace(pos, "X")
            total += 1
        pos = pos.move(dir)
        moves += 1
    return total if isPart1 else moves

total1 = traverse(startPos) + 1

grid = Grid(gridRaw)
total2 = 0
for x in range(grid.height):
    for y in range(grid.width):
        pos = Pos(x, y)
        if grid.get(pos) == "X":
            grid.replace(pos, "#")
            if traverse(startPos, isPart1=False) > grid.height * grid.width:
                total2 += 1
            grid.replace(pos, ".")

aocutils.printParts(total1, total2)