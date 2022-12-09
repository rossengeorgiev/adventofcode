
moves = (move.rstrip().split(' ') for move in open('input.txt'))

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, pos):
        self.x += pos.x
        self.y += pos.y

    def follow(self, pos):
        dx = pos.x - self.x
        dy = pos.y - self.y

        if abs(dx) > 1 or abs(dy) > 1:
            self.x += dx//2 if abs(dx) > 1 else dx
            self.y += dy//2 if abs(dy) > 1 else dy

    def get_position(self):
        return (self.x, self.y)

dirmap = {
    'U': Position( 0,  1),
    'D': Position( 0, -1),
    'R': Position( 1,  0),
    'L': Position(-1,  0),
}

rope1 = [Position(0, 0) for _ in range(2)]
rope2 = [Position(0, 0) for _ in range(10)]

visited1 = set([(0, 0)])
visited2 = set([(0, 0)])

for direction, steps in moves:
    direction = dirmap[direction]

    for _ in range(int(steps)):
        # part1
        rope1[0].move(direction)
        rope1[-1].follow(rope1[0])
        visited1.add(rope1[-1].get_position())
        # part2
        rope2[0].move(direction)
        for i, knot in enumerate(rope2[1:], 0):
            knot.follow(rope2[i])
        visited2.add(rope2[-1].get_position())


print("Answer 1:", len(visited1))
print("Answer 2:", len(visited2))
