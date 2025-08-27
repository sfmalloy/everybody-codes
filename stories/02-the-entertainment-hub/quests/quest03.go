package quests

import (
	"os"
)

type Quest03 struct{}

func (q Quest03) Id() uint {
	return 3
}

func (q Quest03) Parse(file *os.File, info os.FileInfo) string {
	input := make([]byte, info.Size())
	file.Read(input)
	return string(input)
}

func (q Quest03) Part1(input string) string {
	return input
}

func (q Quest03) Part2(input string) string {
	return input
}

func (q Quest03) Part3(input string) string {
	return input
}
