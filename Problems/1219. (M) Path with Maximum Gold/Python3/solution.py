class Solution:
  def getMaximumGold(self, grid: List[List[int]]) -> int:
    # backtracking with DFS

    m, n = len(grid), len(grid[0])
    VEC = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    def recurse(i, j):
      # starting at grid[i][j] return maximum attainable amount of gold

      temp, grid[i][j] = grid[i][j], 0
      ret = 0
      for dy, dx in VEC:
        ny, nx = i + dy, j + dx
        if 0 <= ny < m and 0 <= nx < n and grid[ny][nx]:
          ret = max(ret, recurse(ny, nx))
      grid[i][j] = temp

      return ret + grid[i][j]
    
    # try backtracking at each and every cell with gold
    ret = 0
    for i in range(m):
      for j in range(n):
        if grid[i][j]:
          ret = max(ret, recurse(i, j))
      
    return ret

