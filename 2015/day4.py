from __future__ import print_function
from hashlib import md5
from re import search

key = raw_input("Input: ")

answers = {
    '0'*5: None,
    '0'*6: None,
}
answers_remaining = len(answers)
count = 1
while answers_remaining:
    r = search(r"^000000?", md5("%s%d" % (key, count)).hexdigest())

    if r and not answers[r.group()]:
        answers[r.group()] = count
        answers_remaining -= 1

    count += 1

print("Answer (part1): %d" % answers['0'*5])
print("Answer (part2): %d" % answers['0'*6])
