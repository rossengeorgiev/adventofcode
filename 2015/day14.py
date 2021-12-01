from __future__ import print_function
import re
from collections import Counter

def distance(racer, time):
    speed, flytime, rest = map(float, racer[1:])
    a, b = divmod(time, flytime + rest)
    return int((min(b, flytime) + (a * flytime)) * speed)

print("Input (empty line to finish): ")

raw = '\n'.join(list(iter(raw_input, '')))
racers = re.findall(r'(\w+) can fly (\d+) km/s for (\d+) .* (\d+) seconds.', raw)

print("Answer (part1): %s" % max([distance(racer, 2503) for racer in racers]))

scoreboard = []

for time in range(2503):
    ds = [distance(racer, time+1) for racer in racers]
    scoreboard += [name for i,(name,_,_,_) in enumerate(racers) if ds[i] == max(ds)]

print("Answer (part2): %s" % str(Counter(scoreboard).most_common()[0]))
