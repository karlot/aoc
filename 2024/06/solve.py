import sys

next_d = {
    "up": (0, -1),
    "right": (1, 0),
    "down": (0, 1),
    "left": (-1, 0),
}
next_rot = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up",
}

def parse_grid(lines):
    grid = []
    guard = None
    direction = None
    for y, l in enumerate(lines):
        row = []
        for x, c in enumerate(l):
            row.append(c)
            if c not in "^v<>": continue
            guard = (x, y)
            if   c == "^": direction = "up"
            elif c == "v": direction = "down"
            elif c == "<": direction = "left"
            elif c == ">": direction = "right"
        grid.append(row)
    return grid, guard, direction

def run_sim(grid, guard, direction):
    visited = set()
    visited.add(guard)

    visited_dir = set()
    visited_dir.add((*guard, direction))

    max_y = len(grid)
    max_x = len(grid[0])

    while(True):
        nx = guard[0] + next_d[direction][0]
        ny = guard[1] + next_d[direction][1]

        if ny < 0 or nx < 0 or ny >= max_y or nx >= max_x:
            break
        elif grid[ny][nx] == "#":
            direction = next_rot[direction]
        else:
            guard = (nx, ny)
            guard_dir = (nx, ny, direction)
            if guard not in visited:
                visited.add(guard)

            if guard_dir in visited_dir:
                return True, 0
            else:
                visited_dir.add(guard_dir)
    
    return False, len(visited)


def solve(file):
    with open(file, "r") as f:
        content = f.read()
    content = content.strip()
    lines = content.splitlines()

    grid, guard, direction = parse_grid(lines)

    # Part1
    _, p1 = run_sim(grid, guard, direction)
    print(f"Part1: {p1}")

    # Part2
    loop_opts = 0
    total_options = len(grid) * len(grid[0])
    testing = 0
    for y, r in enumerate(grid):
        testing += len(r)
        sys.stdout.write(f"\rTesting {testing} out of {total_options} options")
        sys.stdout.flush()
        for x, c in enumerate(r):
            if grid[y][x] in "#^>v<":
                continue
            grid[y][x] = "#"
            looped, _ = run_sim(grid, guard, direction)
            if looped:
                loop_opts += 1
            grid[y][x] = "."
    print(f"\nPart2: {loop_opts}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
