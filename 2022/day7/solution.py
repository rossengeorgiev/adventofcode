
from collections import defaultdict

output = (line.rstrip() for line in open('input.txt'))
next(output) # skip cd /

path = [{'_name':'/'}]
dirsizes = defaultdict(int)


for line in output:
    if line == '$ ls':
        continue

    if line[:4] == '$ cd':
        if line[-1] == '.':
            path.pop()
        else:
            _, _, dirname = line.split(' ', 2)
            path.append(path[-1][dirname])
        continue

    column1, name = line.split(' ')

    if column1 == 'dir':
        path[-1][name] = {
            '_name': name,
        }
    else:
        for dirn in range(len(path), 0, -1):
            key = '/'.join((d['_name'] for d in path[:dirn]))
            dirsizes[key] += int(column1)

print("Answer 1", sum(filter(lambda x: x<=100000, dirsizes.values())))

freespace = 70000000 - max(dirsizes.values())

for size in sorted(dirsizes.values()):
    if freespace + size >= 30000000:
        print("Answer 2", size)
        break

