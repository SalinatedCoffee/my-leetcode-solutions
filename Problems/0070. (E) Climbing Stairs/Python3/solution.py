class Solution:
  def climbStairs(self, n: int) -> int:
    # top-down dynamic programming (memoization)

    @cache
    def recurse(r):
      # returns number of ways to climb r stairs
      if r == 0:
        return 1
      if r < 0:
        return 0
      
      return recurse(r-1) + recurse(r-2)

    return recurse(n)

