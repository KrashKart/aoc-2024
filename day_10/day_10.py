import aocutils

visited = []
grid = []
h = 0
w = 0

def score(i, j, isPart1):
	global grid, visited, h, w
	if grid[i][j] == 9 and ((i, j) not in visited or not isPart1):
		visited.append((i, j))
		return 1
	res = 0
	for di, dj in aocutils.getLRUD():
		if not aocutils.outOfBounds(i + di, j + dj, h - 1, w - 1) and grid[i + di][j + dj] - grid[i][j] == 1:
			res += score(i + di, j + dj, isPart1)
	return res

@aocutils.timeFunction
def main():
	global grid, h, w, visited
	grid = list(map(lambda x: list(map(int, x)), aocutils.readFile(10)))
	h, w = len(grid), len(grid[0])
	total1, total2 = 0, 0
	
	for i in range(h):
		for j in range(w):
			if grid[i][j] == 0:
				visited = []
				total1 += score(i, j, True)
				total2 += score(i, j, False)

	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()