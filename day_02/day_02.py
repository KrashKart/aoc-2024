# helpers
def isSafeInterval(a, b):
    return 1 <= abs(a - b) and abs(a - b) <= 3

def isSafeArr(arr):
    if sorted(arr) != arr and sorted(arr, reverse=True) != arr:
        return False

    for i in range(1, len(arr)):
        if not isSafeInterval(arr[i], arr[i - 1]):
            return False
    return True

# part 1
total1 = 0
reports = []
with open("day_02/day_02.txt", "r") as f:
    for line in f:
        seq = list(map(int, line.split(" ")))
        reports.append(seq)

for seq in reports:
    if isSafeArr(seq):
        total1 += 1
    

print("Part 1: " + str(total1))

# part 2
total2 = 0
for seq in reports:
    if isSafeArr(seq):
        total2 += 1
    else:
        for i in range(len(seq)):
            temp = seq[::]
            temp.pop(i)
            if isSafeArr(temp):
                total2 += 1
                break

print("Part 2: " + str(total2))