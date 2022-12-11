
import re, math, operator
from functools import reduce

class Monkey:
    crew = {}
    items_inspected = 0
    common_div = 1

    def __init__(self, text):
        lines = re.sub("(  |[:,])", "", text).split("\n")
        self.id = int(lines[0].split(" ", 1)[1])

        self.items = list(map(int, lines[1].split(" ")[2:]))
        self.op, self.op_param = lines[2].split(" ")[-2:]
        self.test = int(lines[3].split(" ")[-1])
        Monkey.common_div *= self.test
        self.throw_true = int(lines[4].split(" ")[-1])
        self.throw_false = int(lines[5].split(" ")[-1])

        Monkey.crew[self.id] = self

    def throw(self, monkey, item):
        Monkey.crew[monkey].catch(item)

    def catch(self, item):
        self.items.append(item)

    def inspect(self, care_free=False):
        for item in self.items:
            self.items_inspected += 1

            param = item if self.op_param == "old" else int(self.op_param)

            if self.op == "*":
                item = item * param
            elif self.op == "+":
                item = item + param
            else:
                raise NotImplemented("Monkey operation %s" % self.op)

            if not care_free:
                item //= 3
            else:
                item %= self.common_div

            if item % self.test == 0:
                self.throw(self.throw_true, item)
            else:
                self.throw(self.throw_false, item)

        self.items.clear()


monkeys = [monkey for monkey in open('input.txt').read().split("\n\n")]

# part 1
crew = [Monkey(m) for m in monkeys]

for rnd in range(20):
    for monkey in crew:
        monkey.inspect()

answer1 = reduce(operator.mul, sorted((monkey.items_inspected for monkey in crew))[-2:])

print("Answer 1", answer1)

Monkey.crew.clear()
crew = [Monkey(m) for m in monkeys]

for rnd in range(10000):
    for monkey in crew:
        monkey.inspect(care_free=True)

answer2 = reduce(operator.mul, sorted((monkey.items_inspected for monkey in crew))[-2:])

print("Answer 2", answer2)
