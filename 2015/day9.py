from __future__ import print_function
from collections import defaultdict
from re import findall
from itertools import permutations

print("Input (empty line to finish): ")

edges = defaultdict(dict)

for line in iter(raw_input, ''):
    a, b, dist = findall("(\w+) to (\w+) = (\d+)", line)[0]
    edges[a][b] = int(dist)
    edges[b][a] = int(dist)

shortest = None
longest = None

for path in permutations(edges.keys()):
    dist = sum([edges[a][b] for a, b in zip(path, path[1:])])

    if not shortest or dist < shortest:
        shortest = dist
    if not longest or dist > longest:
        longest = dist

print("Answer (part1): %d" % shortest)
print("Answer (part2): %d" % longest)
