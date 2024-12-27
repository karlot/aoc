import sys
import re

def solve(file):
    with open(file, "r") as f:
        content = f.read()

    content = content.strip()
    lines = content.splitlines()
    grid = [[c for c in l] for l in lines]
    h = len(grid)
    w = len(grid[0])

    p1 = 0
    for y in range(h):
        for x in range(w):
            # print("pos", x,y)
            # print(w-x)
            if w-x > 3 and ((
                grid[y][x] == "X" and grid[y][x+1] == "M" and grid[y][x+2] == "A" and grid[y][x+3] == "S") or (
                grid[y][x] == "S" and grid[y][x+1] == "A" and grid[y][x+2] == "M" and grid[y][x+3] == "X")):
                # print("horizontal at",x,y)
                p1 += 1
            if h-y > 3 and ((
                grid[y][x] == "X" and grid[y+1][x] == "M" and grid[y+2][x] == "A" and grid[y+3][x] == "S") or (
                grid[y][x] == "S" and grid[y+1][x] == "A" and grid[y+2][x] == "M" and grid[y+3][x] == "X")):
                # print("vertical at",x,y)
                p1 += 1
            if h-y > 3 and w-x > 3 and ((
                grid[y][x] == "X" and grid[y+1][x+1] == "M" and grid[y+2][x+2] == "A" and grid[y+3][x+3] == "S") or (
                grid[y][x] == "S" and grid[y+1][x+1] == "A" and grid[y+2][x+2] == "M" and grid[y+3][x+3] == "X")):
                # print("diagonal at",x,y)
                p1 += 1
            if y >= 3 and w-x > 3 and ((
                grid[y][x] == "X" and grid[y-1][x+1] == "M" and grid[y-2][x+2] == "A" and grid[y-3][x+3] == "S") or (
                grid[y][x] == "S" and grid[y-1][x+1] == "A" and grid[y-2][x+2] == "M" and grid[y-3][x+3] == "X")):
                # print("diagonal2 at",x,y)
                p1 += 1

    print(f"Part1: {p1}")

    p2 = 0
    for y in range(h):
        for x in range(w):
            if y == 0 or y > h-2 or x == 0 or x > w-2: continue
            # print("pos", x,y)
            if ((grid[y-1][x-1] == "M" and grid[y][x] == "A" and grid[y+1][x+1] == "S") or (grid[y-1][x-1] == "S" and grid[y][x] == "A" and grid[y+1][x+1] == "M")) and (
                (grid[y-1][x+1] == "M" and grid[y][x] == "A" and grid[y+1][x-1] == "S") or (grid[y-1][x+1] == "S" and grid[y][x] == "A" and grid[y+1][x-1] == "M")):
                p2 += 1

    print(f"Part2: {p2}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
