
import operator

l_list, r_list = zip(*(tuple(map(int, line.split('   '))) for line in open('input.txt')))

print("Answer 1: ", sum(( abs(a-b) for a, b in zip(sorted(l_list), sorted(r_list)) )))

print("Answer 2: ", sum((a * r_list.count(a) for a in l_list)))
