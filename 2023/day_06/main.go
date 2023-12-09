package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"os"
	"strconv"
)

type Race struct {
	time     int
	distance int
}

func get_races(filepath string) []Race {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	times := []int{}
	distances := []int{}
	for scanner.Scan() {
		if bytes.Contains(scanner.Bytes(), []byte("Time")) {
			splitted := bytes.Split(scanner.Bytes(), []byte(":"))
			times_bytes := bytes.Split(splitted[1], []byte(" "))
			for _, time := range times_bytes {
				time_int, err := strconv.Atoi(string(time))
				if err == nil {
					times = append(times, time_int)
				}
			}
		}
		if bytes.Contains(scanner.Bytes(), []byte("Distance")) {
			splitted := bytes.Split(scanner.Bytes(), []byte(":"))
			distances_bytes := bytes.Split(splitted[1], []byte(" "))
			for _, distance := range distances_bytes {
				distance_int, err := strconv.Atoi(string(distance))
				if err == nil {
					distances = append(distances, distance_int)
				}
			}
		}
	}

	races := []Race{}

	for i, time := range times {
		races = append(races, Race{time, distances[i]})
	}

	return races
}

func (r *Race) get_number_of_ways_to_win() int {
	var start int
	var end int
	for ms := 0; ms < r.time; ms++ {
		if r.distance < (r.time-ms)*ms {
			start = ms
			break
		}
	}
	for ms := r.time; ms > 0; ms-- {
		if r.distance < (r.time-ms)*ms {
			end = ms
			break
		}
	}
	return end - start + 1
}

func part_1(filepath string) int {
	races := get_races(filepath)

	result := 1
	for _, race := range races {
		result *= race.get_number_of_ways_to_win()
	}

	return result
}

func part_2(filepath string) int {
	races := get_races(filepath)

	var new_time bytes.Buffer
	var new_distance bytes.Buffer
	for _, race := range races {
		new_time.WriteString(fmt.Sprint(race.time))
		new_distance.WriteString(fmt.Sprint(race.distance))
	}

	time, _ := strconv.Atoi(new_time.String())
	distance, _ := strconv.Atoi(new_distance.String())

	race := Race{time, distance}

	return race.get_number_of_ways_to_win()
}

func main() {

	// Part 1
	fmt.Printf("%v\n", part_1("input.txt"))

	// Part 2
	fmt.Printf("%v\n", part_2("input.txt"))

}
