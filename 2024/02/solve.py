import sys

def check_nums(nums):
    s_nums = sorted(nums)
    rs_nums = list(reversed(s_nums))
    if nums == s_nums or nums == rs_nums:
        a = None
        for n in nums:
            if not a:
                a = n
                continue
            if n == a: return False
            if abs(n - a) > 3: return False
            a = n
        return True
    return False

def check_nums2(nums):
    if check_nums(nums): return True
    for i in range(len(nums)):
        new_nums = nums[:]
        del new_nums[i]
        if check_nums(new_nums): return True
    return False

def solve(file):
    with open(file, "r") as f:
        lines = f.readlines()

    safe_p1 = 0
    safe_p2 = 0
    for line in lines:
        nums = line.strip().split()
        nums = [int(n) for n in nums]
        if check_nums(nums): safe_p1 += 1
        if check_nums2(nums): safe_p2 += 1

    print(f"Part1: {safe_p1}")
    print(f"Part2: {safe_p2}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
