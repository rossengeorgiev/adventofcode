from __future__ import print_function
import re

def part2_regex(item):
    name, n = item

    if name in ('cats', 'trees'):
        return "%s: ([%s-9]|\d{2})" % (name, n+1)
    elif name in ('pomeranians', 'goldfish'):
        return "%s: ([0-%s])" % (name, n-1)
    else:
        return "%s: [%s]" % item

tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

print("Input (empty line to finish): ")

data = '\n'.join(iter(raw_input, ''))

exp_base = "((Sue \d+):( (%s),?)+)\n"
exp1 = exp_base % '|'.join(map(lambda x: "%s: [%s]" % x, tape.items()))
exp2 = exp_base % '|'.join(map(part2_regex, tape.items()))

print("Answer (part1):", re.search(exp1, data).group(1))
print("Answer (part2):", re.search(exp2, data).group(1))
