package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func LoadInput(fileName string) []map[string]int {

	file, err := os.Open(fileName)
	if err != nil {
		fmt.Errorf("Error reading in file %w", err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var lines []string

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	var input []map[string]int

	// for each line in the input document, convert the command/value pair into a slice
	// of string/int pairs
	for _, line := range lines {

		valuesSlice := strings.Fields(line)
		command := valuesSlice[0]
		value, _ := strconv.Atoi(valuesSlice[1])

		tempMap := map[string]int{command: value}
		input = append(input, tempMap)
	}
	return input
}

func NavigationPart1(input *[]map[string]int) int {

	distance, depth := 0, 0

	for _, commandMap := range *input {

		for command, value := range commandMap {

			switch command {
			case "forward":
				distance += value
			case "up":
				depth -= value
			case "down":
				depth += value
			}
		}
	}

	return distance * depth
}

func NavigationPart2(input *[]map[string]int) int {

	distance, depth, aim := 0, 0, 0

	for _, commandMap := range *input {

		for command, value := range commandMap {

			switch command {
			case "forward":
				distance += value
				depth += value * aim
			case "up":
				aim -= value
			case "down":
				aim += value
			}
		}
	}

	return distance * depth
}

func main() {

	input := LoadInput("input.txt")

	fmt.Println(NavigationPart1(&input))
	fmt.Println(NavigationPart2(&input))

}
