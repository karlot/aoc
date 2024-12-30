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
# Calculating the number of corners/vertices of a region for each cell based on its connections
def edges(region, grid):
    region_corners = 0

    # Debug grid, shows for each cell how many corners it adds to the region
    # show_grid = [["." for _ in row] for row in grid]

    for cell in region:
        cx, cy = cell
        cell_vertices = 0

        # Check if cell is connected to another cell in the region on the sides
        connected_up         = (cx + 0, cy - 1) in region
        connected_up_right   = (cx + 1, cy - 1) in region
        connected_right      = (cx + 1, cy + 0) in region
        connected_down_right = (cx + 1, cy + 1) in region
        connected_down       = (cx + 0, cy + 1) in region
        connected_down_left  = (cx - 1, cy + 1) in region
        connected_left       = (cx - 1, cy + 0) in region
        connected_up_left    = (cx - 1, cy - 1) in region

        attached = sum(1 for d in [connected_up, connected_down, connected_left, connected_right] if d)
        if attached == 0:
            # This is a non-attached cell, may be isolated single cell region
            # print(f"non-attached cell at {cx},{cy} -> +4")
            cell_vertices = 4
        
        elif attached == 1:
            # This cell is single connected cell, so it has 2 corners, even if we dont check diagonals
            cell_vertices = 2
            # print(f"1-way connected cell at {cx},{cy} -> +2")

        elif attached == 2:
            # With 2 connected cells to current one, this can be connected in straight line shape or L shape
            # When its in line, it adds no corners, but when its L shape, we need to check if cell between corner in region
            # if it is, then we have 1 corner, otherwise 2 corners (inner one)
            if connected_up and connected_down or connected_left and connected_right:
                # print(f"2-way UD or LR connected cell at {cx},{cy} -> +0")
                cell_vertices = 0
            else:
                if connected_up and connected_right:
                    accum = 1 if connected_up_right else 2
                elif connected_up and connected_left:
                    accum = 1 if connected_up_left else 2
                elif connected_down and connected_right:
                    accum = 1 if connected_down_right else 2
                elif connected_down and connected_left:
                    accum = 1 if connected_down_left else 2
                # print(f"2-way UD or LR connected cell at {cx},{cy} -> +{accum}")
                cell_vertices = accum

        elif attached == 3:
            # With 3 connected cells, we need to check based on which side we are missing connection
            accum = 0
            if not connected_up:
                accum += 0 if connected_down_right else 1
                accum += 0 if connected_down_left else 1
            elif not connected_down:
                accum += 0 if connected_up_right else 1
                accum += 0 if connected_up_left else 1
            elif not connected_left:
                accum += 0 if connected_up_right else 1
                accum += 0 if connected_down_right else 1
            elif not connected_right:
                accum += 0 if connected_up_left else 1
                accum += 0 if connected_down_left else 1
            else:
                print("This should not happen, 3 connected cells but no missing side!", cx, cy, region)

            # print(f"3-way connected cell at {cx},{cy} -> +{accum}")
            cell_vertices = accum

        elif attached == 4:
            # This cell has 4 connected cells, but it can be inner corner on any of 4 diagonals
            accum = sum(1 for d in [connected_up_left, connected_up_right, connected_down_right, connected_down_left] if not d)
            # print(f"4-way connected cell at {cx},{cy} -> +{accum}")
            cell_vertices = accum
        else:
            print("This should not happen, more than 4 connected cells!", cx, cy, region)

        region_corners += cell_vertices
        # show_grid[cy][cx] = str(cell_vertices)

    # print("Region corners/vertices:", region)
    # for row in show_grid:
    #     print("".join(row))

    return region_corners


def solve(file):
    with open(file, "r") as f:
        content = f.read()
    content = content.splitlines()

    # Build grid layout
    grid = [[c for c in row] for row in content]
    regions = parse_regions(grid)

    total_price = sum(area(r) * perimeter(r) for r in regions)
    print("Part 1:", total_price)

    total_price2 = sum(area(r) * edges(r, grid) for r in regions)
    print("Part 2:", total_price2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
