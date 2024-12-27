with open("input.txt") as file:
    lines = file.read().strip().splitlines()

def look_at_nums(nums):
    i = 0
    c = nums[i]
    num = 1
    new_nums = ""
    while i < len(nums) - 1:
        i += 1
        if nums[i] == c:
            num += 1
        else:
            new_nums += str(num) + c
            c = nums[i]
            num = 1
    new_nums += str(num) + c
    return new_nums

nums = lines[0]
for i in range(50):
    if i == 40:
        p1 = len(nums)
    nums = look_at_nums(nums)
p2 = len(nums)

print(f"Part1: {p1}")
print(f"Part2: {p2}")
