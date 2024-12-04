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

// Converts string to integer
func ToI(s string) int {
	val, _ := strconv.Atoi(s)
	return val
}
