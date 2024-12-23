import aocutils
import numpy as np
from heapq import heappush, heappop

h = w = 71

def dijkstra(grid, si, sj, ei, ej):
	global h, w
	heap, visited, weights = [], set(), dict()

	heappush(heap, (0, si, sj, 0, 1))
	heappush(heap, (0, si, sj, 1, 0))

	while heap:
		cost, curri, currj, diri, dirj = heappop(heap)
		weights[(curri, currj)] = min(weights.get((curri, currj), np.inf), cost)

		if (curri, currj) == (ei, ej):
			return weights.get((ei, ej), np.inf)
		else:
			for dirii, dirjj in [(dirj, -diri), (-dirj, diri), (diri, dirj)]:
				nexti, nextj = curri + dirii, currj + dirjj
				if not aocutils.outOfBounds(nexti, nextj, h - 1, w - 1) and grid[nexti][nextj] != "#" and (nexti, nextj) not in visited:
					visited.add((nexti, nextj))
					heappush(heap, (cost + 1, nexti, nextj, dirii, dirjj))
	return weights.get((ei, ej), np.inf)

def getGridUntilByte(ref, n):
	grid = [["." for _ in range(w)] for _ in range(h)]
	for l in ref[:n]:
		i, j = map(int, l.split(","))
		grid[i][j] = "#"
	return grid

# 19.3s with linear Brute Force, 0.03s with Binary Search
@aocutils.timeFunction
def main():
	global h, w
	ref = aocutils.readFile(18, isTest=False, toList=False)
	si, sj, ei, ej = 0, 0, 70, 70

	total1, total2 = dijkstra(getGridUntilByte(ref, 1024), si, sj, ei, ej), 0
	N = len(ref) - 1
	start, end = 0, N
	while start < end:
		mid = (start + end) // 2
		res = dijkstra(getGridUntilByte(ref, mid), si, sj, ei, ej)
		if res == np.inf:
			end = mid - 1
		else:
			start = mid + 1
	
	total2 = ref[mid + 1]

	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()