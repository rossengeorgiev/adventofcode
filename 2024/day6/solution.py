
from io import StringIO
from itertools import cycle

class Mapper:
    def __init__(self, map_in):
        self.map = StringIO(map_in.replace('^', 'X')) # nice try AoC devs

        self.size_x = map_in.find('\n')
        self.size_y = map_in.count('\n')

        self.guard_y, self.guard_x = divmod(map_in.find('^'), map_in.find('\n')+1)
        self.start_y, self.start_x = self.guard_y, self.guard_x

        self.dirs = cycle([
            (0, -1), # up
            (1, 0), # right
            (0, 1), # down
            (-1, 0), # left
        ])

        self.curr_dir = next(self.dirs)
        self.loop_count = 0

    def get_pos(self, x, y):
        return (y * (self.size_y+1)) + x

    def rotate(self):
        self.curr_dir = next(self.dirs)

    def move(self):
        guard_x = self.guard_x + self.curr_dir[0]
        guard_y = self.guard_y + self.curr_dir[1]

        # guard exits map
        if not (0 <= guard_x < self.size_x and 0 <= guard_y < self.size_y):
            return False

        # encounter obstruction
        self.map.seek(self.get_pos(guard_x, guard_y))
        pos_state = self.map.read(1)

        if pos_state in '#O':
            self.rotate() # rotate 90
            return True

        # search for loops
        if self.loop_count >= 0:
            # do not place obstacles on guard start position
            # or positions the guard has already visited
            if pos_state != 'X' and not (self.start_x == guard_x and self.start_y == guard_y):
                if LoopMapper(self, self.map.tell() - 1).loop_predict():
                    self.loop_count += 1

        # regular move
        self.map.seek(self.get_pos(guard_x, guard_y))
        self.map.write('X')
        self.guard_x = guard_x
        self.guard_y = guard_y

        return True

    def predict(self):
        while self.move(): # loop stops once guard exits map area
            pass

    def print(self):
        print(self.map.getvalue())

    def count_guard_positions(self):
        return self.map.getvalue().count('X')

    def count_loop_positions(self):
        return self.loop_count

class LoopMapper(Mapper):
    def __init__(self, prev, obst_pos):
        self.parent_map = prev

        self.map = StringIO(prev.map.getvalue())
        self.map.seek(obst_pos)
        self.map.write('O')

        self.size_x = prev.size_x
        self.size_y = prev.size_y

        self.guard_x = prev.guard_x
        self.guard_y = prev.guard_y

        # we turn 90 deg here
        self.dirs = cycle([
            next(prev.dirs),
            next(prev.dirs),
            next(prev.dirs),
            next(prev.dirs),
        ])

        self.curr_dir = next(self.dirs)

        self.loop_count = -1 # disable loop searching in move()
        self.looped = False
        self.visited = {(self.guard_x, self.guard_y, self.curr_dir)}

    def rotate(self):
        super().rotate()

        # we record every position where the guard make a turn
        # in order to detect when guard has entered a loop
        pos_key = (self.guard_x, self.guard_y, self.curr_dir)

        if pos_key in self.visited:
            self.looped = True
        else:
            self.visited.add(pos_key)

    def loop_predict(self):
        while self.move(): # loop stops once guard exits map area
            if self.looped:
                return True
        return False

gmap = Mapper(open('input.txt').read())
gmap.predict()
gmap.print()

print("Answer 1: ", gmap.count_guard_positions())
print("Answer 2: ", gmap.count_loop_positions())
