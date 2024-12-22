import aocutils
import z3

def process(instrs, regs):
	out = []
	pointer = 0
	while pointer < len(instrs):
		opcode, val = instrs[pointer:pointer + 2]
		match opcode:
			case 0: regs[0] //= 2 ** getOperand(val, regs, True)
			case 1: regs[1] ^= getOperand(val, regs, False)
			case 2: regs[1] = getOperand(val, regs, True) % 8
			case 3: 
				if regs[0] != 0: pointer = getOperand(val, regs, False) - 2
			case 4: regs[1] ^= regs[2]
			case 5: out.append(getOperand(val, regs, True) % 8)
			case 6: regs[1] = regs[0] // 2 ** getOperand(val, regs, True)
			case 7: regs[2] = regs[0] // 2 ** getOperand(val, regs, True)
		pointer += 2
	return ",".join(map(str, out))

def getOperand(val, regs, isCombo):
	if not isCombo or 0 <= val <= 3:
		return val
	return regs[val - 4]

@aocutils.timeFunction
def main():
	ref = aocutils.readFile(17, isTest=False, toList=False)
	for line in ref:
		if "Register A" in line: regA = int(line[12:])
		elif "Register B" in line: regB = int(line[12:])
		elif "Register C" in line: regC = int(line[12:])
		elif "Program" in line: instrs = list(map(int, line[9:].split(",")))

	assert instrs

	# would like to thank u/SuperSmurfen for the idea to analyse the program and to use z3 to solve for A
	solver = z3.Optimize()
	varA = z3.BitVec("varA", 64)
	a, b, c = varA, 0, 0
	for instr in instrs:
		b = a % 8
		b ^= 5
		c = a >> b
		b ^= 6
		a >>= 3
		b ^= c
		solver.add(b % 8 == instr)
	solver.add(a == 0)
	solver.minimize(varA)

	assert str(solver.check()) == "sat"
	total1, total2 = process(instrs, [regA, regB, regC]), solver.model().eval(varA)
	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()