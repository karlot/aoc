import re
from itertools import permutations
with open("input.txt") as file:
    lines = file.read().strip().splitlines()

happiness = {}      # Key: (p1,p2) tuple -> value: p1 happiness towards sitting next to p2
names = set()       # All unique person names
for line in lines:
    if m := re.match(r"^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.$", line):
        p1, dif, points, p2 = m.groups()
        names.add(p1)
        names.add(p2)
        if dif == "gain":
            happiness[(p1,p2)] = int(points)
        else:
            happiness[(p1,p2)] = -int(points)

def find_optimal_happiness(names):
    total_names = len(names)
    print(f"{total_names=}")
    optimum_happiness = 0
    for perm in permutations(names):
        ph = 0
        for i in range(total_names):
            p1 = perm[i]
            if i == 0:                  # Beginning of circle
                p_prev = perm[-1]
                p_next = perm[1]
            elif i == total_names - 1:  # end of circle
                p_prev = perm[i-1]
                p_next = perm[0]
            else:                       # middle of circle
                p_prev = perm[i-1]
                p_next = perm[i+1]
            ph += happiness[(p1,p_prev)]
            ph += happiness[(p1,p_next)]
        optimum_happiness = max(optimum_happiness, ph) if optimum_happiness > 0 else ph
    return optimum_happiness

print(f"Part1: {find_optimal_happiness(names)}")

# Add "me" to the table... with indifferent score to anyone and anyone to "me"
for n in names:
    happiness[("me",n)] = 0
    happiness[(n,"me")] = 0
names.add("me")

print(f"Part2: {find_optimal_happiness(names)}")
