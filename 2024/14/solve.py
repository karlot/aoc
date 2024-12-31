import sys
import re
import math
from dataclasses import dataclass


# Doing this one with "real" robots, kek
@dataclass
class Robot:
    x: int = 0
    y: int = 0
    vx: int = 0
    vy: int = 0
    my: int = 0
    mx: int = 0

    def move(self):
        self.x = (self.x + self.vx) % self.mx
        self.y = (self.y + self.vy) % self.my


# Read robots from the inputs, and generate 
def parse_robots(content: str, gw, gh) -> list[Robot]:
    robots = []
    for line in content.splitlines():
        px, py, vx, vy = map(int, re.findall(r"\-?\d+", line))
        r = Robot(px, py, vx, vy, gh, gw)
        robots.append(r)
    return robots


# Useful for debugging to see positions of robots
def draw_robots(gw, gh, robots: dict[int, Robot]):
    grid = [["." for _ in range(gw)] for _ in range(gh)]
    for r in robots:
        if grid[r.y][r.x] == ".":
            grid[r.y][r.x] = 1
        else:
            grid[r.y][r.x] += 1
    for row in grid:
        print("".join(map(str, row)))
    print()


# Get number of robots per each quadrant excluding middle rows
def get_quadrants(gw, gh, robots: dict[int, Robot]):
    mid_h, mid_w = gh // 2, gw // 2
    q1, q2, q3, q4 = 0, 0, 0, 0

    for r in robots:
        if r.y == mid_h or r.x == mid_w:
            # print("Robot not in any quadrant:", r)
            continue
        elif r.y < mid_h:
            if r.x < mid_w:   q1 += 1
            elif r.x > mid_w: q2 += 1
        elif r.y > mid_h:
            if r.x < mid_w:   q3 += 1
            elif r.x > mid_w: q4 += 1
    return q1, q2, q3, q4


def solve(file: str):
    with open(file, "r") as f:
        content = f.read()

    # Grid dimensions are different for example and real input
    gw, gh = (101, 103) if "input" in file else (11, 7)
    print(f"Grid size: wide={gw}, tall={gh}")

    robots = parse_robots(content, gw, gh)
    # draw_robots(gw, gh, robots)

    elapsed = 100
    for _ in range(elapsed):
        for r in robots: r.move()
    # print("Robots on map after 100 sec:")
    # draw_robots(gw, gh, robots)

    sf = math.prod(get_quadrants(gw, gh, robots))
    print(f"Part 1: {sf} (safety factor after 100 seconds)")

    # Part 2 is really not great, as basically there is no indication about the result
    # Here we need to "guess" max iterations, and observe patterns... since shapes or anything is not really specified
    # I've assumed SF factor from part1 might be key for solving part2, so I tried to find within specific max iterations
    # how SF factor is changed, and it appears that in specific second SF factor is the lowest, meaning distribution of
    # robots is not fully random across all quadrants
    safety_factors = []
    sf_to_elapsed = {}
    while True:
        elapsed += 1
        for r in robots: r.move()
        if elapsed % 10000 == 0: break      # It appears 10.000 seconds is enough to catch pattern

        quadrants = get_quadrants(gw, gh, robots)
        sf = math.prod(quadrants)
        sf_to_elapsed[sf] = elapsed
        safety_factors.append(sf)
    
    sf_tree = min(safety_factors)
    seconds_to_tree = sf_to_elapsed[sf_tree]
    print(f"Part 2: {seconds_to_tree} (minimum seconds after which easter egg is formed)")

    # To print the tree, we need to reset robots and run for exact number of seconds for part2
    robots = parse_robots(content, gw, gh)
    for _ in range(seconds_to_tree):
        for r in robots: r.move()
    draw_robots(gw, gh, robots)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
