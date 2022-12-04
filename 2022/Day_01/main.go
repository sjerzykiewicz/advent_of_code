package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "io"
    "strconv"
    "sort"
)

func main() {
    file, err := os.Open("input.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    reader := bufio.NewReader(file)
    calories := []int{0}
    i := 0
    for {
        line, _, err := reader.ReadLine()
        if err == io.EOF {
            break
        }

        lineStr := string(line[:])
        if len(line) == 0 {
            i++
            calories = append(calories, 0)
        } else {
            calorie, _ := strconv.Atoi(lineStr)
            calories[i] += calorie
        }
    }

    sort.Ints(calories)

    // Part 1
    fmt.Printf("%v\n", calories[len(calories)-1])

    // Part 2
    sum := calories[len(calories)-1] + calories[len(calories)-2] + calories[len(calories)-3]
    fmt.Printf("%v\n", sum)
}