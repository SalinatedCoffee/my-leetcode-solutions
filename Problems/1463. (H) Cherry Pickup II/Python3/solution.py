class Solution:
  def cherryPickup(self, grid: List[List[int]]) -> int:
    # top-down dynamic programming (tabulation)

    m, n = len(grid), len(grid[0])
    vectors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    @cache
    def recurse(row, l, r):
      # returns number of max cherries collected starting at row-th row
      # and left/right robots at l/r-th column
      if l < 0 or l >= n or r < 0 or r >= n or row >= m:
        return 0
      if l == r:
        cherries = grid[row][l]
      else:
        cherries = grid[row][l] + grid[row][r]
      
      return cherries + max([recurse(row+1, l+dl, r+dr) for dl, dr in vectors])

    return recurse(0, 0, n-1)

