package quests

import (
	"os"
	"strings"
)

type Quest02 struct{}

func (q Quest02) Id() uint {
	return 2
}

func (q Quest02) Parse(file *os.File, info os.FileInfo, _part uint) string {
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

type Balloon struct {
	symbol byte
	next   *Balloon
}

type BalloonListActions interface {
	Push(symbol byte)
	Pop(i int) *Balloon
	Get(i int) *Balloon
}

type BalloonList struct {
	len   int
	front *Balloon
	back  *Balloon
}

func (list *BalloonList) Push(symbol byte) {
	b := new(Balloon)
	b.symbol = symbol
	if list.front == nil {
		list.front = b
	} else {
		list.back.next = b
	}
	list.back = b
	b.next = list.front
	list.len += 1
}

func (list *BalloonList) Pop(i int) *Balloon {
	a := list.front
	b := list.front
	for range i {
		a = b
		b = b.next
	}
	if b == list.front {
		list.front = list.front.next
	}
	if b == list.back {
		list.back = a
	}
	a.next = b.next
	b.next = nil
	list.len -= 1
	return b
}

func (list *BalloonList) Get(i int) *Balloon {
	b := list.front
	for range i {
		b = b.next
	}
	return b
}

func (q Quest02) Part2(input string) int {
	return ClearList(100, input)
}

func (q Quest02) Part3(input string) int {
	return 0
}

func ClearList(reps int, input string) int {
	list := BalloonList{}
	for r := range reps {
		println(r)
		for i := range len(input) {
			list.Push(input[i])

			a := list.front
			b := a.next
			for b != a {
				b = b.next
			}
		}
	}

	darts := "RGB"
	b := 0
	throws := 0
	for list.len > 0 {
		println(list.len)
		throws += 1
		if list.len%2 == 0 && list.front.symbol == darts[b] {
			list.Pop(list.len / 2)
		}
		list.Pop(0)
		b = (b + 1) % 3
	}
	return throws
}
