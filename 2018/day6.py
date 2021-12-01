from aoc import aoc_web_session
web = aoc_web_session()

from itertools import product
from collections import Counter

cords = [tuple(map(int, cord.split(',')))
         for cord in web.get('https://adventofcode.com/2018/day/6/input').text.split('\n')
         if cord]

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

x1 = min(map(lambda xy: xy[0], cords))
x2 = max(map(lambda xy: xy[0], cords))
y1 = min(map(lambda xy: xy[1], cords))
y2 = max(map(lambda xy: xy[1], cords))

grid = {}
part2 = 0

for xy in product(range(x1, x2+1), range(y1, y2+1)):
    distances = [distance(xy, p) for p in cords]
    min_dist = min(distances)
    grid[xy] = None if distances.count(min_dist) > 1 else distances.index(min_dist)
    if sum(distances) < 10000:
        part2 += 1

infinite_zones = set([None])
infinite_zones.update(map(grid.get, product(range(x1, x2+1), [y1, y2])))
infinite_zones.update(map(grid.get, product([x1, x2], range(y1, y2+1))))

part1 = [size
         for zone, size in Counter(grid.values()).most_common()
         if zone not in infinite_zones
         ][0]

print("Part 1: %s" % part1)
print("Part 2: %s" % part2)
