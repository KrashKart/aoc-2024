package day_07

import (
	a "aoc_2024/aocutils"
	"strings"
)

func canCompute(target int, operands []int, val int, isPart1 bool) bool {
	if len(operands) == 0 {
		return val == target
	} 
	return canCompute(target, operands[1:], val + operands[0]					  , isPart1) ||
		   canCompute(target, operands[1:], val * operands[0]					  , isPart1) ||
		   canCompute(target, operands[1:], a.ToI(a.ToS(val) + a.ToS(operands[0])), isPart1) && !isPart1
}

func Day_07() {
	eqns := a.Reader(7)
	total1, total2 := 0, 0
	for _, e := range eqns {
		e := strings.Split(e, ": ")
		t, os := a.ToI(e[0]), a.MapToInt(strings.Split(e[1], " "))
		if canCompute(t, os, 0, true) {
			total1 += t
		}
		if canCompute(t, os, 0, false) {
			total2 += t
		}
	}

	a.PrintPartsInt(total1, total2)
}
