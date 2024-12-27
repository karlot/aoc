import sys
import re

def solve(file):
    with open(file, "r") as f:
        content = f.read()

    content = content.strip()

    mul1 = 0
    for nums in re.findall(r"mul\((\d+,\d+)\)", content):
        a, b = map(int, nums.split(","))
        mul1 += int(a) * int(b)

    mul2 = 0
    mul_enabled = True
    for inst in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", content):
        if inst.startswith("mul") and mul_enabled:
            a, b = map(int, inst.strip("mul(").strip(")").split(","))
            mul2 += int(a) * int(b)
        elif inst == "don't()":
            mul_enabled = False
        elif inst == "do()":
            mul_enabled = True

    print(f"Part1: {mul1}")
    print(f"Part2: {mul2}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
