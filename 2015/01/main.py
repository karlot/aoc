with open("input.txt") as file:
    for line in file.readlines():
        floor = 0
        bii = 0
        for i, c in enumerate(line):
            if c == "(": floor += 1
            if c == ")": floor -= 1
            if floor < 0:
                if not bii:
                    bii = i + 1
        print(f"Part1: {floor}")
        print(f"Part2: {bii}")