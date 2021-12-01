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

def naughty_or_nice_2point0(line):
    if not findall("([a-z]{2}).*\\1", line):
        return False
    if not findall("([a-z])[a-z]\\1", line):
        return False
    return True

print("Input (empty line to finish): ")

words = list(iter(raw_input, ''))

answer = map(naughty_or_nice, words).count(True)
print("Answer (part1): %d" % answer)
answer = map(naughty_or_nice_2point0, words).count(True)
print("Answer (part2): %d" % answer)
