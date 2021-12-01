from aoc import aoc_web_session
web = aoc_web_session()

data = web.get('https://adventofcode.com/2018/day/8/input').text
data = [int(n) for n in data.split(' ')]

class Node(object):
    def __init__(self):
        self.children = list()
        self.metadata = list()
        self.metadata_sum = 0
        self.value = 0

def parse_node(data):
    n_children = data[0]
    n_metadata = data[1]
    data = data[2:]

    node = Node()

    for _ in range(n_children):
        child, data = parse_node(data)
        node.children.append(child)
        node.metadata_sum += child.metadata_sum

    if n_metadata:
        node.metadata, data = data[:n_metadata], data[n_metadata:]
        node.metadata_sum += sum(node.metadata)

        if n_children == 0:
            node.value = node.metadata_sum
        else:
            for idx in node.metadata:
                if idx <= len(node.children):
                    node.value += node.children[idx-1].value

    return node, data


root, _ = parse_node(data)

print("Part 1: %s" % root.metadata_sum)
print("Part 2: %s" % root.value)
