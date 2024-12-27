import re
with open("input.txt") as file:
    lines = file.read().strip().splitlines()

olen = sum(len(l) for l in lines)
print(f"Original line len: {olen}")

p1 = olen - sum(len(bytes(l[1:-1], 'ascii').decode('unicode_escape')) for l in lines)
p2 = sum(len('"' + re.sub(r'([\"\'\\])', r'\\\1', l) + '"') for l in lines) - olen

print(f"Part1: {p1}")
print(f"Part2: {p2}")
