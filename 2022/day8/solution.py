

treemap = [
    [int(tree) for tree in line.rstrip()]
    for line in open('input.txt')
]

visible = 0
scores = []

def score(line, tree):
    score = 0
    for n in line:
        score += 1
        if n >= tree:
            break
    return score

for y, row in enumerate(treemap, 0):
    for x, tree in enumerate(row, 0):
        if (x == 0 or x == len(row)-1) or (y == 0 or y == len(treemap)-1):
            visible += 1
        else:
            west = max(row[:x])
            east = max(row[x+1:])
            north = max((row[x] for row in treemap[:y]))
            south = max((row[x] for row in treemap[y+1:]))
            if tree > min([west, east, north, south]):
                visible += 1

            scores.append(
                score(row[x-1::-1], tree)
                * score(row[x+1:], tree)
                * score((row[x] for row in treemap[y-1::-1]), tree)
                * score((row[x] for row in treemap[y+1:]), tree)
            )

print("Answer 1", visible)
print("Answer 2", max(scores))

