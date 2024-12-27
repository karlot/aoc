from itertools import combinations

#// Shop items
weapons =  [
    ("Dagger",       8, 4, 0),
    ("Shortsword",  10, 5, 0),
    ("Warhammer",   25, 6, 0),
    ("Longsword",   40, 7, 0),
    ("Greataxe",    74, 8, 0),
]
armors = [
    ("None",        0,  0, 0),  # Because armor is optional
    ("Leather",     13, 0, 1),
    ("Chainmail",   31, 0, 2),
    ("Splintmail",  53, 0, 3),
    ("Bandedmail",  75, 0, 4),
    ("Platemail",  102, 0, 5),
]
rings = [
    ("Damage +1",   25, 1, 0),
    ("Damage +2",   50, 2, 0),
    ("Damage +3",  100, 3, 0),
    ("Defense +1",  20, 0, 1),
    ("Defense +2",  40, 0, 2),
    ("Defense +3", 80, 0, 3),
]

#// You can buy 0-2 rings (at most one for each hand). You must use any items you buy.
#// The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.
all_ring_combos = [('None', 0, 0, 0)]   # Starting with "no ring" as option
for ring_comb in list(combinations(rings, 1)) + list(combinations(rings, 2)):
    tot_ring_stats = ['',0,0,0]
    for ring in ring_comb:
        tot_ring_stats[0] += ring[0]
        tot_ring_stats[1] += ring[1]
        tot_ring_stats[2] += ring[2]
        tot_ring_stats[3] += ring[3]
    all_ring_combos.append(tuple(tot_ring_stats))

#// Read boss stats from file
with open("input.txt") as file:
    lines = file.read().strip().splitlines()
    for line in lines:
        prop, stat = line.split(": ")
        if "Hit Points" in prop:  hp = int(stat)
        if "Damage" in prop:      dmg = int(stat)
        if "Armor" in prop:       armor = int(stat)
    boss_stat = (hp, dmg, armor)

#// Initial player stats
player_stat = (100, 0, 0)


def attack(attacker, defender):
    defender[0] -= attacker[1] - defender[2] if attacker[1] - defender[2] > 0 else 1

def fight(player_stat, boss_stat):
    while True:
        attack(player_stat, boss_stat)
        if boss_stat[0] <= 0: return True
        attack(boss_stat, player_stat)
        if player_stat[0] <= 0: return False
        

def run_game():
    win_costs = []
    lose_costs = []
    for weapon in weapons:
        for armor in armors:
            for ring_combo in all_ring_combos:
                new_player_stat = list(player_stat)

                items_cost   = weapon[1] + armor[1] + ring_combo[1]
                items_damage = weapon[2] + armor[2] + ring_combo[2]
                items_armor  = weapon[3] + armor[3] + ring_combo[3]

                new_player_stat[1] += items_damage
                new_player_stat[2] += items_armor

                new_boss_stat = list(boss_stat)
                if fight(new_player_stat, new_boss_stat):
                    win_costs.append(items_cost)
                else:
                    lose_costs.append(items_cost)

    return min(win_costs), max(lose_costs)


lowest_win_cost, highest_lose_cost = run_game()

print(f"Part1: {lowest_win_cost}")
print(f"Part2: {highest_lose_cost}")
