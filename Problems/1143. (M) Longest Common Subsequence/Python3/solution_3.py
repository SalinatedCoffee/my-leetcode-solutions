class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    # space optimized bottom-up dynamic programming (tabulation)
    
    m, n = len(text1), len(text2)
    # dp[i] is length of LCS between text1[i:] and text2[*:]
    dp = [0]*(n+1)
    dp_prev = [0]*(n+1)

    for i in range(m-1, -1, -1):
      for j in range(n-1, -1, -1):
        if text1[i] == text2[j]:
          dp[j] = dp_prev[j+1] + 1
        dp[j] = max(dp[j], dp[j+1], dp_prev[j])
      dp, dp_prev = dp_prev, dp
    
    return dp_prev[0]

