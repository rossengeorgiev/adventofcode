from __future__ import print_function
import re

def mixtures(n, total):
    start = total if n == 1 else 0

    for i in range(start, total+1):
        left = total - i
        if n-1:
            for y in mixtures(n-1, left):
                yield [i] + y
        else:
            yield [i]

def score(recipe, max_calories=0):
    proportions = [map(lambda x:x*mul, props) for props, mul in zip(ingredients.values(), recipe)]
    dough = reduce(lambda a, b: map(sum, zip(a, b)), proportions)
    calories = dough.pop()
    result = reduce(lambda a, b: a*b, map(lambda x: max(x, 0), dough))
    return 0 if max_calories and calories > max_calories else result

print("Input (empty line to finish): ")

ingredients = {}

for line in iter(raw_input, ''):
    name, rest = line.split(":")
    ingredients[name] = map(int, re.sub("[a-z ]+", '', rest).split(','))

print("Answer (part1): %s" % max(map(score, mixtures(len(ingredients), 100))))
print("Answer (part2): %s" % max(map(lambda r: score(r, 500), mixtures(len(ingredients), 100))))
