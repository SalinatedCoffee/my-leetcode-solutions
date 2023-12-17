class Solution:
  def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
    # preprocess input

    m, n = len(grid), len(grid[0])
    # count number of 0s in each row and col
    row, col = [0]*m, [0]*n
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 0:
          row[i] -= 2
          col[j] -= 2
    
    # compute difference for each pos in grid
    ret = [[0]*n for _ in range(m)]
    for i in range(m):
      for j in range(n):
        ret[i][j] = m + n + row[i] + col[j]
    
    return ret

