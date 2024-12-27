import sys
import re

def check_order(update, print_order_rules):
    for i in range(len(update)):
        if i == len(update) - 1: break
        for n1, n2 in print_order_rules:
            if update[i] == n2 and update[i+1] == n1:
                return False
    return True


def solve(file):
    with open(file, "r") as f:
        content = f.read()

    content = content.strip()
    print_order_rules, print_pages_update = content.split("\n\n")

    print_order_rules = [list(map(int, r.split("|"))) for r in print_order_rules.strip().splitlines()]
    print_pages_update = [list(map(int, u.split(","))) for u in print_pages_update.strip().splitlines()]

    sum_p1 = 0
    sum_p2 = 0
    for update in print_pages_update:
        correct = check_order(update, print_order_rules)
        if correct:
            sum_p1 += update[int(len(update)/2)]
        else:
            ordered = False
            while(not ordered):
                for i in range(len(update)):
                    if i == len(update) - 1: break
                    for n1, n2 in print_order_rules:
                        if update[i] == n2 and update[i+1] == n1:
                            update[i] = n1
                            update[i+1] = n2
                ordered = check_order(update, print_order_rules)
            sum_p2 += update[int(len(update)/2)]

    print(f"Part1: {sum_p1}")
    print(f"Part2: {sum_p2}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
