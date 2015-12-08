from __future__ import print_function

floor = 0
basement = None
for index, c in enumerate(list(raw_input("Input: "))):
    floor += 1 if c == '(' else -1

    if floor == -1 and basement is None:
        basement = index + 1

print("Answer (part1): %d" % floor)
print("Answer (part2): %d" % basement)
