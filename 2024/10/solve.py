import sys
from collections import deque


def solve(file):
    with open(file, "r") as f:
        content = f.read()
    content = content.strip()
    lines = content.splitlines()
    grid = [[int(c) for c in l] for l in lines]
    rows = len(grid)
    cols = len(grid[0])

    trailheads = []
    for r, row in enumerate(grid):
        for c, h in enumerate(row):
            if h == 0:
                trailheads.append((r,c))
    # print(trailheads)

    def find_ends(y, x):
        paths = deque([(y,x)])
        seen = {(y,x): 1}
        ends = 0
        unique = 0

        while len(paths) > 0:
            cy, cx = paths.popleft()
            if grid[cy][cx] == 9:
                ends += 1
                unique += seen[(cy, cx)]
            dirs = [(cy - 1, cx), (cy, cx + 1), (cy + 1, cx), (cy, cx - 1)]
            for ny, nx in dirs:
                if ny < 0 or nx < 0 or ny >= rows or nx >= cols:
                    # out of map
                    continue
                if grid[ny][nx] != grid[cy][cx] + 1:
                    # not a valid path (not going up)
                    continue
                if (ny, nx) in seen:
                    # Skip same path
                    seen[(ny, nx)] += seen[(cy, cx)]
                    continue
                seen[(ny, nx)] = seen[(cy, cx)]
                # New path found, append to list of paths
                paths.append((ny, nx))
        # print(f"For source {(y, x)}, number of paths to summit: {ends}")
        return ends, unique

    total_trails = 0
    total_unique = 0
    for x, y in trailheads:
        t, u = find_ends(x, y)
        total_trails += t
        total_unique += u

    print(f"Part1: {total_trails}")
    print(f"Part2: {total_unique}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
