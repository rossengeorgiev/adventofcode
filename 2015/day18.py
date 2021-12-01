from __future__ import print_function

def count_neighbours(x, y, lights):
    return len([None for x2 in (x-1, x, x+1) for y2 in (y-1, y, y+1)
                if (x2, y2) in lights and (x, y) != (x2, y2)
                ])

def run(lights, n, part2=False, size=100):
    broken_lights = {(0, 0), (0, 99), (99, 0), (99, 99)} if part2 else set()

    for _ in range(n):
        lights = broken_lights | {(x, y) for x in range(size) for y in range(size)
                                  if ((x, y) in lights and count_neighbours(x, y, lights) in (2, 3))
                                  or ((x, y) not in lights and count_neighbours(x, y, lights) == 3)
                                  }
    return lights

print("Input (empty line to finish): ")

lights = {(x, y) for y, row in enumerate(iter(raw_input, ''))
          for x, state in enumerate(row) if state == '#'}

print("Answer (part1): %s" % len(run(lights, 100)))
print("Answer (part1): %s" % len(run(lights, 100, part2=True)))
