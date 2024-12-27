with open("input.txt") as file:
    total_area = 0
    rib_len = 0
    for line in file.readlines():
        l, w ,h = tuple(map(int,line.split("x")))
        # Part1 calc
        area = 2*l*w + 2*w*h + 2*h*l
        total_area += area + min(l*w, w*h, h*l)

        # Part2 calc
        a, b = sorted([l, w, h])[0:2]
        rib_len += (2*a) + (2*b) + (l*w*h)

    print(f"Part1: {total_area}")
    print(f"Part2: {rib_len}")