class Solution:
  def gridGame(self, grid: List[List[int]]) -> int:
    # pre / suffix sums

    n = len(grid[0])
    r0, r1 = sum(grid[0]), 0
    res = float("inf")
    for i in range(n):
      r0 -= grid[0][i]
      res = min(res, max(r0, r1))
      r1 += grid[1][i]

    return res

