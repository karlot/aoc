import sys
import re
import time


def process_input(content: str) -> list:
    machines = []
    for machine_block in content.split("\n\n"):
        machine_lines = machine_block.splitlines()
        btnA = re.match(r"Button A: X\+(\d+), Y\+(\d+)", machine_lines[0]).groups()
        btnB = re.match(r"Button B: X\+(\d+), Y\+(\d+)", machine_lines[1]).groups()
        prize = re.match(r"Prize: X=(\d+), Y=(\d+)", machine_lines[2]).groups()
        machines.append((
            tuple(int(btn) for btn in btnA),    # button A location distance (x,y)
            tuple(int(btn) for btn in btnB),    # button B location distance (x,y)
            tuple(int(loc) for loc in prize),   # button C location (x,y)
        ))
    return machines


# Attempt to brute-force solution (works for part1, with maximum number of button presses)
def brute(machine):
    (ax, ay), (bx, by), (px, py) = machine
    tokens = None
    for a in range(101):
        for b in range(101):
            prizeX = (a * ax) + (b * bx)
            prizeY = (a * ay) + (b * by)
            if prizeX == px and prizeY == py:
                sol_tokens = (a * 3) + b
                tokens = sol_tokens if tokens == None else min(tokens, sol_tokens)
    return tokens if tokens else 0


# Doing some linear algebra stuff, had to dig trough wikipedia for "Cramer's rule"
# https://en.wikipedia.org/wiki/Cramer%27s_rule
def linear_alg(machine, prize_offset=0):
    (ax, ay), (bx, by), (px, py) = machine
    px += prize_offset
    py += prize_offset

    na = (px * by - py * bx) / (ax * by - ay * bx)
    nb = (py * ax - px * ay) / (ax * by - ay * bx)

    if int(na) == na and int(nb) == nb:
        return int(na) * 3 + int(nb)
    else:
        return 0


def solve(file):
    with open(file, "r") as f:
        content = f.read()

    machines = process_input(content)

    # Part 1 - initial attempt
    t1 = time.perf_counter()
    tokens = sum(brute(m) for m in machines)
    t2 = time.perf_counter()
    print("-" * 60)
    print("Brute-force attempt:")
    print(f"Part 1: {tokens:<16} took: {round(t2 - t1, 9):.9f} sec", )

    # Part 1 - rework
    print("-" * 60)
    print("Linear-algebra attempt:")
    t1 = time.perf_counter()
    tokens = sum(linear_alg(m) for m in machines)
    t2 = time.perf_counter()
    print(f"Part 1: {tokens:<16} took: {round(t2 - t1, 9):.9f} sec", )

    # Part 2 with prize offset
    prize_offset = 10_000_000_000_000
    t1 = time.perf_counter()
    tokens = sum(linear_alg(m, prize_offset) for m in machines)
    t2 = time.perf_counter()
    print(f"Part 2: {tokens:<16} took: {round(t2 - t1, 9):.9f} sec", )
    print("-" * 60)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
