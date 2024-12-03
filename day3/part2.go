package main

import (
	"os"
	"regexp"
	"strconv"
	"strings"
)

func part2() int64 {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}

	dataStr := string(data)

	correctData := "";

	doNow := true
	lastDoIndex := 0

	for i := 7; i <= len(dataStr); i += 1 {
		if dataStr[i-4:i] == "do()" {
			if !doNow {
				lastDoIndex = i
			}

			doNow = true
		} else if dataStr[i-7:i] == "don't()" {
			if doNow {
				correctData += dataStr[lastDoIndex : i-7]
			}

			doNow = false
		}
	}

	if doNow {
		correctData += dataStr[lastDoIndex : ]
	}

	var result int64 = 0

	mulReg, _ := regexp.Compile("mul\\([0-9]{1,3},[0-9]{1,3}\\)")
	matchedSlices := mulReg.FindAllStringIndex(correctData, -1)
	
	for i := 0; i < len(matchedSlices); i += 1 {
		numsCommaText := correctData[matchedSlices[i][0]+4 : matchedSlices[i][1]-1]
		numsText := strings.Split(numsCommaText, ",")
		a, _ := strconv.ParseInt(numsText[0], 10, 64)
		b, _ := strconv.ParseInt(numsText[1], 10, 64)

		result += a * b
	}

	return result
}