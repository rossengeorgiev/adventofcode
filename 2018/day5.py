from aoc import aoc_web_session
web = aoc_web_session()

from string import ascii_lowercase
import re
from collections import defaultdict

chemical = web.get('https://adventofcode.com/2018/day/5/input').text.strip()

pairs = '|'.join(("%s%s|%s%s" % (x, x.upper(), x.upper(), x) for x in ascii_lowercase))

def react(chemical):
    while True:
        chemical, reacted = re.subn(pairs, '', chemical)
        if not reacted:
            break
    return chemical

chemical = react(chemical)

print("Part 1: %s" % len(chemical))

answer = min((len(react(re.sub(l, '', chemical, flags=re.I))) for l in ascii_lowercase))

print("Part 2: %s" % answer)
