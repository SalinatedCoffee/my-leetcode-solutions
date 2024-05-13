class Solution:
  def matrixScore(self, grid: List[List[int]]) -> int:
    # greedy

    m, n = len(grid), len(grid[0])
    # scanning row by row, flip bits if MSB is 0
    for i in range(m):
      if grid[i][0] == 0:
        for j in range(n):
          grid[i][j] += 1
          grid[i][j] %= 2
    # scanning col by col, flip bits if there are more 0s than 1s
    for j in range(1, n):
      if sum([grid[i][j] for i in range(m)]) <= m // 2:
        for i in range(m):
          grid[i][j] += 1
          grid[i][j] %= 2
    
    # convert row into integer, get sum of rows
    ret = 0
    for row in grid:
      # convert values to string because I'm lazy
      ret += int(''.join(list(map(str, row))), 2)

    return ret

