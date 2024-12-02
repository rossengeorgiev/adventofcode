
levels = [tuple(map(int, line.split(' '))) for line in open('input.txt')]

answer1, answer2 = 0, 0

def is_safe(level):
    diffs = [b-a for a, b in zip(level[:-1], level[1:])]
    return all((0<diff<=3 for diff in diffs)) or all((0>diff>=-3 for diff in diffs))

def tolerate_unsafe(level):
    for idx in range(len(level)):
        if is_safe(level[0:idx] + level[idx+1:]):
            return True

for level in levels:
    if is_safe(level):
        answer1 += 1
    elif tolerate_unsafe(level):
        answer2 += 1

print("Answer 1: ", answer1)
print("Answer 2: ", answer1 + answer2)
