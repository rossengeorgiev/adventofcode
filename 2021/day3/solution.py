
import operator
from functools import reduce
from collections import Counter, defaultdict

report = list(map(str.strip, open('input.txt')))

def count_bits(report):
    bitcount = defaultdict(Counter)

    for reading in report:
        for i, bit in enumerate(reading):
            bitcount[i][bit] += 1

    return bitcount

def calculate_part1(bitcount):
    bits = reduce(operator.add, ([x[0] for x in bit.most_common()] for bit in bitcount.values()))
    gamma = int(''.join(bits[0::2]), 2)
    epsilon = int(''.join(bits[1::2]), 2)

    return gamma * epsilon

part1 = calculate_part1(count_bits(report))
print("Part1:", part1)

o2report = co2report = report

def dumb(counter, even):
    (most , x), (least, y) = counter.most_common()
    if x == y:
        return even
    else:
        return most if even == '1' else least

for i in range(len(report[0])):
   if len(o2report) > 1:
       o2c = Counter((reading[i] for reading in o2report))
       o2report = [reading for reading in o2report if reading[i] == dumb(o2c, '1')]
   if len(co2report) > 1:
       co2c = Counter((reading[i] for reading in co2report))
       co2report = [reading for reading in co2report if reading[i] == dumb(co2c, '0')]


part2 = int(o2report[0], 2) * int(co2report[0], 2)
print("Part2:", part2)






