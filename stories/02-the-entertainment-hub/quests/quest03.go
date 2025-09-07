package quests

import (
	"fmt"
	"os"
	"regexp"
	"slices"
	"strconv"
	"strings"
)

type Quest03 struct{}

func (q Quest03) Id() uint {
	return 3
}

type Input struct {
	dice      []Die
	racetrack []int
}

type Die struct {
	faces      []int
	seed       int
	pulse      int
	pos        int
	trackIndex int
}

func (q Quest03) Parse(file *os.File, info os.FileInfo, part uint) Input {
	input := make([]byte, info.Size())
	file.Read(input)

	val := Input{
		dice:      make([]Die, 0),
		racetrack: make([]int, 0),
	}
	for line := range strings.Lines(string(input)) {
		if len(line) == 0 {
			continue
		} else if !strings.Contains(line, ":") {
			line = strings.TrimRight(line, "\n")
			for _, c := range line {
				spot, err := strconv.ParseInt(fmt.Sprintf("%c", c), 10, 32)
				if err != nil {
					panic("failed to parse racetrack int")
				}
				val.racetrack = append(val.racetrack, int(spot))
			}
			continue
		}
		facesPattern, err := regexp.Compile(`\[(-?[0-9]+,?)+\]`)
		if err != nil {
			panic("faces regex failed to compile")
		}
		facesLine := facesPattern.FindString(line)
		faces := strings.Split(facesLine[1:len(facesLine)-1], ",")

		seedPattern, err := regexp.Compile(`seed=-?[0-9]+`)
		if err != nil {
			panic("faces")
		}

		seedLine := seedPattern.FindString(line)
		seed, err := strconv.ParseInt(seedLine[5:], 10, 32)
		if err != nil {
			panic("failed to parse seed int")
		}

		die := Die{
			faces: make([]int, len(faces)),
			seed:  int(seed),
			pulse: int(seed),
			pos:   0,
		}
		for i, face := range faces {
			v, err := strconv.ParseInt(face, 10, 32)
			if err != nil {
				panic("failed to parse int")
			}
			die.faces[i] = int(v)
		}
		val.dice = append(val.dice, die)
	}
	return val
}

func (q Quest03) Part1(input Input) string {
	score := 0
	rollNumber := 1
	for score < 10000 {
		for i := range input.dice {
			score += roll(&input.dice[i], rollNumber)
		}
		rollNumber += 1
	}
	return fmt.Sprintf("%d", rollNumber-1)
}

type Placement struct {
	index     int
	runLength int
}

func (q Quest03) Part2(input Input) string {
	placements := make([]Placement, len(input.dice))
	for i := range input.dice {
		rollNumber := 1
		for input.dice[i].trackIndex < len(input.racetrack) {
			r := roll(&input.dice[i], rollNumber)
			if r == input.racetrack[input.dice[i].trackIndex] {
				input.dice[i].trackIndex += 1
			}
			rollNumber += 1
		}
		println(rollNumber - 1)
		placements[i] = Placement{
			index:     i + 1,
			runLength: rollNumber - 1,
		}
	}
	slices.SortFunc(placements, func(a, b Placement) int {
		return a.runLength - b.runLength
	})
	res := ""
	for _, die := range placements {
		res += fmt.Sprintf("%d,", die.index)
	}
	return res[:len(res)-1]
}

func (q Quest03) Part3(input Input) string {
	return "a"
}

func roll(d *Die, rollNumber int) int {
	spin := rollNumber * d.pulse
	d.pos += spin
	d.pulse = d.pulse + spin
	d.pulse = d.pulse % d.seed
	d.pulse = d.pulse + 1 + rollNumber + d.seed
	return d.faces[d.pos%len(d.faces)]
}
