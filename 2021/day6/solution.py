
from functools import lru_cache

data = list(map(int, open('input.txt').readline().strip().split(',')))

@lru_cache(None)
def reproduce(fish, reprocycle=7):
    rdays, period, offset = fish
    d = max(0, period + (reprocycle - rdays) - offset)
    total_fish = 1

    for np in range(d % reprocycle, d, reprocycle):
        total_fish += reproduce((reprocycle, np, 2))

    return total_fish

def simulate(fishes, reprocycle=7, start_period=80):
    fishes = list(map(lambda day: (day, start_period, 1), sorted(fishes, reverse=True)))

    return sum(map(lambda fish: reproduce(fish, reprocycle=reprocycle), fishes))

part1 = simulate(data, start_period=80)
print("Part1:", part1)
part2 = simulate(data, start_period=256)
print("Part2:", part2)
