class Solution:
  def minInsertions(self, s: str) -> int:
    # top-down dynamic programming (memoization)

    n = len(s)
    # dp[i][j] is the length of the LCSs between s[:i+1] and s_rev[:j+1]
    dp = [[-1] * (n+1) for _ in range(n+1)]
    s_rev = s[::-1]

    def recurse(s1, s2, l1, l2):
      if not l1 or not l2:
        return 0
      if dp[l1][l2] != -1:
        return dp[l1][l2]
      if s1[l1-1] == s2[l2-1]:
        dp[l1][l2] = 1 + recurse(s1, s2, l1-1, l2-1)
      else:
        dp[l1][l2] = max(recurse(s1, s2, l1-1, l2), recurse(s1, s2, l1, l2-1))
      return dp[l1][l2]
    
    return n - recurse(s, s_rev, n, n)
    
