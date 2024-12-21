import aocutils
import re
import numpy as np

@aocutils.timeFunction
def main():
	OFFSET = 10000000000000
	ref = aocutils.readFile(13, toList=False)
	ref.append('')

	total1, total2 = 0, 0
	for i in range(0, len(ref), 4):
		buttonA, buttonB, prize, _ = ref[i:i + 4]
		buttonA = list(map(int, re.findall(r"[XY]\+(\d+)", buttonA)))
		buttonB = list(map(int, re.findall(r"[XY]\+(\d+)", buttonB)))
		prize = list(map(int, re.findall(r"[XY]=(\d+)", prize)))

		A = np.column_stack([buttonA, buttonB])
		B = np.array(prize, dtype=np.int64)
		B_2 = B + OFFSET

		x = np.rint(np.linalg.solve(A, B))
		x_2 = np.rint(np.linalg.solve(A, B_2))
		y = A @ x
		y_2 = A @ x_2

		if (y == B).all():
			total1 += int(x[0] * 3) + int(x[1])
		if (y_2 == B_2).all():
			total2 += int(x_2[0] * 3) + int(x_2[1])

	aocutils.printParts(total1, total2)
if __name__ == "__main__":
	main()