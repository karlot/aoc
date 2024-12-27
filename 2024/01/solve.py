import sys

def solve(file):
    left = []
    right = []
    with open(file, "r") as f:
        for line in f:
            l, r = line.strip().split()
            if l and r:
                left.append(int(l))
                right.append(int(r))

    l_sorted = sorted(left)
    r_sorted = sorted(right)
    p1_dist = 0
    for i in range(len(l_sorted)):
        p1_dist += abs(l_sorted[i] - r_sorted[i])

    p2_sim_score = 0
    for a in left:
        num_seen = 0
        for b in right:
            if a == b: num_seen += 1
        p2_sim_score += a * num_seen
        
    print(f"Part1: {p1_dist}")
    print(f"Part2: {p2_sim_score}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input")
        exit(1)
    solve(sys.argv[1])
