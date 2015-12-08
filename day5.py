from __future__ import print_function
from re import findall

def naughty_or_nice(line):
    if len(findall("[aeiou]", line)) < 3:
        return False
    if not findall("([a-z])\\1", line):
        return False
    if findall("(ab|cd|pq|xy)", line):
        return False
    return True

print("Input (empty line to finish): ")

answer = map(naughty_or_nice, iter(raw_input, '')).count(True)

print("Answer: %d" % answer)
