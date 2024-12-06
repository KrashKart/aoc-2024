import aocutils

# this solution runs in 13 seconds

grid = aocutils.readFile(6)

h, w = len(grid), len(grid[0])

for idx, g in enumerate(grid):
    if "^" in g:
        starti, startj = idx, g.index("^")
grid[starti][startj] = "X"

def traverse(i, j, di = -1, dj = 0, isPart1=True):
    total = 0
    moves = 0
    while (not aocutils.outOfBounds(i, j, 0, 0, h - 1, w - 1) and moves <= h * w):
        if grid[i][j] == "#":
            i, j = i - di, j - dj
            di, dj = dj, -di
        elif grid[i][j] == ".":
            grid[i][j] = "X"
            total += 1
        i, j = i + di, j + dj
        moves += 1
    return total if isPart1 else moves

total1 = traverse(starti, startj) + 1

total2 = 0
for x in range(h):
    for y in range(w):
        if grid[x][y] == "X":
            grid[x][y] = "#"
            if traverse(starti, startj, isPart1=False) > h * w:
                total2 += 1
            grid[x][y] = "."

aocutils.printParts(total1, total2)