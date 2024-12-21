import aocutils
from copy import deepcopy

dirs = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}

# MASSIVE THANKS to u/4HbQ, because I would not be able to figure this shorter implementation out without looking at his implementation

def move(grid, posi, posj, di, dj):
	nexti, nextj = posi + di, posj + dj
	if all([grid[nexti][nextj] != "[" or move(grid, nexti, nextj + 1, di, dj) and move(grid, nexti, nextj, di, dj),
        	grid[nexti][nextj] != "]" or move(grid, nexti, nextj - 1, di, dj) and move(grid, nexti, nextj, di, dj),
        	grid[nexti][nextj] != "O" or move(grid, nexti, nextj, di, dj), 
			grid[nexti][nextj] != "#"]):
		
			grid[posi][posj], grid[nexti][nextj] = grid[nexti][nextj], grid[posi][posj]
			return True
	return False

def sumCoords(grid):
	s = 0
	for i, l in enumerate(grid):
		for j, t in enumerate(l):
			if t in "O[":
				s += 100 * i + j
	return s

@aocutils.timeFunction
def main():
	ref = aocutils.readFile(15, isTest=False, toList=False)
	splitOn = 0
	for idx, line in enumerate(ref):
		if line == "":
			splitOn = idx
			break

	grid, instructions = list(map(list, ref[:splitOn])), "".join(ref[splitOn + 1:])
	grid2 = [list("".join(l).translate(str.maketrans({"#": "##", ".": "..", "O": "[]", "@": "@."}))) for l in grid]

	ci, cj = 0, 0
	isPart2 = False
	for g in [grid, grid2]:
		for i, line in enumerate(g):
			for j, c in enumerate(line):
				if c == "@":
					ci, cj = i, j
		for instrs in instructions:
			unchanged = deepcopy(g)
			di, dj = dirs[instrs]
			if move(g, ci, cj, di, dj):
				ci, cj = ci + di, cj + dj
			else:
				g = unchanged
		if not isPart2:
			total1 = sumCoords(g)
			isPart2 = True
	total2 = sumCoords(g)

	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()