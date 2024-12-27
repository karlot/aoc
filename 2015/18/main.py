# from pprint import pp
from copy import deepcopy

with open("input.txt") as file:
    lines = file.read().strip().splitlines()

grid = [[1 if c == "#" else 0 for c in line] for line in lines]
rows = len(grid)
cols = len(grid[0])

def print_grid(g):
    for r in g:
        print(r)
    print()

def animate(g, part=1):
    ng = deepcopy(g)
    for y, row in enumerate(g):
        for x, light in enumerate(row):
            if part == 2:
                if (y == 0 and x == 0) or \
                   (y == 0 and x == cols-1) or \
                   (y == rows-1 and x == 0) or \
                   (y == rows-1 and x == cols-1):
                    continue
            n_on = 0
            # Check around:   UL      U     UR     R     DR    D     DL     L
            for dy, dx in  [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]:
                ny, nx = y + dy, x + dx
                if ny < 0 or ny > rows-1 or nx < 0 or nx > cols-1 or g[ny][nx] == 0:
                    continue
                n_on += 1
            # Check current light state
            if light == 1:
                if n_on == 2 or n_on == 3:
                    ng[y][x] = 1
                else:
                    ng[y][x] = 0
            else:
                if n_on == 3:
                    ng[y][x] = 1
                else:
                    ng[y][x] = 0
    return ng
# -------------------------------------------------------------------------------------------------

steps = 100

for _ in range(steps):
    grid = animate(grid, part=1)

print(f"Part1: {sum([sum(row) for row in grid])}")


# Reset grid for p2
grid = [[1 if c == "#" else 0 for c in line] for line in lines]
for _ in range(steps):
    grid = animate(grid, part=2)

print(f"Part2: {sum([sum(row) for row in grid])}")
