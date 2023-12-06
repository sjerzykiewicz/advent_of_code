package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

type Schema struct {
	board         [][]byte
	width         int
	height        int
	special_chars map[byte]bool
}

func make_schema(filepath string) Schema {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	schema := Schema{}
	schema.special_chars = map[byte]bool{}
	for scanner.Scan() {
		row := []byte{}
		for _, char := range scanner.Bytes() {
			row = append(row, char)
			schema.special_chars[char] = true
		}
		schema.board = append(schema.board, row)
	}

	delete(schema.special_chars, byte('.'))
	for i := 0; i < 10; i++ {
		delete(schema.special_chars, byte(i+48))
	}

	schema.width = len(schema.board[0])
	schema.height = len(schema.board)

	return schema
}

type Number struct {
	number int
	startX int
	endX   int
	y      int
}

func (s *Schema) get_all_numbers() []Number {
	numbers := []Number{}
	for y, row := range s.board {
		x := 0
		for x < s.width {
			char := row[x]
			if !s.special_chars[char] && char != byte('.') {
				startX := x
				num_str := ""
				for x < s.width && !s.special_chars[row[x]] && row[x] != byte('.') {
					num_str = num_str + string(row[x])
					x++
				}
				endX := x - 1
				num, _ := strconv.Atoi(num_str)
				numbers = append(numbers, Number{num, startX, endX, y})
			}
			x++
		}
	}

	return numbers
}

func (n *Number) check_if_adjacent_or_diagonal_is_special(s Schema) bool {
	for x := n.startX - 1; x <= n.endX+1; x++ {
		for y := n.y - 1; y <= n.y+1; y++ {
			if x >= 0 && x < s.width && y >= 0 && y < s.height {
				if s.special_chars[s.board[y][x]] {
					return true
				}
			}
		}
	}
	return false
}

func part_1(filepath string) int {
	schema := make_schema(filepath)
	numbers := schema.get_all_numbers()

	sum := 0
	for _, number := range numbers {
		if number.check_if_adjacent_or_diagonal_is_special(schema) {
			sum += number.number
		}
	}

	return sum
}

type Gear struct {
	ratio int
}

func (s *Schema) get_all_gears(numbers []Number) []Gear {
	gears := []Gear{}
	found_numbers := map[string][]Number{}
	for _, number := range numbers {
		for x := number.startX - 1; x <= number.endX+1; x++ {
			for y := number.y - 1; y <= number.y+1; y++ {
				if x >= 0 && x < s.width && y >= 0 && y < s.height {
					if s.board[y][x] == '*' {
						pos := fmt.Sprint(x) + "_" + fmt.Sprint(y)
						found_numbers[pos] = append(found_numbers[pos], number)
					}
				}
			}
		}
	}

	for _, v := range found_numbers {
		if len(v) == 2 {
			gears = append(gears, Gear{ratio: v[0].number * v[1].number})
		}
	}

	return gears
}

func part_2(filepath string) int {
	schema := make_schema(filepath)
	numbers := schema.get_all_numbers()
	gears := schema.get_all_gears(numbers)

	sum := 0
	for _, gear := range gears {
		sum += gear.ratio
	}

	return sum
}

func main() {

	// Part 1
	fmt.Printf("%v\n", part_1("input.txt"))

	// Part 2
	fmt.Printf("%v\n", part_2("input.txt"))

}
