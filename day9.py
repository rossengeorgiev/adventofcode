from aoc import aoc_web_session
web = aoc_web_session()

import re
from itertools import cycle
from blist import blist

data = web.get('https://adventofcode.com/2018/day/9/input').text
n_players, n_marbles = [int(x) for x in re.search("(\d+) players; last marble is worth (\d+) points", data).groups()]


def simulate_game(n_players, n_marbles):
    scores = [0] * n_players
    gameboard = blist([0])
    center = 0

    for i in range(1, n_marbles+1):
        if i % 23 == 0:
            center = center - 7
            scores[(i - 1) % n_players] += i + gameboard.pop(center)
        else:
            center = (center + 2) % (len(gameboard) + 1)
            center = center if center else center+1
            gameboard.insert(center, i)

    #   print("[%d] %s" % (p+1, repr(gameboard)))

    score = max(scores)
    winner = scores.index(score) + 1

    return winner, score

print("Part 1: Player %s wins; score %d" % simulate_game(n_players, n_marbles))
print("Part 2: Player %s wins; score %d" % simulate_game(n_players, n_marbles*100))


