from hashlib import md5

with open("input.txt") as file:
    content = file.read().strip()
    key = bytes(content, "ascii")

def find_number(zeroes):
    search_target = "0" * zeroes
    number = 0
    while True:
        h = md5(key)
        h.update(bytes(str(number), "ascii"))
        result = h.hexdigest()
        if result.startswith(search_target): return number
        number += 1
    

print(f"Part1: {find_number(5)}")
print(f"Part2: {find_number(6)}")