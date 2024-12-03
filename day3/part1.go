package main

import (
	"os"
	"regexp"
	"strconv"
	"strings"
)

func part1() int64 {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}

	dataStr := string(data)

	mulReg, _ := regexp.Compile("mul\\([0-9]{1,3},[0-9]{1,3}\\)")
	matchedSlices := mulReg.FindAllStringIndex(dataStr, -1)

	var result int64 = 0

	for i := 0; i < len(matchedSlices); i += 1 {
		numsCommaText := dataStr[matchedSlices[i][0]+4 : matchedSlices[i][1]-1]
		numsText := strings.Split(numsCommaText, ",")
		a, _ := strconv.ParseInt(numsText[0], 10, 64)
		b, _ := strconv.ParseInt(numsText[1], 10, 64)

		result += a * b
	}	

	return result
}