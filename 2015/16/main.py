import re

with open("input.txt") as file:
    lines = file.read().strip().splitlines()

MFCSAM_info = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

aunts = {}
for line in lines:
    if m := re.match(r"^Sue (\d+): (.*)$", line):
        sue_num, rest = m.groups()
        aunts[sue_num] = {}
        for c in [comp for comp in rest.split(", ")]:
            prop, num = c.split(": ")
            aunts[sue_num][prop] = int(num)


def find_sue(part=1):
    for sue, sue_props in aunts.items():
        found = True
        for prop, num in sue_props.items():
            if part == 2:
                if prop == "cats" or prop == "trees":
                    if MFCSAM_info[prop] > num:
                        found = False
                        break
                    continue
                if prop == "pomeranians" or prop == "goldfish":
                    if MFCSAM_info[prop] <= num:
                        found = False
                        break
                    continue
            if MFCSAM_info[prop] != num:
                found = False
                break
        if found:
            return sue


print(f"Part1: {find_sue(part=1)}")
print(f"Part2: {find_sue(part=2)}")
