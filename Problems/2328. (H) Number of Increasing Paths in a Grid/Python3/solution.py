class Solution:
  def countPaths(self, grid: List[List[int]]) -> int:
    # traverse cells in ascending value order
    # sorting with bottom-up dynamic programming (tabulation)

    m = len(grid)
    n = len(grid[0])
    mod = 10**9 + 7
    dp = [[1] * n for _ in range(m)]

    cells = [(i, j) for i in range(m) for j in range(n)]
    cells.sort(key = lambda x: grid[x[0]][x[1]])

    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    for i, j in cells:
      for di, dj in moves:
        ni = i + di
        nj = j + dj
        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
          dp[ni][nj] += dp[i][j]
          dp[ni][nj] %= mod

    return sum(sum(row) % mod for row in dp) % mod

