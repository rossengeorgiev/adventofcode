
prog = (line.rstrip() for line in open('input.txt'))

x = 1
cycle = 0
sprite = 0
answer1 = 0
answer2 = []

def tick():
    global x, cycle, answer1

    pixel = (cycle % 40)
    if cycle and pixel == 0:
       answer2.append('\n')
    answer2.append("#" if sprite <= pixel <= sprite+2 else " ")

    cycle += 1
    if cycle in (20, 60, 100, 140, 180, 220):
        answer1 += x * cycle

for op in prog:
    if op == 'noop':
        tick()
    elif op.startswith("addx"):
        tick()
        tick()
        _, val = op.split(' ', 1)
        x += int(val)
        sprite = x-1


print("Answer 1", answer1)
print("Answer 2:\n", ''.join(answer2))
