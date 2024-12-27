with open("input.txt") as file:
    lines = file.read().strip().splitlines()

def rotate_pass(old):
    for i in range(8):
        if old[i] == 122:   # z
            old[i] = 97     # a
        else:
            old[i] += 1
            return

def check1(pas):
    for i, c in enumerate(pas[:-2]):
        if c == pas[i+1] + 1 and c == pas[i+2] + 2:
            return True
    return False

def check2(pas):
    if 105 in pas or 111 in pas or 108 in pas:
        return False
    return True 

def check3(pas):
    for i, c in enumerate(pas[:-3]):
        if c == pas[i+1]:   # found two letters identical
            chunk = pas[i+2:]
            for j, d in enumerate(chunk[:-1]):
                if d == c: # should not match equal
                    continue
                if d == chunk[j+1]:
                    return True
            break
    return False

def pas(pas):
    return "".join(reversed(list(map(chr, pas))))


def find_next_pass(old):
    new = list(reversed(list(map(ord, old))))
    while True:
        rotate_pass(new)
        if not check1(new) or not check2(new) or not check3(new):
            continue
        return pas(new)


new1_pass = find_next_pass(lines[0])
new2_pass = find_next_pass(new1_pass)

print(f"Part1: {new1_pass}")
print(f"Part2: {new2_pass}")
