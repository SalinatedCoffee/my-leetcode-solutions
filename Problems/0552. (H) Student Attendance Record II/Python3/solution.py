class Solution:
  def checkRecord(self, n: int) -> int:
    # top-down dynamic programming (memoization)

    MOD = 10**9 + 7

    dp = [[[-1]*3 for _ in range(2)] for _ in range(n+1)]

    def recurse(d, a, l):
      # return number of possible attendance records for d days where
      # there are a total absence days
      # and l consecutive late days currently
      if a >= 2 or l >= 3:
        return 0
      if d == 0:
        return 1
      if dp[d][a][l] != -1:
        return dp[d][a][l]
      dp[d][a][l] = recurse(d-1, a, 0)
      dp[d][a][l] += recurse(d-1, a+1, 0)
      dp[d][a][l] %= MOD
      dp[d][a][l] += recurse(d-1, a, l+1)
      dp[d][a][l] %= MOD

      return dp[d][a][l]

    return recurse(n, 0, 0)

