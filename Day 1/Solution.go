package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func IncreasingDepthsPart1(depths *[]int) int {

	output := 0

	for previousIndex, depth := range (*depths)[1:] {

		if depth > (*depths)[previousIndex] {
			output += 1
		}

	}

	return output
}

func IncreasingDepthsPart2(depths *[]int) int {

	output := 0

	for previousIndex, depth := range (*depths)[3:] {

		if depth > (*depths)[previousIndex] {
			output += 1
		}

	}

	return output
}

func main() {

	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error reading in input file", err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	var depths []int

	for scanner.Scan() {
		num, _ := strconv.Atoi(scanner.Text())
		depths = append(depths, num)
	}

	fmt.Println(IncreasingDepthsPart1(&depths))
	fmt.Println(IncreasingDepthsPart2(&depths))
}
