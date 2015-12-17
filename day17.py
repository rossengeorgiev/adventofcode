
from __future__ import print_function
import re

def combinations(containers, liters):
    for i, container in enumerate(containers):
        if container > liters:
            continue

        left = liters - container
        if left:
            for y in combinations(containers[i+1:], left):
                yield [container] + y
        else:
            yield [container]


print("Input (empty line to finish): ")

containers = map(int, iter(raw_input, ''))
diff_ways = list(combinations(containers, 150))

print("Answer (part1): %s" % len(diff_ways))

diff_ways = map(len, diff_ways)

print("Answer (part2): %s" % diff_ways.count(min(diff_ways)))
