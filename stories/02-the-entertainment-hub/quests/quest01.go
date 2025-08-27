package quests

import (
	"fmt"
	"os"
	"strings"
)

type Quest01 struct{}

type BoardSequence struct {
	board        []string
	instructions []string
}

func (q Quest01) Id() uint {
	return 1
}

func (q Quest01) Parse(file *os.File, info os.FileInfo) BoardSequence {
	bytes := make([]byte, info.Size())
	file.Read(bytes)
	args := strings.Split(strings.TrimRight(string(bytes), "\n"), "\n\n")
	return BoardSequence{
		board:        strings.Split(args[0], "\n"),
		instructions: strings.Split(args[1], "\n"),
	}
}

func (q Quest01) Part1(input BoardSequence) string {
	total := 0
	c := 0
	for _, seq := range input.instructions {
		res := drop(input.board, seq, c)
		total += res
		c += 2
	}
	return fmt.Sprintf("%d", total)

}

func (q Quest01) Part2(input BoardSequence) string {
	total := 0
	for _, seq := range input.instructions {
		best := 0
		for c := 0; c < len(input.board[0]); c += 2 {
			best = max(best, drop(input.board, seq, c))
		}
		total += best
	}
	return fmt.Sprintf("%d", total)
}

func (q Quest01) Part3(input BoardSequence) string {
	// 1. precalculate all token values
	// 2. BFS to the highest/lowest
	hi := 0
	lo := 0
	return fmt.Sprintf("%d %d", hi, lo)
}

func drop(board []string, sequence string, startCol int) int {
	r := 0
	c := startCol
	s := 0
	for r < len(board) {
		// fmt.Println(r, c)
		if board[r][c] == '*' {
			delta := 0
			if sequence[s] == 'R' {
				delta = 1
			} else {
				delta = -1
			}
			s += 1

			if c+delta >= len(board[0]) || c+delta < 0 {
				delta *= -1
			}
			c += delta
		} else {
			r += 1
		}
	}

	start := (startCol + 2) / 2
	end := (c + 2) / 2
	return max(0, end*2-start)
}
