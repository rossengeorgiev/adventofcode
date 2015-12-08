from __future__ import print_function
from hashlib import md5

key = raw_input("Input: ")

answer = 1
while not md5("%s%d" % (key, answer)).hexdigest().startswith("00000"):
    answer += 1

print("Answer: %d" % answer)
