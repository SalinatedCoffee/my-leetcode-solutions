class Solution:
  def maxDistance(self, grid: List[List[int]]) -> int:
    # dp, need to traverse twice to cover all directions

    # length of one side and max possible manhattan distance
    n = len(grid)
    max_dist = n*2+1
    
    # value of dp[i][j] is distance from nearest land to square at (i, j)
    dp = [[max_dist for _ in range(n)] for _ in range(n)]

    # filling dp towards bottom-right
    for i in range(n):
      for j in range(n):
        # at land square, distance is 0
        if grid[i][j]:
          dp[i][j] = 0
        # choose min among current and previously filled dp
        else:
          up = dp[i-1][j]+1 if i else max_dist
          left = dp[i][j-1]+1 if j else max_dist
          dp[i][j] = min(dp[i][j], up, left)
    
    res = float('-inf')
    # filling dp towards top-left
    for i in range(n-1, -1, -1):
      for j in range(n-1, -1, -1):
        # choose min among current and previously filled dp
        down = dp[i+1][j]+1 if i < n-1 else max_dist
        right = dp[i][j+1]+1 if j < n-1 else max_dist
        dp[i][j] = min(dp[i][j], down, right)
        # update max accordingly
        res = max(res, dp[i][j])
    
    # max dist is 0 if all land or max manhattan dist of all water
    return -1 if not res or res == max_dist else res

