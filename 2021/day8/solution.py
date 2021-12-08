
fp = ((a.split(' '), b.split(' ')) for a,b in (line.strip().split(' | ') for line in open('input.txt')))

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

# 1 = 2 x
# 7 = 3 x
# 4 = 4 x

# 2 = 5
# 3 = 5
# 5 = 5

# 6 = 6
# 0 = 6
# 9 = 6

# 8 = 7 x

easy = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}

count = 0
count_p2 = 0

for signals, reading in fp:
    for signal in signals:
        n = easy.get(len(signal), None)
        if n == 1:
            one = set(signal)
        elif n == 4:
            four = set(signal)

    num = ''
    for signal in reading:
        signal = set(signal)

        n = easy.get(len(signal), None)
        if n is not None:
            count += 1
            num += str(n)
        elif len(signal) == 5:
            if len(signal.intersection(one)) == 2:
                num += '3'
            elif len(signal.intersection(four)) == 2:
                num += '2'
            else:
                num += '5'
        elif len(signal) == 6:
            if len(signal.intersection(one)) == 1:
                num += '6'
            elif len(signal.intersection(four)) == 4:
                num += '9'
            else:
                num += '0'

    count_p2 += int(num)

print('part1:', count)
print('part2:', count_p2)

