import re

with open("input.txt") as file:
    content = file.read().strip()
    lines = content.splitlines()

lights_p1 = [[0 for _ in range(1000)] for _ in range(1000)]
lights_p2 = [[0 for _ in range(1000)] for _ in range(1000)]

for line in lines:
    if m := re.match(r"^([\w ]+) (\d+),(\d+) through (\d+),(\d+)$", line):
        cmd, x1, y1, x2, y2 = m.groups()
        for y in range(int(y1), int(y2) + 1):
            row1 = lights_p1[y] # dereferencing row add some speed up
            row2 = lights_p2[y] # dereferencing row add some speed up
            for x in range(int(x1), int(x2) + 1):
                if cmd == "turn on":
                    row1[x] = 1
                    row2[x] += 1
                if cmd == "turn off":
                    row1[x] = 0
                    row2[x] -= 1 if row2[x] > 0 else 0
                if cmd == "toggle":
                    row1[x] = 0 if row1[x] == 1 else 1
                    row2[x] += 2

print(f"Part1: {sum([sum(row) for row in lights_p1])}")
print(f"Part2: {sum([sum(row) for row in lights_p2])}")
