package quests

import "os"

type Quest[I any, O any] interface {
	Id() uint
	Parse(file *os.File, info os.FileInfo) I
	Part1(input I) O
	Part2(input I) O
	Part3(input I) O
}
