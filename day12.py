from __future__ import print_function
import re
import json

print("Input (empty line to finish): ")

data = ''.join(list(iter(raw_input, '')))

answer = sum(map(int, re.findall(r'-?\d+', data)))

print("Answer (part1): %s" % answer)

data = json.loads(data)

def redsum(part):
    if isinstance(part, int):
        return part
    if isinstance(part, (dict, list)):
        if isinstance(part, dict):
            part = part.values()
            if 'red' in part:
                return 0
        return sum(map(redsum, part))
    return 0

print("Answer (part2): %s" % redsum(data))
