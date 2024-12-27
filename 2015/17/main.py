from itertools import combinations
from collections import defaultdict

with open("input.txt") as file:
    lines = file.read().strip().splitlines()

# TEST
# lines = ["20", "15", "10", "5", "5" ]

def find_combinations(containers, target_volume):
    all_combinations = 0
    combos = defaultdict(int)
    for r in range(len(containers)):
        for combination in combinations(containers, r + 1):
            if sum(combination) == target_volume:
                all_combinations += 1
                curr_len = len(combination)
                if not curr_len in combos:
                    combos[curr_len] = 1
                else:
                    combos[curr_len] += 1
    return all_combinations, combos[min(*combos.keys())]


containers = list(map(int, lines))
p1, p2 = find_combinations(containers, 150)

print(f"Part1: {p1}")
print(f"Part2: {p2}")
