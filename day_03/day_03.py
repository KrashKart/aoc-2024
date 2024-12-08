import re
import aocutils

@aocutils.timeFunction
def main():
    total1 = 0
    total2 = 0
    do = 1

    lines = aocutils.readFile(3, False)
    for line in lines:
        muls = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line)
        for match in muls:
            # part 1 and 2
            if match[0]:
                total1 += int(match[0]) * int(match[1])
                total2 += do * int(match[0]) * int(match[1])
            
            # part 2
            elif match[2]: do = 1
            else: do = 0
    
    aocutils.printParts(total1, total2)

if __name__ == "__main__":
    main()