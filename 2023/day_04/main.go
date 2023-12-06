package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"os"
	"strconv"
)

type Scratchcard struct {
	id               int
	winning_numbers  map[int]bool
	numbers          []int
	number_of_copies int
}

func get_scratchcards(filepath string) []Scratchcard {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	scratchcards := []Scratchcard{}
	for scanner.Scan() {
		splitted := bytes.Split(scanner.Bytes(), []byte(":"))
		card_id := splitted[0]
		cards := splitted[1]
		card_id_int, _ := strconv.Atoi(string(bytes.Split(card_id, []byte(" "))[1]))
		cards_bytes := bytes.Split(cards, []byte("|"))

		winning_numbers_bytes := bytes.Split(cards_bytes[0], []byte(" "))
		winning_numbers := map[int]bool{}
		for _, number := range winning_numbers_bytes {
			number_int, err := strconv.Atoi(string(number))
			if err == nil {
				winning_numbers[number_int] = true
			}
		}

		numbers_bytes := bytes.Split(cards_bytes[1], []byte(" "))
		numbers := []int{}
		for _, number := range numbers_bytes {
			number_int, err := strconv.Atoi(string(number))
			if err == nil {
				numbers = append(numbers, number_int)
			}
		}

		scratchcards = append(scratchcards, Scratchcard{card_id_int, winning_numbers, numbers, 1})
	}

	return scratchcards
}

func (s *Scratchcard) calculate_points() int {
	points := 0
	for _, number := range s.numbers {
		if s.winning_numbers[number] {
			if points == 0 {
				points = 1
			} else {
				points *= 2
			}
		}
	}
	return points
}

func part_1(filepath string) int {
	scratchcards := get_scratchcards(filepath)

	sum := 0
	for _, scratchcard := range scratchcards {
		sum += scratchcard.calculate_points()
	}

	return sum
}

func (s *Scratchcard) calculate_matched_cards() int {
	cnt := 0
	for _, number := range s.numbers {
		if s.winning_numbers[number] {
			cnt++
		}
	}
	return cnt
}

func calculate_number_of_cards(scratchcards []Scratchcard) []Scratchcard {
	for i, scratchcard := range scratchcards {
		cards_matched := scratchcard.calculate_matched_cards()
		for j := 1; j <= cards_matched; j++ {
			if i+j < len(scratchcards) {
				scratchcards[i+j].number_of_copies += scratchcard.number_of_copies
			}
		}
	}

	return scratchcards
}

func part_2(filepath string) int {
	scratchcards := calculate_number_of_cards(get_scratchcards(filepath))

	sum := 0
	for _, scratchcard := range scratchcards {
		sum += scratchcard.number_of_copies
	}

	return sum
}

func main() {

	// Part 1
	fmt.Printf("%v\n", part_1("input.txt"))

	// Part 2
	fmt.Printf("%v\n", part_2("input.txt"))

}
