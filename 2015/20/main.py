import math
with open("input.txt") as file:
    lines = file.read().strip().splitlines()

target_presents = int(lines[0])

#// Initial sum_of_divisors implementation... very readable but slow in large iterations:
# def sum_of_divisors(n):
#     return sum(x for x in range(1, n+1) if n % x == 0)

#// First workable approach ... but very slow as divisors generation is slowing down in each
#// increment of house number. This optimizations uses square root calculations
# def sum_of_divisors(n):
#     result = 1
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             count = 0
#             while n % i == 0:
#                 count += 1
#                 n //= i
#             result *= (i**(count + 1) - 1) // (i - 1)
#     if n > 1:
#         result *= (n + 1)
#     return result

# def find_house():
#     house = 1
#     while True:
#         presents = sum_of_divisors(house) * 10
#         if presents >= target_presents:
#             return house
#         house += 1

# print(f"Part1: {find_house()}")

#// Just generating assumed amount of houses, and have each elf add presents to them
def find_house(target_presents, num_presents=10, quota=None, upper_limit=None):
    if not upper_limit:
        upper_limit = target_presents // num_presents

    houses = [house_num * num_presents for house_num in range(upper_limit + 1)]
    houses_above_target = set([])

    for elf in range(2, len(houses)):
        bound = min(upper_limit, elf * quota) if quota else upper_limit
        for house_num in range(elf * 2, bound + 1, elf):
            houses[house_num] += num_presents * elf

            # If presents are crossing target add this house to 
            if houses[house_num] >= target_presents:
                houses_above_target.add(house_num)
    
    # Return smallest house value
    return min(houses_above_target)


# Adding upper limit speeds up quite a lot, and saves memory, in this reverse-approach
# as we are generating in-memory list of all possible houses
print(f"Part1: {find_house(target_presents, num_presents=10, upper_limit=1_000_000)}")
print(f"Part2: {find_house(target_presents, num_presents=11, quota=50, upper_limit=1_000_000)}")
