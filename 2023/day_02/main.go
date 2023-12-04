package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"os"
	"strconv"
)

var max_red_cubes = 12
var max_green_cubes = 13
var max_blue_cubes = 14

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

type Round struct {
	red_cubes_count int
	green_cubes_count int
	blue_cubes_count int
}

func get_round(round_bytes []byte) Round {
	round := Round{}
	round_bytes_ := bytes.Split(round_bytes, []byte(","))
	for _, cube := range round_bytes_ {
		if bytes.Contains(cube, []byte("red")) {
			red_cubes_count, _ := strconv.Atoi(string(bytes.Split(cube, []byte(" "))[1]))
			round.red_cubes_count = red_cubes_count
		}
		if bytes.Contains(cube, []byte("green")) {
			green_cubes_count, _ := strconv.Atoi(string(bytes.Split(cube, []byte(" "))[1]))
			round.green_cubes_count = green_cubes_count
		}
		if bytes.Contains(cube, []byte("blue")) {
			blue_cubes_count, _ := strconv.Atoi(string(bytes.Split(cube, []byte(" "))[1]))
			round.blue_cubes_count = blue_cubes_count
		}
	}
	return round
}

type Game struct {
	id int
	rounds []Round
}

func (g *Game) all_rounds_possible() bool {
	for _, round := range g.rounds {
		if round.red_cubes_count > max_red_cubes || round.green_cubes_count > max_green_cubes || round.blue_cubes_count > max_blue_cubes {
			return false
		}
	}
	return true
}

func (g *Game) least_cubes_needed() int {
	max_red_cubes := 0
	max_green_cubes := 0
	max_blue_cubes := 0
	for _, round := range g.rounds {
		max_red_cubes = Max(round.red_cubes_count, max_red_cubes)
		max_green_cubes = Max(round.green_cubes_count, max_green_cubes)
		max_blue_cubes = Max(round.blue_cubes_count, max_blue_cubes)
	}
	return max_red_cubes * max_green_cubes * max_blue_cubes
}

func get_games(filepath string) []Game {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	games := []Game{}
	for scanner.Scan() {
		splitted := bytes.Split(scanner.Bytes(), []byte(":"))
		game_id := splitted[0]
		rounds_bytes := splitted[1]
		game_id_int, _ := strconv.Atoi(string(bytes.Split(game_id, []byte(" "))[1]))
		rounds_bytes_ := bytes.Split(rounds_bytes, []byte(";"))
		rounds := []Round{}
		for _, round_bytes := range rounds_bytes_ {
			round := get_round(round_bytes)
			rounds = append(rounds, round)
		}
		games = append(games, Game{game_id_int, rounds})
	}
	return games
}

func part_1(filepath string) int {
	games := get_games(filepath)

	sum := 0
	for _, game := range games {
		if game.all_rounds_possible() {
			sum += game.id
		}
	}
	return sum
}

func part_2(filepath string) int {
	games := get_games(filepath)

	sum := 0
	for _, game  := range games {
		sum += game.least_cubes_needed()
	}
	return sum
}


func main() {

	// Part 1
	fmt.Printf("%v\n", part_1("input.txt"))

	// Part 2
	fmt.Printf("%v\n", part_2("input.txt"))

}
