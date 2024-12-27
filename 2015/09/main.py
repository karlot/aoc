import sys
from itertools import permutations, pairwise

with open(sys.argv[1]) as file:
    lines = file.read().strip().splitlines()

distances = {}      # Key: (src,dst) tuple -> value: distance
towns = set()       # All unique town names
for line in lines:
    src, _, dst, _, dist = line.split()
    towns.add(src)
    towns.add(dst)
    distances[(src,dst)] = int(dist)
    distances[(dst,src)] = int(dist)

shortest = None
longest = None
# Iterate over all unique permutations of input towns
for perm in permutations(towns):
    path_len = sum(distances[(src,dst)] for src, dst in pairwise(perm))

    shortest = min(path_len, shortest) if shortest else path_len
    longest = max(path_len, longest) if longest else path_len


print(f"Part1: {shortest}")
print(f"Part2: {longest}")
