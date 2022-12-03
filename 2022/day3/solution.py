
def score(item):
    n = ord(item) - 64
    return n-32 if n>26 else n+26

sacks = [sack.strip() for sack in open('input.txt').readlines()]
dups = []

for sack in sacks:
    pocket_a, pocket_b = set(sack[:len(sack)/2]), set(sack[len(sack)/2:])
    dup = pocket_a.intersection(pocket_b).pop()
    dups.append(dup)

badges = []
sacks.reverse()

while sacks:
    badge = set(sacks.pop()).intersection(set(sacks.pop()))
    badge = badge.intersection(set(sacks.pop()))
    badges.append(badge.pop())

print("Answer 1", sum(map(score, dups)))
print("Answer 2", sum(map(score, badges)))
