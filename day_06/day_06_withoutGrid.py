import aocutils
from copy import deepcopy
from multiprocessing import Pool

def traverse(grid, i, j, h, w, isPart1=True):
    total = 0
    moves = 0
    di, dj = -1, 0 
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

def modifyTraverse(grid, modi, modj, starti, startj, h, w):
    gridCopy = deepcopy(grid)
    gridCopy[modi][modj] = "#"
    return traverse(gridCopy, starti, startj, h, w, isPart1=False) > h * w

@aocutils.timeFunction
def main():
    grid = aocutils.readFile(6)
    h, w = len(grid), len(grid[0])
    pool = Pool()

    for idx, g in enumerate(grid):
        if "^" in g:
            starti, startj = idx, g.index("^")
    grid[starti][startj] = "X"

    total1 = traverse(grid, starti, startj, h, w) + 1
    total2 = sum(pool.starmap(modifyTraverse, [(grid, x, y, starti, startj, h, w) for x in range(h) for y in range(w) if grid[x][y] == "X"]))

    aocutils.printParts(total1, total2)

if __name__ == "__main__":
    main()