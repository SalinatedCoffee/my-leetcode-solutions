class Solution:
  def stoneGameII(self, piles: List[int]) -> int:
    # top-down dynamic programming (memoization)

    n = len(piles)
    # dp[i][j][k] is max number of stones for game with parameters:
    #   starts with player i (0 == Alice, 1 == Bob)
    #   uses piles[j:] set of piles
    #   M = k
    dp = [[[-1]*(n+1) for i in range(n+1)] for p in range(0, 2)]

    def recurse(p, i, m):
      if i == n:
        return 0
      if dp[p][i][m] != -1:
        return dp[p][i][m]
      ret = float('inf') if p else -1
      s = 0
      for j in range(1, min(2*m, n-i)+1):
        s += piles[i+j-1]
        if p:
          ret = min(ret, recurse(0, i+j, max(m, j)))
        else:
          ret = max(ret, s+recurse(1, i+j, max(m, j)))
      dp[p][i][m] = ret
      return ret
    
    return recurse(0, 0, 1)

