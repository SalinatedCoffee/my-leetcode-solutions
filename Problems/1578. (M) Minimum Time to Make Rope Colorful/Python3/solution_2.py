class Solution:
  def minCost(self, colors: str, neededTime: List[int]) -> int:
    # greedy

    n = len(colors)
    ret, i = 0, 0
    while i < n:
      t, m, c = 0, 0, i
      while c < n and colors[c] == colors[i]:
        t += neededTime[c]
        m = max(m, neededTime[c])
        c += 1
      ret += t - m
      i = c

    return ret

