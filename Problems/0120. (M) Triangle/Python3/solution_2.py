class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(triangle)

    # dp[r][c] is minimum sum of values in path between triangle[r][c] and triangle[-1](last row)
    dp = {i : [0]*(i+1) for i in range(n)}
    # initialize memoization table
    dp[n-1] = triangle[-1][:]

    # tabulate
    for i in range(n-2, -1, -1):
      for j in range(i+1):
        dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

    return dp[0][0]

