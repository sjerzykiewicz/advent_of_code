package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func part_1(filepath string) int {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	numbers := []int{}
	for scanner.Scan() {
		digits := []string{}

		for _, char := range scanner.Bytes() {
			_, err := strconv.Atoi(string(char))
			if err == nil {
				digits = append(digits, string(char))
			}
		}
		number, err := strconv.Atoi(digits[0] + digits[len(digits)-1])
		if err == nil {
			numbers = append(numbers, number)
		}
	}

	sum := 0
	for _, number := range numbers {
		sum += number
	}

	return sum
}

var Digits = [][]byte{[]byte("0"), []byte("1"), []byte("2"), []byte("3"), []byte("4"), []byte("5"), []byte("6"), []byte("7"), []byte("8"), []byte("9")}
var DigitsWords = [][]byte{[]byte("one"), []byte("two"), []byte("three"), []byte("four"), []byte("five"), []byte("six"), []byte("seven"), []byte("eight"), []byte("nine")}

type DigitWithPos struct {
	Digit string
	Pos   int
}

func part_2(filepath string) int {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	numbers := []int{}
	for scanner.Scan() {
		digitsWithPos := []DigitWithPos{}

		line := scanner.Bytes()

		for _, digit := range Digits {
			newLine := line
			index := bytes.LastIndex(newLine, digit)
			for {
				if index == -1 {
					break
				}
				digitsWithPos = append(digitsWithPos, DigitWithPos{string(digit), index})
				index = bytes.LastIndex(newLine[:index], digit)
			}
		}
		for i, digitWord := range DigitsWords {
			newLine := line
			index := bytes.LastIndex(newLine, []byte(digitWord))
			for {
				if index == -1 {
					break
				}
				digitsWithPos = append(digitsWithPos, DigitWithPos{strconv.Itoa(i + 1), index})
				index = bytes.LastIndex(newLine[:index], []byte(digitWord))
			}
		}

		sort.Slice(digitsWithPos, func(i, j int) bool {
			return digitsWithPos[i].Pos < digitsWithPos[j].Pos
		})

		number, err := strconv.Atoi(digitsWithPos[0].Digit + digitsWithPos[len(digitsWithPos)-1].Digit)
		if err == nil {
			numbers = append(numbers, number)
		}
	}

	sum := 0
	for _, number := range numbers {
		sum += number
	}

	return sum
}

func main() {

	// Part 1
	fmt.Printf("%v\n", part_1("input.txt"))

	// Part 2
	fmt.Printf("%v\n", part_2("input.txt"))

}
