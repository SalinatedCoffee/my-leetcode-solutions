class Solution:
  def minCost(self, colors: str, neededTime: List[int]) -> int:
    # top-down dynamic programming (memoization)
    n = len(colors)
    
    @cache
    def recurse(i):
      # return value of recurse(i) is minimum time to make colors[i:] colorful
      if i >= n:
        return 0
      ret = 0
      c, m = i, 0
      while c < n and colors[c] == colors[i]:
        ret += neededTime[c]
        m = max(m, neededTime[c])
        c += 1

      return ret - m + recurse(c)
    
    return recurse(0)

