from __future__ import print_function

def mutate(a, b):
    i = 0
    while mol[i:].find(a) >= 0:
        i += mol[i:].find(a)
        yield mol[:i] + b + mol[i+len(a):]
        i += len(a)

print("Input: ")

reps = map(lambda x: x.split(' => '), iter(raw_input, ''))
mol = raw_input()

part1 = len(reduce(lambda a, b: a|b, map(lambda x: set(mutate(*x)), reps)))

target = mol
part2 = 0

while target != 'e':
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

print("Answer (part1): %s" % part1)
print("Answer (part2): %s" % part2)
