# Regex style
import re
with open("input.txt") as file:
    lines = file.read().strip().splitlines()

# Part1 checkers
r1 = re.compile(r".*(?:[aeiou].*){3,}")     # Minimum 3 vowels (a, e, i, o, u)
r2 = re.compile(r".*(\w)\1+")               # Contains pairs of characters like "aa" or "xx"
r3 = re.compile(r".*(?:ab|cd|pq|xy)")       # Contains forbidden words (ab, cd, pq, or xy)

# Part2 checkers
r4 = re.compile(r".*(.{2}).*?\1")           # Pair of chars that appear again, like "abab" or "abcab"
r5 = re.compile(r".*(.)(.)\1")              # Matches repeating letter after once char, like "xyx" or "efe"

print(f"Part1: {sum([1 for l in lines if r1.match(l) and r2.match(l) and not r3.match(l)])}")
print(f"Part2: {sum([1 for l in lines if r4.match(l) and r5.match(l)])}")
