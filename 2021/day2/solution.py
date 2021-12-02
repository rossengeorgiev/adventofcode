

commands = ((cmd, -int(n) if cmd == 'up' else int(n)) for cmd, n in map(lambda x: x.split(' '), open('input.txt')))


depth = 0
depth2 = 0
distance = 0
aim = 0

for cmd, n in commands:
    if cmd == 'forward':
        distance += n
        depth2 += aim * n
    else:
        depth += n
        aim += n


print("Part1:", depth * distance)
print("Part2:", depth2 * distance)

