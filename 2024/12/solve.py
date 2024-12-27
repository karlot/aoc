import sys
from collections import deque

# 4 directions to move in a grid
dir4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Parses all regions in the grid, and returns them as a list of location sets
def parse_regions(grid):
    gh = len(grid)      # grid height
    gw = len(grid[0])   # grid width

    regions = []
    seen = set()

    for y in range(gh):
        for x in range(gw):
            check_loc = (x, y)
            if check_loc in seen: continue

            seen.add(check_loc)         # mark as seen
            region = {check_loc}        # new region
            queue = deque([check_loc])  # start BFS

            # Breadth First Search
            while queue:
                cx, cy = queue.popleft()
                for nx, ny in [(cx + dx, cy + dy) for dx, dy in dir4]:
                    # Check if next position is out of bounds or not the same plant type that started the region
                    if nx < 0 or nx >= gw or ny < 0 or ny >= gh or grid[ny][nx] != grid[y][x]:
                        continue

                    next_pos = (nx, ny)
                    if next_pos in region:
                        continue

                    region.add(next_pos)
                    queue.append(next_pos)

            # Append all cells from region to seen set (union)
            seen |= region
            regions.append(region)

    return regions


# Area is basically lengths of positions in the region
def area(region):
    return len(region)


# Perimeter is the sum of all 4 directions around a cell, minus the number
# of cells that are adjacent to the current cell
def perimeter(region):
    perim = 0
    for x, y in region:
        perim += 4
        for dx, dy in dir4:
            if (x + dx, y + dy) in region:
                perim -= 1
    return perim


# Function that calculates the number of edges of a region
def edges(region):
    # TODO: I dont know how to calculate this
    ...


def solve(file):
    with open(file, "r") as f:
        content = f.read()
    content = content.splitlines()

    # Build grid layout
    grid = [[c for c in row] for row in content]
    regions = parse_regions(grid)

    total_price = sum(area(r) * perimeter(r) for r in regions)
    print("Part 1:", total_price)

    # total_price2 = sum(len(r) * sides(r) for r in regions)
    # print("Part 2:", total_price2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
