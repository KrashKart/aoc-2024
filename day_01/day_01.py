import aocutils

@aocutils.timeFunction
def main():
    # part 1
    arr1 = []
    arr2 = []
    lines = aocutils.readFile(1, False)

    for line in lines:
        i, j = list(map(int, line.strip().split('  ')))
        arr1.append(i)
        arr2.append(j)

    arr1, arr2 = sorted(arr1), sorted(arr2)

    total1 = 0
    for x in range(len(arr1)):
        total1 += abs(arr1[x] - arr2[x])

    # part 2
    arr1 = set(arr1)
    total2 = 0
    for i in arr1:
        total2 += i * arr2.count(i)

if __name__ == "__main__":
    main()