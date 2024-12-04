package aocutils

import (
	"bufio"
	"os"
)

func Reader(filename string) []string {
	file, err := os.Open(filename)
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
