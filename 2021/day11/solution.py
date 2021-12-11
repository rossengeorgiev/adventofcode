
data = list(map(lambda x: list(map(int, x.strip())), open('input.txt').readlines()))

def pulse(data, x, y):
    data[x][y] = -999999

    for dx in [-1, 0, +1]:
        for dy in [-1, 0, +1]:
            xx = dx + x
            yy = dy + y
            if 0 <= xx < 10 and 0 <= yy < 10:
                if x == xx and y == yy:
                    pass
                else:
                    data[xx][yy] += 1
                    if data[xx][yy] > 9:
                        pulse(data, xx, yy)

def oprint(data, step):
    print("Step:", step)
    for y in range(10):
        for x in range(10):
            print(data[y][x], end='')
        print()
    print()


oprint(data, 0)

n_flashes = 0
for step in range(500):

    for x in range(10):
        for y in range(10):
            data[x][y] += 1

    for x in range(10):
        for y in range(10):
            if data[x][y] > 9:
                pulse(data, x, y)

    step_flashes = 0

    for x in range(10):
        for y in range(10):
            if data[x][y] < 0:
                if step < 100:
                    n_flashes += 1
                step_flashes += 1
                data[x][y] = 0

    if step == 99:
        oprint(data, step+1)

    if step_flashes == 100:
        oprint(data, step+1)
        break


print("Part1", n_flashes)
print("Part2", step+1)
