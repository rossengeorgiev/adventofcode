from __future__ import print_function
from collections import defaultdict
from itertools import permutations
import re

guests = defaultdict(dict)

def total_happiness(seats):
        total, n = 0, len(seats)
        for i, name in enumerate(seats):
            total += guests[name][seats[(i-1) % n]]
            total += guests[name][seats[(i+1) % n]]
        return total

print("Input (empty line to finish): ")

data = '\n'.join(list(iter(raw_input, '')))
data = re.findall(r'(\w+) would (lose|gain) (\d+) .*? next to (\w+).', data)

for guest, sign, happiness, toward in data:
    guests[guest][toward] = int(happiness) if sign == 'gain' else -int(happiness)

print("Answer (part1): %s" % max(map(total_happiness, permutations(guests))))

for guest in list(guests.keys()):
    guests[guest]['me'] = guests['me'][guest] = 0

print("Answer (part2): %s" % max(map(total_happiness, permutations(guests))))
