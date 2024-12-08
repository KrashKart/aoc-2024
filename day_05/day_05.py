import aocutils
import functools

everything = aocutils.readFile(5, toList=False)
partition = everything.index("")
rules, updates = everything[:partition], everything[partition + 1:]

rules = list(map(lambda x: tuple(map(int, x.split("|"))), rules))
updates = list(map(lambda x: list(map(int, x.split(","))), updates))

def isGreater(a, b):
    for r in rules:
        if r == (a, b):
            return -1
        elif r == (b, a):
            return 1

@aocutils.timeFunction
def main():
    total1 = 0
    total2 = 0
    for u in updates:
        uOriginal = u[::]
        uOriginal.sort(key=functools.cmp_to_key(isGreater))
        if uOriginal == u:
            total1 += u[len(u) // 2]
        else:
            total2 += uOriginal[len(u) // 2]

    aocutils.printParts(total1, total2)

if __name__ == "__main__":
    main()