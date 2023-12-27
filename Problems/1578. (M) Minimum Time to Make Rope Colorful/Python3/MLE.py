class Solution:
  def minCost(self, colors: str, neededTime: List[int]) -> int:
    # top-down dynamic programming (memoization)
    n = len(colors)
    
    @cache
    def recurse(i, last):
      # return minimum time to make colors[i:] colorful,
      # where last balloon has color last
      if i >= n:
        return 0
      if colors[i] == last:
        return neededTime[i] + recurse(i+1, last)
      return min(neededTime[i] + recurse(i+1, last), recurse(i+1, colors[i]))
    
    return recurse(0, None)

