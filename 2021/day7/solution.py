
from functools import lru_cache

crabs = tuple(map(int, open('input.txt').readline().strip().split(',')))

@lru_cache(None)
def calc_fuel(crabs, pos):
    return sum(map(lambda x: abs(x - pos), crabs))


@lru_cache(None)
def calc_fuel_part2(crabs, pos):
    return sum(map(lambda y: (y*(1+y))//2,
               map(lambda x: abs(x - pos), crabs)
               ))

def find_position(crabs, cost=calc_fuel):
    start, end = min(crabs), max(crabs)

    if start > end:
        start, end = end, start

    step = (end - start) // 2
    pos = start + step

    while True:
        curr = cost(crabs, pos)
        if curr > cost(crabs, pos + 1):
            pos += step
        elif curr > cost(crabs, pos - 1):
            pos -= step
        else:
            return curr

        step = max(1, (step // 2))


part1 = find_position(crabs)
print("part1:", part1)
part2 = find_position(crabs, cost=calc_fuel_part2)
print("part2:", part2)
