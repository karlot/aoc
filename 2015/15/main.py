with open("input.txt") as file:
    lines = file.read().strip().splitlines()

def main():
    # ingredients = []
    # for line in lines:
    #     ing, rest = line.split(":")
    #     cap, dur, fla, tex, cal = [int(prop.split()[1]) for prop in rest.strip().split(", ")]
    #     ingredients.append((cap, dur, fla, tex, cal))
    ingredients = [[int(prop.split()[1]) for prop in line.split(":")[1].strip().split(", ")] for line in lines]

    teaspoons = 100
    p1best = 0
    p2best = 0
    # Here this solution is hardcoded a bit since it expects exactly 4 ingredients as per input (not the most generic solution)
    options = 0
    for a in range(1, teaspoons + 1):
        for b in range(1, teaspoons + 1 - a):
            for c in range(1, teaspoons + 1 - a - b):
                for d in range(1, teaspoons + 1 - a - b - c):
                    # Only run calculations when we add up to 100 teaspoons (as I am clearly unable to generate )
                    if a + b + c + d == teaspoons:
                        options +=1
                        cap = ingredients[0][0] * a + ingredients[1][0] * b + ingredients[2][0] * c + ingredients[3][0] * d
                        dur = ingredients[0][1] * a + ingredients[1][1] * b + ingredients[2][1] * c + ingredients[3][1] * d
                        fla = ingredients[0][2] * a + ingredients[1][2] * b + ingredients[2][2] * c + ingredients[3][2] * d
                        tex = ingredients[0][3] * a + ingredients[1][3] * b + ingredients[2][3] * c + ingredients[3][3] * d
                        cal = ingredients[0][4] * a + ingredients[1][4] * b + ingredients[2][4] * c + ingredients[3][4] * d
                        if cap < 0: cap = 0
                        if dur < 0: dur = 0
                        if fla < 0: fla = 0
                        if tex < 0: tex = 0
                        cookie_score = cap * dur * fla * tex
                        p1best = max(p1best, cookie_score)

                        # for p2, we are interested only in cookies that are exactly 500 cal
                        if cal == 500:
                            p2best = max(p2best, cookie_score)

    print(f"Part1: {p1best}")
    print(f"Part2: {p2best}")


if __name__ == "__main__":
    main()