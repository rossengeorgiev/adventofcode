from __future__ import print_function
from re import findall

def listen_to_santa(line):
    if not line: return
    cmd, state, x, y, x2, y2 = findall("(turn (on|off)|toggle) (\d+),(\d+) \w+ (\d+),(\d+)", line)[0]

    for i in range(int(x), int(x2)+1):
        for j in range(int(y), int(y2)+1):
            pos = i*1000 + j
            if cmd == 'toggle':
                lights[pos] = 1 if lights[pos] == 0 else 0
                lights2[pos] += 2
            else:
                lights[pos] = 1 if state == 'on' else 0
                lights2[pos] += 1 if state == 'on' else -1
                lights2[pos] = max(0, lights2[pos])

lights = [0] * 1000000
lights2 = [0] * 1000000

print("Input (empty line to finish): ")

map(listen_to_santa, iter(raw_input, ''))

print("Answer (part1): %d" % sum(lights))
print("Answer (part2): %d" % sum(lights2))
