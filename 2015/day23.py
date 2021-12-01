from __future__ import print_function
from collections import defaultdict
import re

print("Input program instrctions (blank line to finish):")

raw = '\n'.join(iter(raw_input, ''))
program = re.findall("(\w+) ([a-z]|[+\-0-9]+)(, ([a-z]|[+\-0-9]+))?", raw)

def execute(program, regs={}):
    regs = defaultdict(int, regs)
    IP = 0

    while len(program) > IP:
        inst, a, _, b = program[IP]

        if inst == "inc":
            regs[a] += 1
        elif inst == "hlf":
            regs[a] /= 2
        elif inst == "tpl":
            regs[a] *= 3
        elif inst == "jmp":
            IP += int(a) - 1
        elif inst == "jie" and regs[a] % 2 == 0:
            IP += int(b) - 1
        elif inst == "jio" and regs[a] == 1:
            IP += int(b) - 1

        IP += 1

    return regs['b']

print("Answer (part1): %s" % execute(program))
print("Answer (part2): %s" % execute(program, regs={'a': 1}))
