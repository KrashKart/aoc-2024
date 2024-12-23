import aocutils

prune = lambda n: n % 16777216
mix = lambda n, a: n ^ a

def generate(n):
	n = prune(mix(64 * n, n))
	n = prune(mix(n // 32, n))
	return prune(mix(n * 2048, n))

# 2.5s
@aocutils.timeFunction
def main():
	ref = map(int, aocutils.readFile(22, isTest=False, toList=False))

	total1, total2 = 0, 0
	seqs = {}
	for num in ref:
		nums = [num % 10]
		for _ in range(2000):
			num = generate(num)
			nums.append(num % 10)
		total1 += num

		diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
		seen = set()
		for i in range(len(nums) - 4):
			interval = tuple(diffs[i:i + 4])
			if interval not in seen:
				seqs[interval] = seqs.get(interval, 0) + nums[i + 4]
				seen.add(interval)

	total2 = max(seqs.values())
	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()