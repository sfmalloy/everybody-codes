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

func (q Quest01) Parse(file *os.File, info os.FileInfo, _part uint) BoardSequence {
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
	scores := make([][]int, len(input.instructions))
	for i, seq := range input.instructions {
		scores[i] = make([]int, 1+len(input.board[0])/2)
		for c := 0; c < len(input.board[0]); c += 2 {
			scores[i][c/2] = drop(input.board, seq, c)
		}
	}
	best := getBestScores(scores, len(input.instructions))
	return fmt.Sprintf("%d %d", best.lo, best.hi)
}

func drop(board []string, sequence string, startCol int) int {
	r := 0
	c := startCol
	s := 0
	for r < len(board) {
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

type Pair struct {
	hi int
	lo int
}

func getBestScores(scores [][]int, depthLimit int) Pair {
	return calculateScores(scores, 0, Pair{-1, -1}, 0, depthLimit, make(map[int]bool))
}

func calculateScores(scores [][]int, score int, best Pair, seqIndex int, depthLimit int, seen map[int]bool) Pair {
	if seqIndex == depthLimit {
		if best.hi == -1 {
			best.hi = score
		} else {
			best.hi = max(best.hi, score)
		}

		if best.lo == -1 {
			best.lo = score
		} else {
			found := 0
			for _, v := range seen {
				if v {
					found += 1
				}
			}
			best.lo = min(best.lo, score)
		}
		return best
	}

	for i := 0; i < len(scores[seqIndex]); i++ {
		if !seen[i] {
			seen[i] = true
			best = calculateScores(scores, score+scores[seqIndex][i], best, seqIndex+1, depthLimit, seen)
			seen[i] = false
		}
	}
	return best
}
