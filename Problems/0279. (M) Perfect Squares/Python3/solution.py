class Solution:
  @cache
  def numSquares(self, n: int) -> int:
    # top-down dynamic programming (memoization)
    if n == 0:
      return 0
    rt = 1
    ret = float('inf')
    while rt**2 <= n:
      ret = min(ret, self.numSquares(n - rt**2))
      rt += 1

    return ret + 1

