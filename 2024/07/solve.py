import sys


def check_valid(t, n, part2):
    if len(n) == 1:
        return t == n[0]
    if check_valid(t, [n[0] + n[1]] + n[2:], part2): return True
    if check_valid(t, [n[0] * n[1]] + n[2:], part2): return True
    if part2 and check_valid(t, [int(f"{n[0]}{n[1]}")] + n[2:], part2): return True
    return False

def solve(file):
    with open(file, "r") as f:
        content = f.read()
    content = content.strip()
    lines = content.splitlines()

    p1 = 0
    p2 = 0
    for l in lines:
        test_val, nums = l.split(":")
        test_val = int(test_val)
        nums = [int(i) for i in nums.split()]
        if check_valid(test_val, nums, False): p1 += test_val
        if check_valid(test_val, nums, True): p2 += test_val
        
    print(f"Part1: {p1}")
    print(f"Part2: {p2}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
