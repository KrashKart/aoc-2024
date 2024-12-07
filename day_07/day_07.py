import aocutils

def extract(x):
    val, operands = x.split(": ")
    return (int(val), list(map(int, operands.split(" "))))

def canCompute(target, operands, val, part1):
    if not operands:
        return target == val
    return canCompute(target, operands[1:], val + operands[0]               , part1) \
        or canCompute(target, operands[1:], val * operands[0]               , part1) \
        or canCompute(target, operands[1:], int(str(val) + str(operands[0])), part1) and not part1

total1 = 0
total2 = 0
eqns = list(map(lambda x: extract(x), aocutils.readFile(7, isTest=False, toList=False)))
for t, os in eqns:
    if canCompute(t, os, 0, True):
        total1 += t
    if canCompute(t, os, 0, False):
        total2 += t

aocutils.printParts(total1, total2)