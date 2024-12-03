
import re

re_instr = r"(do|don't|mul)\((?:(\d+),(\d+))?\)",

answer1 = answer2 = 0
enabled = True

for op, a, b in (m.groups() for m in re.finditer(re_instr, open("input.txt").read())):
    match op:
        case "do":
            enabled = True
        case "don't":
            enabled = False
        case "mul":
            answer1 += int(a) * int(b)
            if enabled:
                answer2 += int(a) * int(b)

print("Answer 1: ", answer1)
print("Answer 2: ", answer2)
