from __future__ import print_function

print("Input (empty line to finish): ")

a = b = c = 0
for line in iter(raw_input, ''):
    a += len(line)
    b += len(eval(line))
    c += len(line) + line.count('\\') + line.count('"') + 2

print("Answer (part1): %d" % (a - b))
print("Answer (part2): %d" % (c - a))
