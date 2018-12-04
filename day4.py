from aoc import aoc_web_session
web = aoc_web_session()

import re
from collections import defaultdict

records = web.get('https://adventofcode.com/2018/day/4/input').text
records = '\n'.join(sorted(records.split('\n')))

guards = defaultdict(lambda: [0]*60)
guard_id = None
sleep_start = None

for minute, record in re.findall(r':(\d+)\] (.*?)$', records, re.M):
    if record.endswith('begins shift'):
        guard_id = int(record.split(' ')[1][1:])
    elif record.endswith('falls asleep'):
        sleep_start = int(minute)
    elif record.endswith('wakes up'):
        for i in range(sleep_start, int(minute)):
            guards[guard_id][i] += 1

for part, func in ((1, sum), (2, max)):
    guard_id, _ = max(map(lambda x: (x[0], func(x[1])),
                          guards.items()),
                      key=lambda y: y[1])

    top_minute = guards[guard_id].index(max(guards[guard_id]))

    print("Part %s: %s" % (part, guard_id * top_minute))
