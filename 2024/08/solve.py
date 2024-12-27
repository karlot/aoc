import sys
from itertools import combinations


def find_frequencies(grid: list[list[str]]):
    freq: dict[str, list[tuple]] = {}
    for y, row in enumerate(grid):
        for x, f in enumerate(row):
            if f == ".": continue
            if f in freq:
                freq[f].append((x, y))
            else:
                freq[f] = [(x, y)]
    return freq

def find_unique_antinodes(freq, grid: list[list[str]], harmonics=False):
    grid_h = len(grid)
    grid_w = len(grid[0])
    anti_nodes = set()
    for f, val in freq.items():
        # print(f"  {f}: ", val)
        for a, b in combinations(val, 2):
            # Test both projection directions
            for p1, p2 in [(a, b), (b, a)]:
                while(True):
                    if harmonics:
                        anti_nodes.add(p1)
                        anti_nodes.add(p2)
                    px = p1[0] + p1[0] - p2[0]
                    py = p1[1] + p1[1] - p2[1]
                    if px < 0 or py < 0 or px > grid_w-1 or py > grid_h-1:  # Skip out of bounds
                        break
                    if harmonics:
                        p2 = p1
                        p1 = (px, py)
                        anti_nodes.add((px, py))
                    else:
                        anti_nodes.add((px, py))
                        break
                    # print("Projection:", (px, py), "for", (p1, p2))
    return anti_nodes

def print_grid(grid: list[list[str]], nodes=None) -> None:
    print("Grid:")
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if nodes and c == "." and (x,y) in nodes:
                c = "#"
            print(f"{c} ", end="")
        print()


def solve(file):
    with open(file, "r") as f:
        content = f.read()
    content = content.strip()
    lines = content.splitlines()
    grid = [[c for c in l] for l in lines]

    # Inspect individual frequencies on the grid, and find all
    # antenna coordinates for specific frequency
    freq = find_frequencies(grid)
    print("#Frequencies:", len(freq))

    an = find_unique_antinodes(freq, grid)
    # print_grid(grid, an)
    print(f"Part1: {len(an)}")

    an = find_unique_antinodes(freq, grid, harmonics=True)
    # print_grid(grid, an)
    print(f"Part2: {len(an)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
