class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    # bottom-up dynamic programming (tabulation)

    m, n = len(text1), len(text2)
    # dp[i][j] is length of LCS between text1[i:] and text2[j:]
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m-1, -1, -1):
      for j in range(n-1, -1, -1):
        if text1[i] == text2[j]:
          dp[i][j] = dp[i+1][j+1] + 1
        dp[i][j] = max(dp[i][j], dp[i][j+1], dp[i+1][j])
    
    return dp[0][0]

