import aocutils
from collections import deque
from itertools import combinations

def floodfill(grid, si, sj):
	h, w = len(grid), len(grid[0])
	d = {}
	visited = set((si, sj))
	unexplored = deque()
	unexplored.append((0, si, sj))
	while unexplored:
		cost, curri, currj = unexplored.pop()
		d[(curri, currj)] = cost
		for di, dj in aocutils.getLRUD():
			nexti, nextj = curri + di, currj + dj
			if not aocutils.outOfBounds(nexti, nextj, h - 1, w - 1) and grid[nexti][nextj] != "#" and (nexti, nextj) not in visited:
				visited.add((nexti, nextj))
				unexplored.append((cost + 1, nexti, nextj))
	return d

def diff(ai, aj, bi, bj):
	return abs(ai - bi) + abs(aj - bj)

# 11s
@aocutils.timeFunction
def main():
	ref = aocutils.readFile(20, isTest=False)

	si, sj = 0, 0
	for i, l in enumerate(ref):
		for j, c in enumerate(l):
			if c == "S":
				si, sj = i, j
	
	total1, total2 = 0, 0
	distances = floodfill(ref, si, sj)
	for (i, j), (x, y) in combinations(distances.keys(), 2):
			dist = diff(i, j, x, y)
			if distances[(x, y)] - distances[(i, j)] - dist >= 100 and dist == 2:
				total1 += 1
			if distances[(x, y)] - distances[(i, j)] - dist >= 100 and dist < 21:
				total2 += 1

	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()