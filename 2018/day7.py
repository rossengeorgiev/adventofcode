from aoc import aoc_web_session
web = aoc_web_session()

import re
from itertools import count as count_from
from collections import defaultdict, OrderedDict

steps = web.get('https://adventofcode.com/2018/day/7/input').text
steps = re.findall(r"Step (.) must be finished before step (.) can begin.", steps)

run_queue = defaultdict(set)

for before_task, task in steps:
    run_queue[task].add(before_task)
    run_queue[before_task]

run_queue = sorted(run_queue.items())

def executor(run_queue):
    run_queue = OrderedDict(run_queue)
    task_sequence = ''

    while run_queue:
        for task, before_tasks in list(run_queue.items()):
            tasks_to_wait = before_tasks.intersection(run_queue)
            if not tasks_to_wait:
                task_sequence += task
                run_queue.pop(task)
                break

    return task_sequence

def threaded_executor(run_queue, n_threads=1):
    run_queue = OrderedDict(run_queue)
    task_sequence = ''

    threads = dict()

    for clock in count_from(0):
        for task in list(threads):
            threads[task] -= 1
            if threads[task] == 0:
                threads.pop(task)
                task_sequence += task

        while run_queue and len(threads) < n_threads:
            task_started = False
            for task, before_tasks in list(run_queue.items()):
                tasks_to_wait = before_tasks.intersection(list(run_queue) + list(threads))
                if not tasks_to_wait:
                    threads[task] = 60 + ord(task) - 64
                    run_queue.pop(task)
                    task_started = True
                    break
            if not task_started:
                break

        if not run_queue and not threads:
            break

    return task_sequence, clock

print("Part 1: %s" % executor(run_queue))
print("-- multi threaded --")
print("Part 1: %s (%d seconds, 1 worker)" % threaded_executor(run_queue, 1))
print("Part 2: %s (%d seconds, 5 workers)" % threaded_executor(run_queue, 5))
