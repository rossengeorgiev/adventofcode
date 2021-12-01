from __future__ import print_function
from math import sqrt
from collections import defaultdict

try:
    xrange(0)
except NameError:
    xrange = range

def factor(x):
    y2 = sqrt(x)
    y2i = int(y2)
    if y2 == y2i:
        yield y2i
    for n in xrange(1, y2i):
        if x % n == 0:
            yield n
            yield x / n

target = int(raw_input("Input: "))

presents = house_n = 0

while presents <= target:
    house_n += 1
    presents = sum(factor(house_n)) * 10

print("Answer (part1): %s" % house_n)

visited = defaultdict(int)
presents = house_n = 0

while presents <= target:
    house_n += 1
    presents = 0
    for n in factor(house_n):
        visited[n] = count = visited[n] + 1
        if count <= 50:
            presents += n
    presents *= 11

print("Answer (part2): %s" % house_n)
