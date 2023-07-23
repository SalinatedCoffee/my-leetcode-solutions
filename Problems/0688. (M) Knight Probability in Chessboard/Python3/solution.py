class Solution:
  # top-down dynamic programming (memoization)

  def recurse(self, r, c, s, k, n):
      if r < 0 or n <= r or c < 0 or n <= c:
        return 0
      if s == k:
        return 1
      if self.dp[r][c][s] != -1:
        return self.dp[r][c][s]
      ret = 0
      for dy, dx in self.vectors:
        ret += self.recurse(r+dy, c+dx, s+1, k, n) * 0.125
      self.dp[r][c][s] = ret

      return ret


  def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    self.vectors = [(1,2), (1,-2), (2,1), (-2,1), (-1,2), (-1,-2), (2,-1), (-2,-1)]
    self.dp = [[[-1] * k for _ in range(n)] for _ in range(n)]

    return self.recurse(row, column, 0, k, n)

