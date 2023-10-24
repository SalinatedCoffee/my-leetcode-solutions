class Solution:
  def numWays(self, steps: int, arrLen: int) -> int:
    # top-down dynamic programming (memoization)

    mod = 10**9 + 7
    
    @cache
    # recurse(p, s) returns number of possible ways to return to 0
    #   from position p using s steps
    def recurse(p, s):
      # base cases
      if p < 0 or p >= arrLen:
        return 0
      if s == 0:
        return 1 if p == 0 else 0
      
      ret = recurse(p-1, s-1) + recurse(p, s-1) + recurse(p+1, s-1)

      return ret % mod

    return recurse(0, steps)
  
