
import re
from collections import Counter


def load_data(f):
    template = f.readline().strip()
    f.readline()

    rules = {}
    for line in f:
        pair, _, insert = line.strip().split(' ')
        #rules[pair] = pair[0] + insert + pair[1]
        rules[pair] = insert

    return template, rules


def polymerize_old(poly, rules, steps=10):
    print("tempalte:", poly)

    for _ in range(steps):
        new_poly = []
        last = len(poly)-2
        for i in range(len(poly)-1):
            pair = poly[i:i+2]
            new_poly.append(rules.get(pair, pair)[:2 if i < last else 3])
        poly = ''.join(new_poly)

    c = Counter(poly).most_common()
    return poly, c[0][1] - c[-1][1]

def polymerize(poly, rules, steps=10):
    pairs = Counter()
    for i in range(len(poly)-1):
        pairs[poly[i] + poly[i+1]] += 1

    total = Counter(poly)

    for _ in range(steps):
        for (a,b), c in list(pairs.items()):
            ins = rules[a+b]
            pairs[a+b] -= c
            pairs[a+ins] += c
            pairs[ins+b] += c
            total[ins] += c

    c = total.most_common()
    return c[0][1] - c[-1][1]


template, rules = load_data(open('input.txt'))
part1 = polymerize(template, rules, steps=10)
part2 = polymerize(template, rules, steps=40)

print("Part1:", part1)
print("Part2:", part2)
