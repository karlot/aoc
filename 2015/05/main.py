with open("input.txt") as file:
    content = file.read().strip()
    lines = content.splitlines()

def solve_p1(lines):
    nice = 0
    for line in lines:
        vowels = 0
        has_double = False
        contains_bad = False
        for i, c in enumerate(line):
            # Count vowels
            if c in "aeiou":
                vowels += 1
            
            # Check double
            if not has_double and not i == 0 and c == line[i - 1]:
                has_double = True
            
        # Check if contains bad letters
        for bad in ["ab", "cd", "pq", "xy"]:
            if bad in line:
                contains_bad = True
        
        if vowels >= 3 and has_double and not contains_bad:
            nice += 1
    return nice

def solve_p2(lines):
    nice = 0
    for line in lines:
        has_pairs = False
        has_between = False
        for i, c in enumerate(line):
            # Check pairs
            if not has_pairs and i > 0:
                pair = line[i - 1] + c
                if pair in line[i+1:]:
                    has_pairs = True

            # Check if it has a between-er
            if not has_between and i >= 2 and c == line[i - 2]:
                has_between = True
            
        if has_between and has_pairs:
            nice += 1
    return nice

print(f"Part1: {solve_p1(lines)}")
print(f"Part2: {solve_p2(lines)}")