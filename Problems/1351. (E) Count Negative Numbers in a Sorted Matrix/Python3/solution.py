class Solution:
  def countNegatives(self, grid: List[List[int]]) -> int:
    # simple iteration
    
    m = len(grid)
    n = len(grid[0])
    c = n-1
    ret = 0
    for i in range(m):
      while c >= 0:
        if grid[i][c] < 0:
          c -= 1
          continue
        else:
          break
      ret += n-1 - c if c != -1 else n

    return ret

