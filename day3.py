from __future__ import print_function

a = raw_input("Input: ")

direction_map = {
    '^': lambda: (x, y+1),
    'v': lambda: (x, y-1),
    '>': lambda: (x+1, y),
    '<': lambda: (x-1, y),
}

x = y = 0
house_visited = [(x, y)]

for c in list(a):
    x, y = direction_map[c]()
    house_visited.append((x, y))

print("Answer: %d" % len(set(house_visited)))
