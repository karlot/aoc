import sys

#### Does not work for lots of blinking!!!
# def blink(stones, times):
#     for _ in range(times):
#         new_stones = []
#         for i, num in enumerate(stones):
#             snum = str(num)
#             l = len(snum)
#             if num == 0:
#                 new_stones.append(1)
#                 continue
#             elif l % 2 == 0:
#                 fst = int(snum[:l//2])
#                 snd = int(snum[l//2:])
#                 new_stones += [fst, snd]
#             else:
#                 new_stones.append(num * 2024)
#         stones = new_stones
#     return len(new_stones)

cache = {}
def blink2(stone, times):
    if times == 0: return 1
    if (stone, times) not in cache:
        if stone == 0:
            r = blink2(1, times - 1)
        elif len(str(stone)) % 2 == 0:
            sx = str(stone)
            r = blink2(int(sx[:len(sx) // 2]), times - 1) + blink2(int(sx[len(sx) // 2:]), times - 1)
        else:
            r = blink2(stone * 2024, times - 1)
        cache[(stone, times)] = r
        return r
    else:
        return cache[(stone, times)]


def solve(file):
    with open(file, "r") as f:
        content = f.read()
    content = content.strip()
    stones = [int(i) for i in content.split()]
    
    # print(f"Part1: {blink(stones, 25)}")
    print(f"Part1: {sum(blink2(s, 25) for s in stones)}")
    print(f"Part2: {sum(blink2(s, 75) for s in stones)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
