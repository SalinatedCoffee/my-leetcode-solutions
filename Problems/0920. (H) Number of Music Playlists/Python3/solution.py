class Solution:
  # top-down dynamic programming (memoization)

  def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
    self.mod = 10**9 + 7
    # dp[i][j] is number of playlists that are i-long with j unique songs
    self.dp = [[-1] * (n+1) for _ in range(goal+1)]
    self.n, self.k = n, k
    return self.recurse(goal, n)
  
  def recurse(self, i, j):
    if self.dp[i][j] != -1:
      return self.dp[i][j]
    if not i and not j:
      return 1
    if not i or not j and i != j:
      return 0
    self.dp[i][j] = self.recurse(i-1, j-1) * (self.n-j+1)
    self.dp[i][j] += self.recurse(i-1, j) * (j-self.k) if j > self.k else 0
    self.dp[i][j] %= self.mod

    return self.dp[i][j]

