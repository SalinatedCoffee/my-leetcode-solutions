class Solution:
  def countServers(self, grid: List[List[int]]) -> int:
    # optimized brute force

    m, n = len(grid), len(grid[0])
    # determine number of servers on each row and column
    row_counts, col_counts = [0]*m, [0]*n
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          row_counts[i] += 1
          col_counts[j] += 1

    # count number of non-isolated servers
    res = 0
    for i in range(m):
      for j in range(n):
        if grid[i][j]:
          res += 1 if (row_counts[i] > 1 or col_counts[j] > 1) else 0

    return res

