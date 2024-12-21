import aocutils
from itertools import accumulate
import re

ref, h, w = [], 101, 103

def quadrant(px, py):
	global h, w
	if px < h // 2 and py < w // 2:
		return 0
	elif px < h // 2 and py > w // 2:
		return 1
	elif px > h // 2 and py < w // 2:
		return 2
	elif px > h // 2 and py > w // 2:
		return 3
	else:
		return -1
	
def getGrid(robots, t):
	poses = set()
	for robot in robots:
		px, py = list(map(int, re.findall(r"p=(\d+),(\d+)", robot[0])[0]))
		vx, vy = list(map(int, re.findall(r"v=([-\d]+),([-\d]+)", robot[1])[0]))
		fx, fy = (px + vx * t) % h, (py + vy * t) % w
		poses.add((fx, fy))
	
	grid = [["." for _ in range(w)] for _ in range(h)]
	for i, j in poses:
		grid[i][j] = "#"
	return list(map(lambda x: "".join(x), grid))

def safety(t):
	quads = [0, 0, 0, 0]
	for robot in ref:
		px, py = list(map(int, re.findall(r"p=(\d+),(\d+)", robot[0])[0]))
		vx, vy = list(map(int, re.findall(r"v=([-\d]+),([-\d]+)", robot[1])[0]))
		fx, fy = (px + vx * t) % h, (py + vy * t) % w
		quad = quadrant(fx, fy)
		if quad != -1:
			quads[quad] += 1
	return quads[0] * quads[1] * quads[2] * quads[3]

def findLine(grid):
	for l in grid:
		if "##########" in l:
			return True
	return False

@aocutils.timeFunction
def main():
	global ref
	ref = aocutils.readFile(14, " ")

	total1, total2 = safety(100), 0

	for i in range(10404):
		if findLine(getGrid(ref, i)):
			total2 = i
			break

	print("\n".join(getGrid(ref, total2)))
	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()