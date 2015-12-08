from __future__ import print_function

def parse_dimensions(line):
    if not line: return 0
    return map(int, line.split('x'))

def paper_size(d):
    l, w, h = d
    sides = [l*w, w*h, h*l]
    return sum(map(lambda x: x*2, sides)) + min(sides)

def ribbon_length(d):
    length = reduce(lambda a,b: a*b, d)
    d.pop(d.index(max(d)))
    return length + sum(d*2)

print("Input (empty line to finish): ")

data = map(parse_dimensions, iter(raw_input, ''))

print("Answer (part1): %d" % sum(map(paper_size, data)))
print("Answer (part2): %d" % sum(map(ribbon_length, data)))
