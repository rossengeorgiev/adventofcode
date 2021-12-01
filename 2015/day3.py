from __future__ import print_function

a = raw_input("Input: ")

direction_map = {
    '^': lambda x, y: (x, y+1),
    'v': lambda x, y: (x, y-1),
    '>': lambda x, y: (x+1, y),
    '<': lambda x, y: (x-1, y),
}

def follow_route(n_santas):
    santas = dict(enumerate([(0, 0)]*n_santas))
    houses_visited = [(0, 0)] * n_santas

    for i, c in enumerate(list(a)):
        xy = santas[i % n_santas]
        xy = santas[i % n_santas] = direction_map[c](*xy)
        houses_visited.append(xy)

    return len(set(houses_visited))

print("Answer (part1): %d" % follow_route(1))
print("Answer (part2): %d" % follow_route(2))
