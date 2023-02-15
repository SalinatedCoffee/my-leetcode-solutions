class Solution:
  def minimumRounds(self, tasks: List[int]) -> int:
    # pack tasks in dictionary
    t_d = {}
    for i in tasks:
      if i in t_d:
        t_d[i] += 1
      else:
        t_d[i] = 1

    # sanity check
    if 1 in t_d.values():
      return -1

    rnd, idx = 0, 0
    diff = list(t_d.keys())
    # for all difficulty levels
    while idx < len(diff):
      # all tasks finished
      if not t_d[diff[idx]]:
        break
      # can finish in 1 round
      if t_d[diff[idx]] in [2, 3]:
        rnd += 1
        idx += 1
      # can finish in 2 rounds
      elif t_d[diff[idx]] in [4, 5, 6]:
        rnd += 2
        idx += 1
      # do 3 tasks
      else:
        rnd += 1
        t_d[diff[idx]] -= 3

    return rnd
