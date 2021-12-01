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

func sum(numbers []int) (total int) {
    total = 0
    for _, n := range numbers {
        total += n
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
        if i >= 3 && sum(numbers[i-3:i]) < sum(numbers[i-2:i+1]) {
            part2 += 1
        }
    }

    fmt.Println("Part 1:", part1)
    fmt.Println("Part 2:", part2)
}

