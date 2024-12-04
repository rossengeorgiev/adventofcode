
import re

data = open("input.txt").read()
ll = data.find('\n')

regex_go_brrr = [
    r"XMAS", # h-foward
    r"SAMX", # h-reverse
    "X(?=.{{{ll}}}M.{{{ll}}}A.{{{ll}}}S)".format(ll=ll), # v-forward
    "S(?=.{{{ll}}}A.{{{ll}}}M.{{{ll}}}X)".format(ll=ll), # v-reverse
    "X(?=.{{{ll}}}M.{{{ll}}}A.{{{ll}}}S)".format(ll=ll+1), # dp-forward
    "S(?=.{{{ll}}}A.{{{ll}}}M.{{{ll}}}X)".format(ll=ll+1), # dp-reverse
    "X(?=.{{{ll}}}M.{{{ll}}}A.{{{ll}}}S)".format(ll=ll-1), # ds-forward
    "S(?=.{{{ll}}}A.{{{ll}}}M.{{{ll}}}X)".format(ll=ll-1), # ds-reverse
]
regex_go_brrr2 = [
    "(?=M.M.{{{dp}}}A.{{{ds}}}S.S)".format(dp=ll-1, ds=ll-1),
    "(?=S.S.{{{dp}}}A.{{{ds}}}M.M)".format(dp=ll-1, ds=ll-1),
    "(?=M.S.{{{dp}}}A.{{{ds}}}M.S)".format(dp=ll-1, ds=ll-1),
    "(?=S.M.{{{dp}}}A.{{{ds}}}S.M)".format(dp=ll-1, ds=ll-1),
]

answer1 = answer2 = 0

for pat in regex_go_brrr:
    answer1 += len(re.findall(pat, data, re.DOTALL))
for pat in regex_go_brrr2:
    answer2 += len(re.findall(pat, data, re.DOTALL))

print("Answer 1: ", answer1)
print("Answer 2: ", answer2)
