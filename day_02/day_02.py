import aocutils

# helper
def isSafeArr(arr):
    if sorted(arr) != arr and sorted(arr, reverse=True) != arr:
        return False

    for i, j in zip(arr, arr[1:]):
        if 1 > abs(i - j) or abs(i - j) > 3:
            return False
    return True

total1 = 0
total2 = 0
lines = aocutils.readFile(2, False)

for line in lines:
    seq = list(map(int, line.split(" ")))

    # part 1 and 2
    if isSafeArr(seq):
        total1 += 1
        total2 += 1
    else:
        # part 2
        for i in range(len(seq)):
            temp = seq[::]
            temp.pop(i)
            if isSafeArr(temp):
                total2 += 1
                break

print("Part 1: " + str(total1))

print("Part 2: " + str(total2))