package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"reflect"
	"strconv"
	"strings"
)

type Line struct {
	history [][]int
}

type Sensor struct {
	lines []Line
}

func getSensor(filepath string) Sensor {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	sensor := Sensor{}
	sensor.lines = []Line{}
	line_cnt := 0
	for scanner.Scan() {
		sensor.lines = append(sensor.lines, Line{})
		line_str := strings.Split(scanner.Text(), " ")
		sensor.lines[line_cnt].history = [][]int{}
		sensor.lines[line_cnt].history = append(sensor.lines[line_cnt].history, []int{})
		for _, char := range line_str {
			number, _ := strconv.Atoi(char)
			sensor.lines[line_cnt].history[0] = append(sensor.lines[line_cnt].history[0], number)
		}
		line_cnt++
	}

	return sensor
}

func checkIfOnlyZeroes(history []int) bool {
	return reflect.DeepEqual(history, make([]int, len(history)))
}

func (l *Line) findNextValue() int {
	for {
		if checkIfOnlyZeroes(l.history[len(l.history)-1]) {
			break
		}
		l.history = append(l.history, []int{})
		for i := 1; i < len(l.history[len(l.history)-2]); i++ {
			l.history[len(l.history)-1] = append(l.history[len(l.history)-1], l.history[len(l.history)-2][i]-l.history[len(l.history)-2][i-1])
		}
	}

	nextValue := 0
	for _, history := range l.history {
		nextValue += history[len(history)-1]
	}

	return nextValue
}

func part_1(filepath string) int {
	sensor := getSensor(filepath)

	sum := 0
	for _, line := range sensor.lines {
		sum += line.findNextValue()
	}

	return sum
}

func (l *Line) findPrevValue() int {
	for {
		if checkIfOnlyZeroes(l.history[len(l.history)-1]) {
			break
		}
		l.history = append(l.history, []int{})
		for i := 1; i < len(l.history[len(l.history)-2]); i++ {
			l.history[len(l.history)-1] = append(l.history[len(l.history)-1], l.history[len(l.history)-2][i]-l.history[len(l.history)-2][i-1])
		}
	}

	prevValues := []int{0}
	for i := len(l.history) - 1; i >= 0; i-- {
		prevValue := prevValues[len(prevValues)-1]
		prevValues = append(prevValues, l.history[i][0]-prevValue)
	}

	return prevValues[len(prevValues)-1]
}

func part_2(filepath string) int {
	sensor := getSensor(filepath)

	sum := 0
	for _, line := range sensor.lines {
		sum += line.findPrevValue()
	}

	return sum
}

func main() {

	// Part 1
	fmt.Printf("%v\n", part_1("input.txt"))

	// Part 2
	fmt.Printf("%v\n", part_2("input.txt"))

}
