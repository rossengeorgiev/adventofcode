from aoc import aoc_web_session
web = aoc_web_session()

from itertools import cycle

freq_changes = [int(x)
                for x in web.get('https://adventofcode.com/2018/day/1/input').text.split('\n')
                if x]

part1 = sum(freq_changes)

print("Part 1: %s" % part1)

freq = 0
seen = {0}

for x in cycle(freq_changes):
    freq += x
    if freq in seen:
        print("Part 2: %s" % freq)
        break
    seen.add(freq)
