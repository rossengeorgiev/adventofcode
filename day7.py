from aoc import aoc_web_session
web = aoc_web_session()

import re
from collections import defaultdict, OrderedDict

steps = web.get('https://adventofcode.com/2018/day/7/input').text
steps = re.findall(r"Step (.) must be finished before step (.) can begin.", steps)

run_queue = defaultdict(set)

for before_task, task in steps:
    run_queue[task].add(before_task)
    run_queue[before_task]

run_queue = OrderedDict(sorted(run_queue.items()))
part1 = ''

while run_queue:
    for task, before_tasks in run_queue.items():
        tasks_to_wait = before_tasks.intersection(run_queue)
        if not tasks_to_wait:
            part1 += task
            run_queue.pop(task)
            break

print("Part 1: %s" % part1)
