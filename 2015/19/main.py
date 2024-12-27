from random import shuffle

with open("input.txt") as file:
    lines = file.read().strip().splitlines()

replacements = []
for line in lines:
    if line:
        if (len(parts := line.split(" => ")) > 1):
            replacements.append((parts[0], parts[1]))
        else:
            molecule = parts[0]

def calibrate(m):
    dm = set()
    for src, dst in replacements:
        sl = len(src)
        for i in range(len(m)):
            if m[i:i+sl] == src:
                if i == 0:
                    dm.add(f"{dst}{m[i + sl:]}")
                else:
                    dm.add(f"{m[:i]}{dst}{m[i + sl:]}")
    return len(dm)


def steps_to_build(m):
    count = shuffles = 0
    mol = m
    # Repeat until we get to single letter (e), reverse since its much better probability to get it than not
    while len(mol) > 1:
        start = mol
        for frm, to in replacements:
            while to in mol:
                count += mol.count(to)      # increase count with all replacement we will do
                mol = mol.replace(to, frm)  # replace all what we can
        
        # Restart (in my sample not needed?)
        if start == mol:
            shuffle(replacements)
            mol = m
            count = 0
            shuffles += 1

    # print(f"{count} steps after randomizing {shuffles} times")
    return count


print(f"Part1: {calibrate(molecule)}")
print(f"Part2: {steps_to_build(molecule)}")
