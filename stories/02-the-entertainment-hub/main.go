package main

import (
	"flag"
	"fmt"
	"os"
	"time"

	"github.com/sfmalloy/everybody-codes/lib"
	"github.com/sfmalloy/everybody-codes/quests"
)

func main() {
	var args = lib.ParseArgs()
	if args.Quest == 0 {
		flag.PrintDefaults()
		return
	}

	switch args.Quest {
	case 1:
		runQuest(quests.Quest01{}, args.Part, args.IsTest)
	case 2:
		runQuest(quests.Quest02{}, args.Part, args.IsTest)
	case 3:
		runQuest(quests.Quest03{}, args.Part, args.IsTest)
	default:
		panic("Quest must be an int between 1 and 3 inclusive")
	}
}

func runQuest[I any, O any](quest quests.Quest[I, O], part uint, test bool) {
	var partFn func(I) O
	switch part {
	case 0:
		runQuest(quest, 1, test)
		runQuest(quest, 2, test)
		runQuest(quest, 3, test)
		return
	case 1:
		partFn = quest.Part1
	case 2:
		partFn = quest.Part2
	case 3:
		partFn = quest.Part3
	}

	var filename string
	if test {
		filename = "inputs/test.txt"
	} else {
		filename = fmt.Sprintf("inputs/quest0%d/part0%d.txt", quest.Id(), part)
	}

	file, err := os.Open(filename)
	if err != nil {
		panic("Failed to open input file")
	}
	info, err := file.Stat()
	if err != nil {
		panic("Failed to read file info")
	}

	start := time.Now()
	input := quest.Parse(file, info, part)
	res := partFn(input)
	end := time.Since(start)
	fmt.Println(res)
	fmt.Printf("Time: %.03fms\n", float64(end.Microseconds())/1000)
}
