
fp = open('input.txt')

from collections import Counter

lookup = {
    ']': '[',
    '}': '{',
    '>': '<',
    ')': '(',
}
rev_lookup = dict(((b, a) for a, b in lookup.items()))

pts = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
pts2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

part1 = Counter()
part2 = []

for line in fp:
    line = line.strip()
    stack = []
    is_currupt = False

    for c in line:
        if c in ('[', '(', '<', '{'):
            stack.append(c)
        elif lookup[c] == stack[-1]:
            stack.pop()
            continue
        else:
            part1[c] += 1
            is_currupt = True
            break

    # part2 - only incomplete lines past this
    if is_currupt or not stack:
        continue

    line_total = 0

    for c in stack[::-1]:
        c = rev_lookup[c]
        line_total *= 5
        line_total += pts2[c]

    part2.append(line_total)

part1 = sum((pts[c] * n for c, n in part1.items()))
part2 = sorted(part2)[(len(part2)-1) // 2]

print("Part1:", part1)
print("Part2:", part2)


