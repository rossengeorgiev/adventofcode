from aoc import aoc_web_session
web = aoc_web_session()

import re
from itertools import count

data = web.get('https://adventofcode.com/2018/day/10/input').text
stars = [tuple(map(int, star))
         for star in re.findall(r'position=<([0-9\- ]+),([0-9\- ]+)> velocity=<([0-9\- ]+),([0-9\- ]+)>', data)
         ]

_yv = [(star[1], star[3]) for star in stars]

for t in count(0):
    yv = [y + (t * v) for y, v in _yv]
    if abs(max(yv) - min(yv)) == 9:
        break

stars = set((x + (vx * t), y + (vy * t)) for x, y, vx, vy in stars)
x1 = min(map(lambda star: star[0], stars))
x2 = max(map(lambda star: star[0], stars))
y1 = min(map(lambda star: star[1], stars))
y2 = max(map(lambda star: star[1], stars))

print("Part 1:")

for y in range(y1, y2+1):
    for x in range(x1, x2+1):
        print("#" if (x, y) in stars else " ", end="")
    print("")

print("Part 2: %s" % t)
