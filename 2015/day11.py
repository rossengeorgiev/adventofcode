from __future__ import print_function
from re import search

password = raw_input("Input: ")

def increment(seed):
    c = chr(((ord(seed[-1])-97+1) % 26) + 97)
    return increment(seed[:-1]) + c if c == 'a' else seed[:-1] + c

def get_next_password():
    global password
    password = increment(password)

    while (search(r'[ilo]', password)
           or not search(r'abc|bcd|cde|def|efg|fgh|pqr|qrs|'
                         r'rst|stu|tuv|uvw|vwx|wxy|xyz', password)
           or not search(r'(.)\1.*(.)\2', password)
           ):
        password = increment(password)

    return password

print("Answer (part1): %s" % get_next_password())
print("Answer (part2): %s" % get_next_password())
