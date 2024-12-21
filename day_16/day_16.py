import aocutils
from heapq import heappop, heappush
import numpy as np

dirs = aocutils.getLRUD()
grid = []
h, w = 0, 0

def dijkstra(si, sj, di, dj, ei, ej):
	global grid, dirs, h, w
	heap, visited, paths, weights = [], set(), [], dict()

	heappush(heap, (0, si, sj, di, dj, [(si, sj)]))
	while heap:
		cost, curri, currj, diri, dirj, path = heappop(heap)
		visited.add((curri, currj, diri, dirj))
		weights[(curri, currj)] = min(weights.get((curri, currj), np.inf), cost)

		if (curri, currj) == (ei, ej):
			if cost <= weights[(ei, ej)]:
				paths.extend(path)
		else:
			for dirii, dirjj in [(dirj, -diri), (-dirj, diri), (diri, dirj)]:
				nexti, nextj = curri + dirii, currj + dirjj
				if not aocutils.outOfBounds(nexti, nextj, h - 1, w - 1) and grid[nexti][nextj] != "#" and (nexti, nextj, dirii, dirjj) not in visited:
					newcost = cost + 1001
					if (dirii, dirjj) == (diri, dirj):
						newcost -= 1000
					heappush(heap, (newcost, nexti, nextj, dirii, dirjj, path + [(nexti, nextj)]))
	return weights[(ei, ej)], len(set(paths))

@aocutils.timeFunction
def main():
	global grid, h, w
	grid = aocutils.readFile(16, isTest=False)
	h, w = len(grid), len(grid[0])
	si, sj = 0, 0
	for i, l in enumerate(grid):
		for j, t in enumerate(l):
			if t == "S":
				si, sj = i, j
			elif t == "E":
				ei, ej = i, j

	total1, total2 = dijkstra(si, sj, 0, 1, ei, ej)

	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()