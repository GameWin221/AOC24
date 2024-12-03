package main

import (
	"fmt"
	"time"
)

func main() {
    start := time.Now()
    answer := part2()
    elapsed := time.Since(start)

    fmt.Println(answer, "took:", elapsed)
}
