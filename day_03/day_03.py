import re

total1 = 0
total2 = 0
do = 1
with open("day_03/day_03.txt", "r") as f:
    for line in f:
        muls = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line)
        for match in muls:
            # part 1 and 2
            if match[0]:
                total1 += int(match[0]) * int(match[1])
                total2 += do * int(match[0]) * int(match[1])
            
            # part 2
            elif match[2]:
                do = 1
            else:
                do = 0

print("Part 1: " + str(total1))
print("Part 2: " + str(total2))