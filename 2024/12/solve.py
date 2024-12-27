import sys
from collections import deque
# from rich import print

dir4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def area(region):
    return len(region)


def perimeter(region):
    p = 0
    for x, y in region:
        p += 4
        for dx, dy in dir4:
            if (x + dx, y + dy) in region:
                p -= 1
    return p

def sides(region):
    edges = {}
    for x, y in region:
        for dx, dy in dir4:
            nx, ny = x + dx, y + dy
            if (nx, ny) in region: continue
            ey = (y + ny) / 2
            ex = (x + nx) / 2
            edges[(ex, ey)] = (ex - x, ey -y)
    
    seen = set()
    side_count = 0
    for edge, direction in edges.items():
        if edge in seen:
            continue

        seen.add(edge)
        side_count += 1

        ex, ey = edge
        if ex % 1 == 0:
            for dy in [-1, 1]:
                cy = ey + dy
                while edges.get((ex, cy)) == direction:
                    seen.add((ex, cy))
                    cy += dy
        else:
            for dx in [-1, 1]:
                cx = ex + dx
                while edges.get((cx, ey)) == direction:
                    seen.add((cx, ey))
                    cx += dx

    return side_count


def solve(file):
    with open(file, "r") as f:
        content = f.read()
    content = content.splitlines()

    # Build grid layout
    grid = [[c for c in row] for row in content]
    gh = len(grid)      # grid height
    gw = len(grid[0])   # grid width

    regions = []
    seen = set()

    for y in range(gh):
        for x in range(gw):
            check_loc = (x, y)
            if check_loc in seen: continue

            seen.add(check_loc)        # mark as seen
            region = {check_loc}       # new region
            queue = deque([check_loc]) # start BFS
            plant = grid[y][x]      # current plant type

            # Breadth First Search
            while queue:
                cx, cy = queue.popleft()
                for nx, ny in [(cx + dx, cy + dy) for dx, dy in dir4]:
                    # Check if next position is out of bounds or not the same plant
                    if nx < 0 or nx >= gw or ny < 0 or ny >= gh or grid[ny][nx] != plant:
                        continue

                    next_pos = (nx, ny)
                    if next_pos in region:
                        continue

                    region.add(next_pos)
                    queue.append(next_pos)
            
            seen |= region
            regions.append(region)

    total_price = sum(area(r) * perimeter(r) for r in regions)
    print("Part 1:", total_price)

    total_price2 = sum(len(r) * sides(r) for r in regions)
    print("Part 2:", total_price2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
