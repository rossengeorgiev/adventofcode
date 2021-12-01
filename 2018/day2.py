from aoc import aoc_web_session
web = aoc_web_session()

from collections import Counter
from functools import reduce
from itertools import combinations
from difflib import SequenceMatcher

ids = [x for x in web.get('https://adventofcode.com/2018/day/2/input').text.split('\n') if x]

freqs = reduce(lambda a, b: a + b,
               (Counter(set(Counter(box_id).values())) for box_id in ids))

print("Part 1: %s" % (freqs[2] * freqs[3]))

for a, b in combinations(ids, 2):
    blocks = list(SequenceMatcher(a=a, b=b).get_matching_blocks())
    if len(blocks) == 3:
        first, second, _ = blocks
        if len(a) - first.size - second.size == 1:
            answer = a[first.a:first.a + first.size] + a[second.a:second.a + second.size]
            print("Part 2: %s" % answer)
            break
