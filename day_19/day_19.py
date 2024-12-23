import aocutils

DP = {}

def isPossible(towels: tuple[str], combi: str):
	global DP
	if not combi:
		DP[combi] = 1
		return 1
	elif all([not combi.startswith(t) for t in towels]):
		DP[combi] = 0
		return 0
	elif combi in DP.keys():
		return DP[combi]
	DP[combi] = sum([isPossible(towels, combi.removeprefix(t)) for t in towels if combi.startswith(t)])
	return DP[combi]

@aocutils.timeFunction
def main():
	towels, combis = aocutils.readFileWithNewline(19, isTest=False, toList=False)
	towels = tuple(towels[0].split(", "))
	total1, total2 = 0, 0

	for combi in combis:
		res = isPossible(towels, combi)
		total1 += 1 if res else 0
		total2 += res

	aocutils.printParts(total1, total2)
if __name__ == "__main__":
	main()