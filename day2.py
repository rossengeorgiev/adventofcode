from __future__ import print_function

def paper_size(line):
    if not line: return 0
    l, w, h = map(int, line.split('x'))
    sides = [l*w, w*h, h*l]
    return sum(map(lambda x: x*2, sides)) + min(sides)

print("Input (empty line to finish): ")

answer = sum(map(paper_size, iter(raw_input, '')))

print("Answer: %d" % answer)
