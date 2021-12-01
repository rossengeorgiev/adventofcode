from __future__ import print_function
import re

print("Input (empty line to finish): ")

def V(var):
    result = eval(live_circuit[var])
    live_circuit[var] = str(result)
    return result

operations = {
    'AND': '&',
    'OR': '|',
    'LSHIFT': '<<',
    'RSHIFT': '>>',
    'NOT': '0xffff ^'
}
circuit = {}

for line in iter(raw_input, ''):
    expr, var = re.findall(r"(.+) -> (.+)", line)[0]

    expr = expr.split(' ')

    for i, part in enumerate(expr):
        if not part.isdigit():
            expr[i] = operations[part] if part in operations else "V('%s')" % part

    circuit[var] = ' '.join(expr)

live_circuit = circuit.copy()
answer = V('a')
print("Answer (part1): %d" % answer)

live_circuit = circuit.copy()
live_circuit['b'] = str(answer)
answer = V('a')
print("Answer (part2): %d" % answer)
