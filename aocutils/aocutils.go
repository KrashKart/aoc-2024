package aocutils

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

const filepath string = "day_%02d/day_%02d.txt"

// Reads from an input txt file. 
// day parameter is the nth day
func Reader(day int) []string {
	file, err := os.Open(fmt.Sprintf(filepath, day, day))
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)
	var res []string

	for scanner.Scan() {
		res = append(res, scanner.Text())
	}

	return res
}


// maps element in array
func MapToInt(arr []string) []int {
	res := make([]int, len(arr))
	for i := range len(arr) {
		res[i] = ToI(arr[i])
	}
	return res
}

// Converts string to integer
func ToI(s string) int {
	val, _ := strconv.Atoi(s)
	return val
}

// Converts integer to string
func ToS(i int) string {
	s := strconv.Itoa(i)
	return s
}

// Checks out for bounds for array traversal problems
func OutOfBounds(i int, j int, iMin int, jMin int, iMax int, jMax int) bool {
	return i < iMin || i > iMax || j < jMin || j > jMax
}

// prints parts
func PrintPartsInt(part1 int, part2 int) {
	fmt.Printf("Part 1: %d\n", part1)
	fmt.Printf("Part 2: %d\n", part2)
}

// prints parts
func PrintPartsStr(part1 string, part2 string) {
	fmt.Printf("Part 1: %s\n", part1)
	fmt.Printf("Part 2: %s\n", part2)
}
