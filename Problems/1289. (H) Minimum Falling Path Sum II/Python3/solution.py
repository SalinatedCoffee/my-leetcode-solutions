class Solution:
  def minFallingPathSum(self, grid: List[List[int]]) -> int:
    # top-down dynamic programming (memoization)

    n = len(grid)

    @cache
    def recurse(r, c):
      # return minimum FPS starting at grid[r][c]

      # base case
      if r == n - 1:
        return grid[r][c]

      ret = float('inf')
      for n_c in range(n):
        if n_c != c:
          ret = min(ret, recurse(r+1, n_c))
      
      return grid[r][c] + ret

    ret = float('inf')
    # pick smallest sum among all possible starting positions
    for c in range(n):
      ret = min(ret, recurse(0, c))
    
    return ret

