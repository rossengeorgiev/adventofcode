
from collections import Counter

data = open('input.txt').read().strip()

answer1 = None
answer2 = None

for n in range(4, len(data)):
    if answer1 is None and len(set(data[n-4:n])) == 4:
        answer1 = n

    if n>=14 and answer2 is None and len(set(data[n-14:n])) == 14:
        answer2 = n
        break

print("Answer 1", answer1)
print("Answer 2", answer2)
