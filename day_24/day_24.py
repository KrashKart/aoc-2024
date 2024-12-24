import aocutils
import re
from itertools import permutations
from collections import deque

def process(ref, gates):
	waiting = deque()
	waiting.extend(gates)

	while waiting:
		a, op, b, c = waiting.popleft()
		if a not in ref.keys() or b not in ref.keys():
			waiting.append((a, op, b, c))
		else:
			match op:
				case "AND":
					ref[c] = ref[a] & ref[b]
				case "OR":
					ref[c] = ref[a] | ref[b]
				case _:
					ref[c] = ref[a] ^ ref[b]

	return int("".join([str(ref[k]) for k in sorted(ref.keys(), reverse=True) if k.startswith("z")]), 2) # convert to decimal

# inspiration from u/ayoubzulfiqar
def find(a, op, b, gates):
    for gate in gates:
        if a in gate and op in gate and b in gate:
            return gate[-1]
    return None

# inspiration from u/ayoubzulfiqar
def solve(gates):
	swapped = []
	prevCarry = None
	for i in range(45):
		n = str(i).zfill(2)
		sumBit = carryBit = prevCarryCarried = prevCarryAdded = currCarry = None

		sumBit = find(f"x{n}", f"y{n}", "XOR", gates)
		carryBit = find(f"x{n}", f"y{n}", "AND", gates)

		if prevCarry:
			prevCarryCarried = find(prevCarry, sumBit, "AND", gates)
			prevCarryAdded = find(prevCarry, sumBit, "XOR", gates)
			
			if not prevCarryCarried:
				sumBit, carryBit = carryBit, sumBit
				swapped.extend([sumBit, carryBit])
				prevCarryCarried = find(prevCarry, sumBit, "AND", gates)

			if sumBit and sumBit.startswith("z"):
				sumBit, prevCarryAdded = prevCarryAdded, sumBit
				swapped.extend([sumBit, prevCarryAdded])

			if carryBit and carryBit.startswith("z"):
				carryBit, prevCarryAdded = prevCarryAdded, carryBit
				swapped.extend([carryBit, prevCarryAdded])

			if prevCarryCarried and prevCarryCarried.startswith("z"):
				prevCarryCarried, prevCarryAdded = prevCarryAdded, prevCarryCarried
				swapped.extend([prevCarryCarried, prevCarryAdded])

			currCarry = find(prevCarryCarried, carryBit, "OR", gates)

		if currCarry and currCarry.startswith("z") and currCarry != "z45":
			currCarry, prevCarryAdded = prevCarryAdded, currCarry
			swapped.extend([currCarry, prevCarryAdded])

		prevCarry = currCarry if prevCarry else carryBit

	return ",".join(sorted(swapped))

@aocutils.timeFunction
def main():
	inputs, gates = aocutils.readFileWithNewline(24, isTest=False, toList=False)
	ref = {}
	for i in inputs:
		inputName, val = i.split(": ")
		val = int(val)
		ref[inputName] = val

	gates = list(map(lambda x: re.findall(r"(.{3}) (AND|OR|XOR) (.{3}) -> (.{3})", x)[0], gates))

	total1, total2 = process(ref, gates), solve(gates)

	aocutils.printParts(total1, total2)


if __name__ == "__main__":
	main()