package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"os"
	"strconv"
)

type AlmanacMap struct {
	source     int64
	difference int64
	n          int64
}

type Almanac struct {
	seeds []int64
	maps  [][]AlmanacMap
}

func resolve_almanac(filepath string) Almanac {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	almanac := Almanac{}
	maps_list := [][]AlmanacMap{}
	blanks_cnt := 0
	for scanner.Scan() {
		if scanner.Text() == "" {
			blanks_cnt++
			maps_list = append(maps_list, []AlmanacMap{})
		} else {
			if blanks_cnt == 0 {
				splitted := bytes.Split(scanner.Bytes(), []byte(":"))
				seeds_bytes := bytes.Split(splitted[1], []byte(" "))
				seeds := []int64{}
				for _, seed := range seeds_bytes {
					seed_int, err := strconv.ParseInt(string(seed), 10, 64)
					if err == nil {
						seeds = append(seeds, seed_int)
					}
				}
				almanac.seeds = seeds
			} else {
				if bytes.Contains(scanner.Bytes(), []byte("map")) {
					continue
				}

				numbers_bytes := bytes.Split(scanner.Bytes(), []byte(" "))
				dest, _ := strconv.ParseInt(string(numbers_bytes[0]), 10, 64)
				source, _ := strconv.ParseInt(string(numbers_bytes[1]), 10, 64)
				n, _ := strconv.ParseInt(string(numbers_bytes[2]), 10, 64)
				maps_list[blanks_cnt-1] = append(maps_list[blanks_cnt-1], AlmanacMap{source, dest - source, n})
			}
		}
	}
	almanac.maps = maps_list

	return almanac
}

func (a *Almanac) get_seed_location(seed int64) int64 {
	current_id := seed
	for _, almanac_map := range a.maps {
		for _, a_map := range almanac_map {
			if current_id >= a_map.source && current_id < a_map.source+a_map.n {
				current_id = current_id + a_map.difference
				break
			}
		}
	}

	return current_id
}

func part_1(filepath string) int64 {
	almanac := resolve_almanac(filepath)
	min_loc := almanac.get_seed_location(almanac.seeds[0])
	for _, seed := range almanac.seeds {
		min_loc = min(min_loc, almanac.get_seed_location(seed))
	}

	return min_loc
}

func part_2(filepath string) int64 {
	almanac := resolve_almanac(filepath)
	min_loc := almanac.get_seed_location(almanac.seeds[0])
	var start int64
	for i, seed := range almanac.seeds {
		if i%2 == 0 {
			start = seed
		} else {
			for j := start; j < start+seed; j++ {
				min_loc = min(min_loc, almanac.get_seed_location(j))
			}
		}
	}

	return min_loc
}

func main() {

	// Part 1
	fmt.Printf("%v\n", part_1("input.txt"))

	// Part 2
	fmt.Printf("%v\n", part_2("input.txt"))

}
