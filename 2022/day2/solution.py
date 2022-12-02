
result1 = {
  ("A", "X"): 1+3, # rock, rock
  ("A", "Y"): 2+6, # rock, paper
  ("A", "Z"): 3+0, # rock, sci

  ("B", "X"): 1+0, # paper, rock
  ("B", "Y"): 2+3, # paper, paper
  ("B", "Z"): 3+6, # paper, sci

  ("C", "X"): 1+6, # sci, rock
  ("C", "Y"): 2+0, # sci, paper
  ("C", "Z"): 3+3, # sci, sci
}

result2 = {
  ("A", "X"): 3+0, # rock, lose (sci)
  ("A", "Y"): 1+3, # rock, draw (rock)
  ("A", "Z"): 2+6, # rock, win  (paper)

  ("B", "X"): 1+0, # paper, lose (rock)
  ("B", "Y"): 2+3, # paper, draw (paper)
  ("B", "Z"): 3+6, # paper, win  (sci)

  ("C", "X"): 2+0, # sci, lose (paper)
  ("C", "Y"): 3+3, # sci, draw (sci)
  ("C", "Z"): 1+6, # sci, win  (rock)
}

strategy = [
    tuple(rnd.strip().split(' '))
    for rnd in open('input.txt').readlines()
]

print("Answer 1", sum((result1[rnd] for rnd in strategy)))
print("Answer 2", sum((result2[rnd] for rnd in strategy)))
