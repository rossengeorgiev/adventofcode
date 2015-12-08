from __future__ import print_function

a = raw_input("Input: ")

print("Answer: %d" % ( a.count('(') - a.count(')') ))
