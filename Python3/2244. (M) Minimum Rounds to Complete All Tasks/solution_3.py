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
    for diff in t_d:
      # impossible to solve
      if t_d[diff] == 1:
        return -1
      # modulo 3
      rem = t_d[diff] % 3
      # if remainder is 1 or 2, need one more round
      if rem in [1, 2]:
        rnd += t_d[diff] // 3 + 1
      # if no remainder, no extra round needed
      else:
        rnd += t_d[diff] // 3

    return rnd

