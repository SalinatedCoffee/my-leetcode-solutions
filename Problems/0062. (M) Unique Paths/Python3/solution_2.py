class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    # DP solution
    # number of paths to a certain square depends on numbers of previous squares
    # move towards goal (bottom-right)

    # initialize grid
    grid = [[1 for _ in range(n+1)] for _ in range(m+1)]

    # iterate row-first
    for i in range(1, m):
      for j in range(1, n):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

    # return value at goal
    return grid[m-1][n-1]

