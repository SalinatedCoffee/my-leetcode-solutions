class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    # 'raytracing'

    m, n = len(grid), len(grid[0])
    ret = 0
    # detect vertical edges
    for i in range(m):
      prev = 0
      for j in range(n):
        ret += 1 if prev != grid[i][j] else 0
        prev = grid[i][j]
      ret += prev
    
    # detect horizontal edges
    for j in range(n):
      prev = 0
      for i in range(m):
        ret += 1 if prev != grid[i][j] else 0
        prev = grid[i][j]
      ret += prev

    return ret

