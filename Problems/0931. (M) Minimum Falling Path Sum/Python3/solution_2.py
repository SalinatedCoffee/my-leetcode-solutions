class Solution:
  def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    dp[-1] = matrix[-1]

    for i in range(n-2, -1, -1):
      dp[i][0] = matrix[i][0] + min(dp[i+1][0], dp[i+1][1])
      for j in range(1, n-1):
        dp[i][j] = matrix[i][j] + min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
      dp[i][-1] = matrix[i][-1] + min(dp[i+1][-2], dp[i+1][-1])

    return min(dp[0])

