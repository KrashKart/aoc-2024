import aocutils

DIRECTIONAL_KEYPAD = {' ': (0, 0), '^': (1, 0), 'A': (2, 0), 
					  '<': (0, 1), 'v': (1, 1), '>': (2, 1)}

NUMERIC_KEYPAD = {'7': (0, 0), '8': (1, 0), '9': (2, 0), 
				  '4': (0, 1), '5': (1, 1), '6': (2, 1), 
				  '1': (0, 2), '2': (1, 2), '3': (2, 2), 
				  ' ': (0, 3), '0': (1, 3), 'A': (2, 3)}

# HEAVILY inspired by blueboss452
def solve(code, n):
	global DIRECTIONAL_KEYPAD
	DP = {(0, key1, key2): 1 for key1 in DIRECTIONAL_KEYPAD for key2 in DIRECTIONAL_KEYPAD}
	fewest_presses = lambda l, ks: sum(DP[(l, ki, kf)] for ki, kf in zip('A' + ks, ks))
	keypad = DIRECTIONAL_KEYPAD
	for layer in range(1, n + 1):
		if layer == n:
			keypad = NUMERIC_KEYPAD
		for key, (i, j) in keypad.items():
			for nextKey, (x, y) in keypad.items():
				horizontal = ('>' if x > i else '<') * abs(x - i)
				vertical = ('^' if y < j else 'v') * abs(y - j)
				hori = fewest_presses(layer - 1, horizontal + vertical + 'A') if (x, j) != keypad[' '] else float('inf')
				verti = fewest_presses(layer - 1, vertical + horizontal + 'A') if (i, y) != keypad[' '] else float('inf')
				DP[(layer, key, nextKey)] = min(hori, verti)
	return fewest_presses(layer, code)

@aocutils.timeFunction
def main():
	ref = aocutils.readFile(21, toList=False)
      
	total1, total2 = 0, 0
	for seq in ref:
		total1 += solve(seq, 3) * int(seq[:-1])
		total2 += solve(seq, 26) * int(seq[:-1])

	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()