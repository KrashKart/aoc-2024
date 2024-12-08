import aocutils
from multiprocessing import Pool

def extract(x):
    val, operands = x.split(": ")
    return (int(val), list(map(int, operands.split(" "))), 0)

def canCompute(target, operands, val, part1):
    if not operands:
        return target == val
    
    isComputable = canCompute(target, operands[1:], val + operands[0]               , part1) \
                or canCompute(target, operands[1:], val * operands[0]               , part1) \
                or canCompute(target, operands[1:], int(str(val) + str(operands[0])), part1) and not part1
    
    return target if isComputable else 0

@aocutils.timeFunction
def main():
    pool = Pool()
    total1 = 0
    total2 = 0
    eqns = list(map(lambda x: extract(x), aocutils.readFile(7, isTest=False, toList=False)))

    total1 = sum(pool.starmap(canCompute, list(map(lambda x: x + (True,), eqns))))
    total2 = sum(pool.starmap(canCompute, list(map(lambda x: x + (False,), eqns))))

    aocutils.printParts(total1, total2)

if __name__ == "__main__":
    main()