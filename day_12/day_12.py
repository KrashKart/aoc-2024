import aocutils

def perimeter(group, withDiscount):
	perimeter = {(i, j, di, dj) for (di, dj) in aocutils.getLRUD() for (i, j) in group if (i + di, j + dj) not in group}
	if withDiscount:
		perimeter -= {(i - dj, j - di, di, dj) for (i, j, di, dj) in perimeter}
	return len(perimeter)

@aocutils.timeFunction
def main():
	grid = aocutils.readFile(12, isTest=False)
	total1, total2 = 0, 0
	
	h, w = len(grid), len(grid[0])
	groups = {(i, j): {(i, j)} for i in range(h) for j in range(w)}

	for i in range(h):
		for j in range(w):
			for di, dj in aocutils.getLRUD():
				if not aocutils.outOfBounds(i + di, j + dj, h - 1, w - 1) and grid[i][j] == grid[i + di][j + dj]:
					groups[(i, j)] = groups[(i, j)].union(groups[(i + di, j + dj)])
					for coords in groups[(i, j)]:
						groups[coords] = groups[(i, j)]
	unique_groups = {tuple(group) for group in groups.values()}

	for group in unique_groups:
		total1 += len(group) * perimeter(group, False)
		total2 += len(group) * perimeter(group, True)

	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()