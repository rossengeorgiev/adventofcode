from __future__ import print_function
import re

def find_and_sum_ints(text):
    return sum(map(int, re.findall(r'-?\d+', text)))

def sub_reduce(match):
    text = match.group()
    if ':"red"' not in text:
        return str(find_and_sum_ints(text))
    return '0'

def no_red_sum(data):
    while not data.isdigit():
        data = re.sub(r'{[^{}]+}', sub_reduce, data)
    return int(data)

print("Input (empty line to finish): ")

data = ''.join(list(iter(raw_input, '')))

print("Answer (part1): %s" % find_and_sum_ints(data))
print("Answer (part2): %s" % no_red_sum(data))
