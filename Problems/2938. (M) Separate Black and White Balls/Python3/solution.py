class Solution:
  def minimumSteps(self, s: str) -> int:
    # greedy algorithm

    n = len(s)
    # cur is previously seen number of 1s
    cur, res = 0, 0
    for i in range(n):
      if s[i] == '1':
        cur += 1
      else:
        res += cur

    return res

