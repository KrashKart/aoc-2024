package day_03

import (
	a "aoc_2024/aocutils"
	"fmt"
	"regexp"
)

func Day_03() {
	total1, total2, do := 0, 0, 1
	lines := a.Reader(3)
	reg := regexp.MustCompile(`mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))`)
	for _, line := range lines {
		matches := reg.FindAllStringSubmatch(line, -1)
		for _, match := range matches {
			if match[0] == "don't()" {
				do = 0
			} else if match[0] == "do()" {
				do = 1
			} else {
				total1 += a.ToI(match[1]) * a.ToI(match[2])
				total2 += do * a.ToI(match[1]) * a.ToI(match[2])
			}
		}
	}

	fmt.Printf("Part 1: %d\n", total1)
	fmt.Printf("Part 2: %d\n", total2)
}