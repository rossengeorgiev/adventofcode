from __future__ import print_function
import re

print("Input (empty line to finish): ")

def V(var):
    result = eval(circuit[var])
    circuit[var] = str(result)
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

print("Answer: %d" % V('a'))
