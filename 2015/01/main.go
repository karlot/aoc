package main

import (
	"fmt"
	"os"
)

func main() {
	b, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Print(err)
		return
	}
	str := string(b) // convert content to a 'string'

	floors := 0
	bii := 0
	for i, c := range str {
		if c == '(' {
			floors++
		}
		if c == ')' {
			floors--
		}
		if floors < 0 {
			if bii == 0 {
				bii = i + 1
			}
		}
	}
	fmt.Println("Part1: ", floors)
	fmt.Println("Part2: ", bii)
}
