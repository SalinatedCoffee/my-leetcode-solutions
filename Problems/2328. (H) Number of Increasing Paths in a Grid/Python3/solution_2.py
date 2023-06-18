class Solution:
  def countPaths(self, grid: List[List[int]]) -> int:
    # top-down dynamic programming (memoization)
    
    m = len(grid)
    n = len(grid[0])
    mod = 10**9 + 7
    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    dp = [[0] * n for _ in range(m)]

    def recurse(i, j):
      if dp[i][j]:
        return dp[i][j]
      total = 1
      for di, dj in moves:
        ni = i + di
        nj = j + dj
        if 0 <= ni < m and 0 <= nj < n and grid[i][j] > grid[ni][nj]:
          total += recurse(ni, nj) % mod
      dp[i][j] = total
      return total
    
    ret = 0
    for i in range(m):
      for j in range(n):
        ret += recurse(i, j)
        ret %= mod

    return ret

