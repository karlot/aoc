import std/strutils
import checksums/md5

proc readkey(): string =
  let f = open("input.txt")
  defer: f.close()
  result = f.readLine()

proc find_number(key: string, zeroes: uint): int =
    result = 0
    let search_pattern = "0".repeat(zeroes)
    while true:
        if getMD5(key & result.intToStr()).startsWith(search_pattern):
            break
        inc result

let key = readkey()
echo "Part1: ", find_number(key, 5)
echo "Part2: ", find_number(key, 6)