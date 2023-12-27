class Solution:
  def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    # top-down dynamic programming (memoization)

    mod = 10**9 + 7

    @cache
    def recurse(rolls, rem):
      # return value of recurse(rolls, rem) is number of ways to roll
      # rem with rolls rolls of k-sided dice
      if rolls == 0 and rem == 0:
        return 1
      if rolls == 0 or rem <= 0:
        return 0
      
      ret = 0
      for r in range(1, k+1):
        ret += recurse(rolls-1, rem-r)
      
      return ret % mod

    return recurse(n, target)

