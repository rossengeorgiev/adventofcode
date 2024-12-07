
data = [
    (
        int(line.split(': ',1)[0]),
        [int(d) for d in line.rstrip('\n').split(': ',1)[1].split(' ')]
    )
    for line in open('input.txt')
]

answer1 = answer2 = 0

def calculate(total, numbers, ver=1):
    if numbers:
        yield from calculate(total + numbers[0], numbers[1:], ver=ver)
        if total > 0:
            yield from calculate(total * numbers[0], numbers[1:], ver=ver)
            if ver == 2:
                yield from calculate(int(str(total) + str(numbers[0])), numbers[1:], ver=ver)
    else:
        yield total

for total, numbers in data:
    for result in calculate(0, numbers):
        if result == total:
            answer1 += total
            break

    for result in calculate(0, numbers, ver=2):
        if result == total:
            answer2 += total
            break

print("Answer 1: ", answer1)
print("Answer 2: ", answer2)
