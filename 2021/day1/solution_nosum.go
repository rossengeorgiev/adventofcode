package main

import (
    "os"
    "io"
    "fmt"
)


func check(e error) {
    if e != nil {
        panic(e)
    }
}

func getNumbers(path string) (numbers []int) {
    f, err := os.Open(path)
    check(err)

    var number int
    for {
        _, err := fmt.Fscanf(f, "%d\n", &number)

        if err == io.EOF {
            return
        } else {
            check(err)
        }

        numbers = append(numbers, number)
    }

    return
}

func main() {
    numbers := getNumbers("./input.txt")

    part1, part2 := 0, 0

    for i, number := range numbers {
        if i > 0 && number > numbers[i-1] {
            part1 += 1
        }

        // sliding window of 3 elements
        // we don't need to sum the windows, since they overlap, except for one item
        // thus we simply compare the diff between that one item
        // [ 1 [[ 2 3 ] 4 ]] = 1 < 4
        if i >= 3 && number > numbers[i-3] {
            part2 += 1
        }
    }

    fmt.Println("Part 1:", part1)
    fmt.Println("Part 2:", part2)
}

