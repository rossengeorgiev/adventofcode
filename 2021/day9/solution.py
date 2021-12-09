

import operator
from functools import reduce

data = list(map(str.strip, open('input.txt').readlines()))

def explore_basin(data, x, y):
    h, w = len(data), len(data[0])
    visited = set()
    to_explore =[(x, y)]

    while to_explore:
        x, y = to_explore.pop()
        visited.add((x, y))

        if x+1<w and 9 > int(data[y][x+1]):
            if (x+1, y) not in visited:
                to_explore.append((x+1, y))
        if x>0 and 9 > int(data[y][x-1]):
            if (x-1, y) not in visited:
                to_explore.append((x-1, y))
        if y+1<h and 9 > int(data[y+1][x]):
            if (x, y+1) not in visited:
                to_explore.append((x, y+1))
        if y>0 and 9 > int(data[y-1][x]):
            if (x, y-1) not in visited:
                to_explore.append((x, y-1))

    return len(visited)

def find_low_points(data):
    h, w = len(data), len(data[0])

    low_points = []
    basins = []

    for y in range(h):
        for x in range(w):
            n = int(data[y][x])

            if x+1<w and n >= int(data[y][x+1]):
                continue
            if x>0 and n >= int(data[y][x-1]):
                continue
            if y+1<h and n >= int(data[y+1][x]):
                continue
            if y>0 and n >= int(data[y-1][x]):
                continue

            low_points.append(n)
            basins.append(explore_basin(data, x, y))

    return sum(low_points) + len(low_points), reduce(operator.mul, sorted(basins)[-3:])


part1, part2 = find_low_points(data)

print("Part1:", part1)
print("Part2:", part2)

