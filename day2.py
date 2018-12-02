from aoc import aoc_web_session
web = aoc_web_session()

from collections import Counter
from itertools import combinations
from difflib import SequenceMatcher

ids = [x for x in web.get('https://adventofcode.com/2018/day/2/input').text.split('\n')]

twos, threes = 0, 0

for box_id in ids:
    counts = set(Counter(box_id).values())
    if 3 in counts:
        threes += 1
    if 2 in counts:
        twos += 1

print("Part 1: %s" % (twos * threes))

for a, b in combinations(ids, 2):
    blocks = list(SequenceMatcher(a=a, b=b).get_matching_blocks())
    if len(blocks) == 3:
        first, second, _ = blocks
        if len(a) - first.size - second.size == 1:
            answer = a[first.a:first.a + first.size] + a[second.a:second.a + second.size]
            print("Part 2: %s" % answer)
            break
