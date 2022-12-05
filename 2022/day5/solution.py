
from collections import defaultdict, deque

stacks_text, moves = open('test.txt').read().split('\n\n', 1)

# process initial stack configuration
stacks_text = stacks_text.split('\n')
stacks_n = (len(stacks_text.pop()) + 1) / 4

stacks1 = defaultdict(deque)
stacks2 = defaultdict(deque)

while stacks_text:
    line = stacks_text.pop()
    for i, crate_i in enumerate(range(0, stacks_n*4, 4), 1):
        crate = line[crate_i+1:crate_i+2]
        if crate != ' ':
            stacks1[i].append(crate)
            stacks2[i].append(crate)

# perform crane moves
for move in moves.strip().split('\n'):
    _, n, _, src , _, dst = move.split(' ', 5)
    n, src, dst = int(n), int(src), int(dst)

    stacks2[src].rotate(n)

    for _ in range(n):
        stacks1[dst].append(stacks1[src].pop())
        stacks2[dst].append(stacks2[src].popleft())


# calculate answers
answer1 = ''.join([stack.pop() for stack in stacks1.values()])
answer2 = ''.join([stack.pop() for stack in stacks2.values()])

print("Answer 1", answer1)
print("Answer 2", answer2)
