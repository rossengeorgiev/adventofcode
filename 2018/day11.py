from aoc import aoc_web_session
web = aoc_web_session()

from collections import deque

serial = int(web.get('https://adventofcode.com/2018/day/11/input').text)
#serial = 18

size = 300
grid = {}

def power(x, y):
    rack = x + 1 + 10
    power = (rack * (y + 1)) + serial
    power *= rack
    return ((power // 100) % 10) - 5


grid = dict(((x, y), power(x, y)) for x in range(size) for y in range(size))

def most_powerful_square(sq_size=1):
    max_power = 0
    loc = None

    for x in range(size - (sq_size - 1)):
        for y in range(size - (sq_size - 1)):
            power = sum(grid[(x1, y1)]
                        for x1 in range(x, x + sq_size)
                        for y1 in range(y, y + sq_size)
                        )

            if power > max_power:
                max_power = power
                loc = x + 1, y + 1

    return loc, power


part1, _ = most_powerful_square(sq_size=3)
print("Part 1: %s,%s" % part1)

sq_size, ((x, y), power) = max(((sq_size, most_powerful_square(sq_size))
                                for sq_size in range(10, 20)
                                ),
                               key=lambda p: p[1][1]
                               )

print("Part 2: %s,%s,%s" % (x, y, sq_size))
