from __future__ import print_function
from itertools import product, combinations
from math import ceil
import operator

shop = {
    "weapons": {
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0),
    },
    "armors": {
        (0, 0, 0),
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5),
    },
    "rings": {
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    }
}

boss_hp = float(raw_input('Boss HP: '))
boss_dmg = int(raw_input('Boss Damage: '))
boss_armor = int(raw_input('Boss Armor: '))

part1 = []
part2 = []

for gear in product(shop['weapons'], shop['armors']):
    for rings in [((0, 0, 0),)] + list(combinations(shop['rings'], 2)):
        player_hp = 100.0

        cost, damage, armor = reduce(lambda a, b: map(operator.add, a, b), gear + rings)

        player_turns = ceil(boss_hp / max(1, damage - boss_armor))
        boss_turns = ceil(player_hp / max(1, boss_dmg - armor))

        if player_turns <= boss_turns:
            # player won
            part1.append(cost)
        else:
            # boss won
            part2.append(cost)

print("Answer (part1): %s" % min(part1))
print("Answer (part2): %s" % max(part2))
