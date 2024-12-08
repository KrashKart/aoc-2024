import aocutils

dirs = [[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]
a = ["SAM", "MAS"]
grid = aocutils.readFile(4)

def matchPattern(i, j):
    if i > len(grid) - 3 or j > len(grid[0]) - 3:
        return 0
    cross1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
    cross2 = grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2]
    if cross1 in a and cross2 in a:
        return 1
    return 0

def traverse(i, j, dir, accum):
    if accum == "XMAS":
        return 1
    elif len(accum) > 4 or aocutils.outOfBounds(i, j, len(grid) - 1, len(grid[0]) - 1):
        return 0
    return traverse(i + dir[0], j + dir[1], dir, accum + grid[i][j])

@aocutils.timeFunction
def main():
    total1, total2 = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for dir in dirs:
                total1 += traverse(i, j, dir, "")
            total2 += matchPattern(i, j)

    aocutils.printParts(total1, total2)

if __name__ == "__main__":
    main()