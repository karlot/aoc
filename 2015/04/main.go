package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func find_number(key string, zeroes int) int {
	search_target := strings.Repeat("0", zeroes)
	number := 0
	for {
		hash := md5.Sum([]byte(key + strconv.Itoa(number)))
		hex := hex.EncodeToString(hash[:])
		if strings.HasPrefix(hex, search_target) {
			return number
		}
		number++
	}
}

func main() {
	b, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Print(err)
		return
	}
	key := string(b)
	fmt.Printf("Part1: %d\n", find_number(key, 5))
	fmt.Printf("Part2: %d\n", find_number(key, 6))
}
