class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(s)
    dp = [0] * n
    prev_dp = [0] * n

    for i in range(n-1, -1, -1):
      dp[i] = 1
      for j in range(i+1, n):
        if s[i] == s[j]:
          dp[j] = prev_dp[j-1] + 2
        else:
          dp[j] = max(prev_dp[j], dp[j-1])
      prev_dp = dp[:]
    
    return dp[n-1]

