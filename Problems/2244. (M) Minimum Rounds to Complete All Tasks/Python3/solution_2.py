class Solution:
  def minimumRounds(self, tasks: List[int]) -> int:
    # pack tasks in dictionary
    t_d = {}
    for i in tasks:
      if i in t_d:
        t_d[i] += 1
      else:
        t_d[i] = 1

    rnd = 0
    # for all difficulty levels
    for diff in t_d:
      while True:
        # impossible to solve
        if t_d[diff] == 1:
          return -1
        # 1 round remaining
        if t_d[diff] in [2, 3]:
          rnd += 1
          break
        # 2 rounds remaining
        elif t_d[diff] in [4, 5, 6]:
          rnd += 2
          break
        # do 3 tasks
        else:
          rnd += 1
          t_d[diff] -= 3

    return rnd

