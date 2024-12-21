import aocutils

def change(stone):
	if int(stone) == 0:
		return ["1"]
	elif len(stone) % 2 == 0:
		mid = len(stone) // 2
		return [str(int(stone[:mid])), str(int(stone[mid:]))]
	else:
		return [str(int(stone) * 2024)]

@aocutils.timeFunction
def main():
	ref = aocutils.readFile(11, " ")[0]
	helper = {i: 1 for i in ref}
	for i in range(75):
		nexthelper = {}
		if i == 25:
			total1 = sum(helper.values())
		for k, v in helper.items():
			for j in change(k):
				nexthelper[j] = nexthelper.get(j, 0) + v
			
		helper = nexthelper
	
	total2 = sum(helper.values())
	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()