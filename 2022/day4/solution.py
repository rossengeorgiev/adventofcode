
pairs = [line.strip().split(',') for line in open('input.txt').readlines()]

answer1 = 0
answer2 = 0

for section_a, section_b in pairs:
    a_start, a_end = tuple(map(int, section_a.split('-')))
    b_start, b_end = tuple(map(int, section_b.split('-')))

    # ensure a is the shorter of the pairs
    if (a_end - a_start) > (b_end - b_start):
        a_start, a_end, b_start, b_end = b_start, b_end, a_start, a_end

    if a_start >= b_start and a_end <= b_end:
        answer1 += 1

    if (b_start <= a_start <= b_end) or (b_start <= a_end <= b_end):
        answer2 += 1

print("Answer 1", answer1)
print("Answer 2", answer2)

