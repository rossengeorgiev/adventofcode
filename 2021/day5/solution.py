
import re
from collections import defaultdict

lines = [list(map(int, re.split('[^0-9]+', line.strip()))) for line in open('input.txt')]

line_map1 = defaultdict(int)
line_map2 = defaultdict(int)

for x1, y1, x2, y2 in lines:
    xdir = 1 if x2 > x1 else -1
    ydir = 1 if y2 > y1 else -1

    x, y = x1, y1

    while True:
        if x1 == x2 or y1 == y2:
            line_map1[(x,y)] += 1
        line_map2[(x,y)] += 1

        if x == x2 and y == y2:
            break

        x += xdir if x != x2 else 0
        y += ydir if y != y2 else 0


part1 = len(list(filter(lambda v: v >= 2, line_map1.values())))
part2 = len(list(filter(lambda v: v >= 2, line_map2.values())))

print("Part1:", part1)
print("Part2:", part2)

