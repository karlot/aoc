# My goal here was not readability, but more exploring functional and minimal style
with open("input.txt") as file:
    lines = file.read().strip().splitlines()

# Part1 checkers
min3vowel = lambda l: sum(map(l.count, "aeiou")) >= 3
doubles   = lambda l: len([c for i, c in enumerate(l) if i>0 and c==l[i-1]]) > 0
not_bads  = lambda l: not len([b for b in "ab cd pq xy".split() if b in l]) > 0

# Part2 checkers
has_pairs = lambda l: len([c for i, c in enumerate(l) if i>0 and l[i-1]+c in l[i+1:]]) > 0
betweener = lambda l: len([c for i, c in enumerate(l) if i>1 and c==l[i-2]]) > 0

print(f"Part1: {sum([1 for l in lines if min3vowel(l) and doubles(l) and not_bads(l)])}")
print(f"Part2: {sum([1 for l in lines if has_pairs(l) and betweener(l)])}")