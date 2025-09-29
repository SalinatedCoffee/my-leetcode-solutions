class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    # space-optimized bottom-up dynamic programming (tabulation)

    n = len(triangle)

    # dp1[i] will be the min. sum of path from last row to i-th element in 'current' row
    dp1 = triangle[-1][:]
    # dp2[i] will be the same, but for the i+1-th row instead
    dp2 = [0] * n
    for i in range(n-2, -1, -1):
      for j in range(i+1):
        dp2[j] = min(dp1[j], dp1[j+1]) + triangle[i][j]
      dp1, dp2 = dp2, dp1
    
    return dp1[0]

