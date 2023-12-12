package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"math/big"
	"os"
	"strings"
)

type Node struct {
	left  string
	right string
}

type NodeMap struct {
	path  []int
	nodes map[string]Node
}

func getMap(filepath string) NodeMap {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	nodeMap := NodeMap{}
	nodeMap.nodes = map[string]Node{}
	blank_line := false
	for scanner.Scan() {
		if scanner.Text() == "" {
			blank_line = true
			continue
		}
		if !blank_line {
			path_bytes := strings.Split(scanner.Text(), "")
			for _, path_byte := range path_bytes {
				if path_byte == "L" {
					nodeMap.path = append(nodeMap.path, 0)
				} else if path_byte == "R" {
					nodeMap.path = append(nodeMap.path, 1)
				}
			}
		} else {
			splitted := bytes.Split(scanner.Bytes(), []byte(" = "))
			name := string(splitted[0])
			node := Node{}
			where := bytes.Split(splitted[1], []byte(", "))
			node.left = strings.Trim(string(where[0]), "(")
			node.right = strings.Trim(string(where[1]), ")")
			nodeMap.nodes[name] = node
		}
	}

	return nodeMap
}

func (n *NodeMap) getThrought(start, end string) int {
	cnt := 0
	curr := start
	i := 0
	for {
		if curr == end {
			break
		}
		if i == len(n.path) {
			i = 0
		}
		if n.path[i] == 0 {
			curr = n.nodes[curr].left
		} else {
			curr = n.nodes[curr].right
		}
		i++
		cnt++
	}

	return cnt
}

func part_1(filepath string) int {
	nodeMap := getMap(filepath)

	return nodeMap.getThrought("AAA", "ZZZ")
}

func (n *NodeMap) getCycles() []int {
	starting_points := map[string]int{}
	i := 0
	for name, _ := range n.nodes {
		if name[2] == 'A' {
			starting_points[name] = i
		}
	}

	current := starting_points
	cycles := []int{}
	i = 0
	for {
		if len(current) == 0 {
			break
		}
		if i == len(n.path) {
			i = 0
		}
		new_curr := map[string]int{}
		for name, id := range current {
			if name[2] == 'Z' {
				cycles = append(cycles, id)
				delete(current, name)
				continue
			}
			if n.path[i] == 0 {
				new_curr[n.nodes[name].left] = id + 1
			} else {
				new_curr[n.nodes[name].right] = id + 1
			}
		}
		current = new_curr
		i++
	}

	return cycles
}

func gcd(a, b *big.Int) *big.Int {
	if b.Sign() == 0 {
		return a
	}
	temp := new(big.Int)
	temp.Set(a)
	temp.Mod(a, b)
	return gcd(b, temp)
}

func lcm(a, b *big.Int) *big.Int {
	temp := new(big.Int)
	temp.Mul(a, b)
	gcdAB := gcd(a, b)
	return temp.Div(temp, gcdAB)
}

func lcmSlice(numbers []int) *big.Int {
	if len(numbers) == 0 {
		return nil
	}

	result := big.NewInt(int64(numbers[0]))
	for _, num := range numbers[1:] {
		result.Set(lcm(result, big.NewInt(int64(num))))
	}

	return result
}

func part_2(filepath string) int {
	nodeMap := getMap(filepath)

	cycles := nodeMap.getCycles()

	return int(lcmSlice(cycles).Int64())
}

func main() {

	// Part 1
	fmt.Printf("%v\n", part_1("input.txt"))

	// Part 2
	fmt.Printf("%v\n", part_2("input.txt"))

}
