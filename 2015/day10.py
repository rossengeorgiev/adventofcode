from __future__ import print_function
from re import sub

seq = raw_input("Input: ")

def mutate(match):
    subseq = match.group()
    return str(len(subseq)) + subseq[0]

def run(times):
    global seq
    for _ in range(times):
        seq = sub(r'(\d)\1*', mutate, seq)
    return len(seq)

print("Answer (part1): %s" % run(40))
print("Answer (part2): %s" % run(10))
