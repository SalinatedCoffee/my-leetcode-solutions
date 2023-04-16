class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    # top-down dynamic programming (memoization)

    n = len(s)
    dp = [[0] * n for _ in range(n)]

    def recurse(i, j):
      if dp[i][j]:
        return dp[i][j]
      if i > j:
        return 0
      if i == j:
        return 1
      if s[i] == s[j]:
        dp[i][j] = recurse(i+1, j-1) + 2
      else:
        dp[i][j] = max(recurse(i+1, j), recurse(i, j-1))
      return dp[i][j]
    
    return recurse(0, n-1)

