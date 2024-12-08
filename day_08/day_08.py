import aocutils

def findAntinodes(i, j, i_diff, j_diff, h, w):
	antinodes = []
	while not aocutils.outOfBounds(i + i_diff, j + j_diff, 0, 0, h - 1, w - 1):
		antinodes.append((i + i_diff, j + j_diff))
		i += i_diff
		j += j_diff
	return antinodes

def antinodesInBounds(coordi, coordj, h, w):
	x1, y1 = coordi
	x2, y2 = coordj
	x_diff, y_diff = x1 - x2, y1 - y2

	antinodes1 = findAntinodes(x1, y1, x_diff, y_diff, h, w)
	antinodes2 = findAntinodes(x2, y2, -x_diff, -y_diff, h, w)

	return antinodes1[:1] + antinodes2[:1], antinodes1 + antinodes2 + [coordi, coordj]

@aocutils.timeFunction
def main():
	grid = aocutils.readFile(8)
	h, w = len(grid), len(grid[0])
	ref = {}
	for i in range(h):
		for j in range(w):
			if grid[i][j] != ".":
				temp = ref.get(grid[i][j], [])
				temp.append((i, j))
				ref[grid[i][j]] = temp

	antinodes1 = []
	antinodes2 = []
	pairs = 0
	for v in ref.values():
		for x in range(len(v) - 1):
			for y in range(x + 1, len(v)):
				if x != y:
					res = antinodesInBounds(v[x], v[y], h, w)
					antinodes1 += res[0]
					antinodes2 += res[1]
	total1 = len(set(antinodes1))
	total2 = len(set(antinodes2)) + pairs
	
	aocutils.printParts(total1, total2)


if __name__ == "__main__":
	main()
