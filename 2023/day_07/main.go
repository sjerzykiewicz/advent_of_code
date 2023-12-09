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

type Hand struct {
	cards []rune
	bid   int
}

func get_hands(filepath string) []Hand {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	hands := []Hand{}
	for scanner.Scan() {
		splitted := bytes.Split(scanner.Bytes(), []byte(" "))
		cards := []rune{}
		for _, card := range splitted[0] {
			cards = append(cards, rune(card))
		}
		bid, _ := strconv.Atoi(string(splitted[1]))
		hands = append(hands, Hand{cards, bid})
	}

	return hands
}

var card_values = map[rune]int{
	'A': 13,
	'K': 12,
	'Q': 11,
	'J': 10,
	'T': 9,
	'9': 8,
	'8': 7,
	'7': 6,
	'6': 5,
	'5': 4,
	'4': 3,
	'3': 2,
	'2': 1,
}

func (h *Hand) get_highest_freq() (int, int) {
	freq := map[rune]int{}
	for _, card := range h.cards {
		freq[card]++
	}

	max := 0
	second_max := 0
	for _, value := range freq {
		if value > max {
			second_max = max
			max = value
		} else if value > second_max {
			second_max = value
		}
	}
	return max, second_max
}

func (h *Hand) get_type_value() int {
	highest, second_highest := h.get_highest_freq()

	if highest == 5 {
		return 7
	} else if highest == 4 {
		return 6
	} else if highest == 3 && second_highest == 2 {
		return 5
	} else if highest == 3 {
		return 4
	} else if highest == 2 && second_highest == 2 {
		return 3
	} else if highest == 2 {
		return 2
	} else if highest == 1 {
		return 1
	} else {
		return 0
	}
}

func compare_hands(hand1, hand2 Hand, part_2 bool) bool {
	if part_2 {
		card_values['J'] = 0
	}
	for i, card := range hand1.cards {
		if card_values[card] > card_values[hand2.cards[i]] {
			return false
		} else if card_values[card] < card_values[hand2.cards[i]] {
			return true
		}
	}
	return false
}

func part_1(filepath string) int {
	hands := get_hands(filepath)

	sort.SliceStable(hands, func(i, j int) bool {
		if hands[i].get_type_value() == hands[j].get_type_value() {
			return compare_hands(hands[i], hands[j], false)
		} else {
			return hands[i].get_type_value() < hands[j].get_type_value()
		}
	})

	result := 0
	for i, hand := range hands {
		result += hand.bid * (i + 1)
	}

	return result
}

var all_cards = []rune{'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2'}

func get_J_indexes(cards []rune) []int {
	indexes := []int{}
	for i, card := range cards {
		if card == 'J' {
			indexes = append(indexes, i)
		}
	}
	return indexes
}

func (h *Hand) get_highest_type_value() int {
	max := h.get_type_value()

	hand_cards := make([]rune, len(h.cards))
	copy(hand_cards, h.cards)
	indexes := get_J_indexes(hand_cards)
	for _, card := range all_cards {
		for _, index := range indexes {
			hand_cards[index] = card
		}
		newHand := Hand{hand_cards, 0}
		if max < newHand.get_type_value() {
			max = newHand.get_type_value()
		}
	}

	return max
}

func part_2(filepath string) int {
	hands := get_hands(filepath)

	sort.SliceStable(hands, func(i, j int) bool {
		hands_i_val := hands[i].get_highest_type_value()
		hands_j_val := hands[j].get_highest_type_value()
		if hands_i_val == hands_j_val {
			return compare_hands(hands[i], hands[j], true)
		} else {
			return hands_i_val < hands_j_val
		}
	})

	result := 0
	for i, hand := range hands {
		result += hand.bid * (i + 1)
	}

	return result
}

func main() {

	// Part 1
	fmt.Printf("%v\n", part_1("input.txt"))

	// Part 2
	fmt.Printf("%v\n", part_2("input.txt"))

}
