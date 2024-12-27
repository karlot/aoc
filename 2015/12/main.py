import json
with open("input.txt") as file:
    lines = file.read().strip().splitlines()

def get_numbers(x, check_red=False):
    if isinstance(x, int): return x
    num = 0
    if isinstance(x, list):
        for n in x:
            num += n if isinstance(n, int) else get_numbers(n, check_red)
        return num
    if isinstance(x, dict):
        if check_red:
            if "red" in x.values(): return 0
        for n in x.values():
            num += n if isinstance(n, int) else get_numbers(n, check_red)
        return num
    return num

doc = json.loads(lines[0])

print(f"Part1: {get_numbers(doc, check_red=False)}")
print(f"Part2: {get_numbers(doc, check_red=True)}")
