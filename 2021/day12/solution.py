
import re

data = open('input.txt').readlines()


class Vertex(object):
    links = set()
    visits = 0
    max_visits = False

    def __init__(self, name):
        self.name = name
        self.links = set()
        self.is_small = not not re.match('^[a-z]+$', self.name)
        self.is_cave = self.name not in ('start', 'end')

    def __repr__(self):
        return "Vertex({})".format(self.name)

    def connect(self, b):
        if b not in self.links:
            self.links.add(b)
            b.connect(self)

def get_vertex(name):
    if name not in graph:
        graph[name] = Vertex(name)
    return graph[name]


# build graph
graph = {}
for line in data:
    a, b = line.strip().split('-')
    get_vertex(a).connect(get_vertex(b))


def find_paths(node, small_visits=1):
    if node.name == 'end':
        return [['end']]

    paths = []

    for link in node.links:
        if link.name == 'start' or link.visits >= small_visits:
            continue

        if link.is_cave and link.is_small:
            link.visits += 1

        if not Vertex.max_visits and link.visits == small_visits:
            Vertex.max_visits = link

        for path in find_paths(link, 1 if Vertex.max_visits else small_visits):
                paths.append([node.name] + path)

        if Vertex.max_visits == link:
            Vertex.max_visits = False

        link.visits = max(0, link.visits - 1)

    return paths


part1 = len(find_paths(graph['start'], small_visits=1))

# reset for part2
Vertex.max_visits = False
for node in graph.values():
    node.visits = 0

part2 = len(find_paths(graph['start'], small_visits=2))

print("Part1:", part1)
print("Part2:", part2)
