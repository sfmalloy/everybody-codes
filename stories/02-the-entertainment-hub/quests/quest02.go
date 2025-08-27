package quests

import (
	"os"
)

type Quest02 struct{}

func (q Quest02) Id() uint {
	return 2
}

func (q Quest02) Parse(file *os.File, info os.FileInfo) string {
	input := make([]byte, info.Size())
	file.Read(input)
	return string(input)
}

func (q Quest02) Part1(input string) string {
	return input
}

func (q Quest02) Part2(input string) string {
	return input
}

func (q Quest02) Part3(input string) string {
	return input
}
