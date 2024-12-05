
import re
import functools

rules, printo = open("input.txt").read().split("\n\n")

rules = [tuple(map(int, line.split('|'))) for line in rules.rstrip('\n').split('\n')]
printo = [tuple(map(int, line.split(','))) for line in printo.rstrip('\n').split('\n')]

answer1 = answer2 = 0

def cmp_pages(a, b):
    if (a, b) in rules:
        return -1
    if (b, a) in rules:
        return 1
    if a == b:
        return 0
    return -1 if a < b else 1

for update in printo:
    good = True

    for bpage, page in rules:
        try:
            if update.index(bpage) > update.index(page):
                good = False

                good_update = sorted(update, key=functools.cmp_to_key(cmp_pages))
                answer2 += good_update[int((len(update)-1)/2)]

                break
        except ValueError:
            continue

    if good:
        answer1 += update[int((len(update)-1)/2)]

print("Answer 1: ", answer1)
print("Answer 2: ", answer2)
