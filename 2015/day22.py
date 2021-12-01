from __future__ import print_function

def simulate_turn(hp, mana, bhp, bdmg, shield=0, poison=0, recharge=0, depth=0, part2=False):
    hp = min(hp, 50)

    # apply effect at start of turn
    if shield:
        shield = max(0, shield - 1)
    if poison:
        bhp -= 3
        poison = max(0, poison - 1)
    if recharge:
        mana += 101
        recharge = max(0, recharge - 1)

    armor = 7 if shield else 0

    # player dead ? (or max depth)
    if depth <= 0 or hp <= 0:
        return 10e8

    # boss dead ?
    if bhp <= 0:
        return 0

    # boss turn
    if depth % 2 == 1:
        hp -= max(1, bdmg - armor)
        return simulate_turn(hp, mana, bhp, bdmg, shield, poison, recharge, depth - 1, part2)
    # player turn
    else:
        if part2:
            hp -= 1

        mimana = 10e8

        if mana >= 53:
            mimana = min(mimana, 53 +  simulate_turn(hp, mana-53, bhp - 4, bdmg, shield, poison, recharge, depth - 1, part2))
        if mana >= 73:
            mimana = min(mimana, 73 +  simulate_turn(hp+2, mana-73, bhp-2, bdmg, shield, poison, recharge, depth - 1, part2))
        if mana >= 113 and not shield:
            mimana = min(mimana, 113 + simulate_turn(hp, mana-113, bhp, bdmg, 6, poison, recharge, depth - 1, part2))
        if mana >= 173 and not poison:
            mimana = min(mimana, 173 + simulate_turn(hp, mana-173, bhp, bdmg, shield, 6, recharge, depth - 1, part2))
        if mana >= 229 and not recharge:
            mimana = min(mimana, 229 + simulate_turn(hp, mana-229, bhp, bdmg, shield, poison, 5, depth - 1, part2))

        return mimana


bhp = int(raw_input("Boss HP: "))
bdmg = int(raw_input("Boss Damage: "))

print("Answer (part1): %s" % simulate_turn(50, 500, bhp, bdmg, depth=30))
print("Answer (part2): %s" % simulate_turn(50, 500, bhp, bdmg, depth=30, part2=True))
