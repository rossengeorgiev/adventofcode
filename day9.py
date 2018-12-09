from aoc import aoc_web_session
web = aoc_web_session()

import re
from collections import deque, Counter

data = web.get('https://adventofcode.com/2018/day/9/input').text
n_players, n_marbles = [int(x) for x in re.search("(\d+) players; last marble is worth (\d+) points", data).groups()]

def simulate_game(n_players, n_marbles):
    scores = Counter()
    circle = deque([0])

    for i in range(1, n_marbles+1):
        if i % 23 == 0:
            circle.rotate(7)
            scores[i % n_players] += i + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)

    return scores.most_common(1)[0][1]

print("Part 1: Winner score %d" % simulate_game(n_players, n_marbles))
print("Part 2: Winner score %d" % simulate_game(n_players, n_marbles*100))
