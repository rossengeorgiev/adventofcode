
elfs = [sum(map(int, elf.rstrip('\n').split('\n'))) for elf in open('input.txt').read().split('\n\n')]

print("Answer 1: ", max(elfs))
print("Answer 2: ", sum(sorted(elfs)[-3:]))
