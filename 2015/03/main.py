with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        x, y = 0, 0
        sx, sy = 0, 0
        rx, ry = 0, 0
        visited_p1 = {(0, 0)}   # SET Include starting position
        visited_p2 = {(0, 0)}   # SET Include starting position

        for i, c in enumerate(line):
            # Part 1
            if c == ">": x += 1
            if c == "<": x -= 1
            if c == "^": y += 1
            if c == "v": y -= 1
            if (x, y) not in visited_p1: visited_p1.add((x, y))
            
            # Part 2 (Santa and RoboSanta each handle one instruction)
            if not i % 2:
                # Santa's moves
                if c == ">": sx += 1
                if c == "<": sx -= 1
                if c == "^": sy += 1
                if c == "v": sy -= 1
                if (sx, sy) not in visited_p2: visited_p2.add((sx, sy))
            else:
                # RoboSanta's moves
                if c == ">": rx += 1
                if c == "<": rx -= 1
                if c == "^": ry += 1
                if c == "v": ry -= 1
                if (rx, ry) not in visited_p2: visited_p2.add((rx, ry))

        print(f"Part1: {len(visited_p1)}")
        print(f"Part2: {len(visited_p2)}")