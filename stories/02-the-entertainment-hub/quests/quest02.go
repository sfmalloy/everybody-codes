package quests

import (
	"os"
	"strings"
)

type Quest02 struct{}

func (q Quest02) Id() uint {
	return 2
}

func (q Quest02) Parse(file *os.File, info os.FileInfo) string {
	input := make([]byte, info.Size())
	file.Read(input)
	return strings.Trim(string(input), "\n")
}

func (q Quest02) Part1(input string) int {
	i := 0
	b := 0
	throws := 0
	balloons := "RGB"
	for i < len(input) {
		throws += 1
		for i < len(input) && balloons[b] == input[i] {
			i += 1
		}
		i += 1
		b = (b + 1) % 3
	}
	return throws
}

func (q Quest02) Part2(input string) int {
	return 0
}

func (q Quest02) Part3(input string) int {
	return 0
}
