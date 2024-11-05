class Solution:
  def minChanges(self, s: str) -> int:
    # greedy

    n = len(s)
    res = 0
    # check all adjacent character pairs
    for i in range(1, n, 2):
      # if characters are different, a single move is required
      if s[i-1] != s[i]:
        res += 1

    return res

