from aoc import aoc_web_session
web = aoc_web_session()

import re
from collections import Counter

patches = web.get('https://adventofcode.com/2018/day/3/input').text

fabric = Counter()
claims = list(map(lambda x: map(int, x),
              re.findall(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', patches)))

for claim_id, x, y, w, h in claims:
    for fx in range(x, x+w):
        for fy in range(y, y+h):
            fabric[(fx, fy)] += 1

answer = sum(map(lambda x: x > 1, fabric.values()))
print("Part 1: %s" % answer)

for claim_id, x, y, w, h in claims:
    if all((fabric[(fx, fy)] == 1 for fx in range(x, x+w) for fy in range(y, y+h))):
        print("Part 2: %s" % claim_id)
        break
