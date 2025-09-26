class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    # space-optimized bottom-up dynamic programming (tabulation)

    n = len(triangle)

    # collapse VERTICALLY, instead of horizontally
    # dp[i] will be the min. sum of path from last row to i-th element in 'current' row
    dp = [float('inf')] * n
    
    return -1

