class Solution:
  def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    # top-down dynamic programming (memoization)

    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    @cache
    def recurse(i, j, moves):
      # return maximum number of ways to go OOB starting at (i, j) using moves moves
      if i < 0 or i >= m or j < 0 or j >= n:
        return 1
      if moves == 0:
        return 0

      return sum([recurse(i+dy, j+dx, moves-1) for dy, dx in vectors])

    return recurse(startRow, startColumn, maxMove) % (10**9 + 7)

