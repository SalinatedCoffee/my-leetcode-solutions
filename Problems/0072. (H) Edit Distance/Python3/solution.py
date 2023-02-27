class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    # bottom-up dynamic programming

    m, n = len(word1), len(word2)
    # dp[i][j] stores the minimum edit distance between
    # word1[:j+1] and word2[:i+1]
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    # initialize cases where either string is empty
    for i in range(n+1):
      dp[i][0] = i
    for j in range(m+1):
      dp[0][j] = j

    # fill dp towards bottom right
    for i in range(1, n+1):
      for j in range(1, m+1):
        if word1[j-1] == word2[i-1]:
          cur_dp = dp[i-1][j-1]
        else:
          cur_dp = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        dp[i][j] = cur_dp

    # return desired value
    return dp[-1][-1]

