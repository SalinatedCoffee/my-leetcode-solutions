class Solution:
  # top-down dynamic programming (memoization)

  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    self.n = len(s3)
    self.a, self.b = len(s1), len(s2)
    # sanity check
    if self.a + self.b != self.n:
      return False
    # dp[i][j][k] is interleavability of s3[k:] with s1[i:] and s2[j:] remaining
    dp = [[[None]*(self.n+1) for _ in range(self.b+1)] for _ in range(self.a+1)]
    dp[-1][-1][-1] = True

    return self.recurse(0, 0, 0, s1, s2, s3, dp)
  
  def recurse(self, i, j, k, s1, s2, s3, dp):
    # return interleavability of s3[k:] given s1[i:] and s2[j:]

    if dp[i][j][k]:
      return dp[i][j][k]

    # base cases
    if i == self.a:
      if s2[j] == s3[k]:
        dp[i][j][k] = self.recurse(i, j+1, k+1, s1, s2, s3, dp)
      else:
        dp[i][j][k] = False
      return dp[i][j][k]
    if j == self.b:
      if s1[i] == s3[k]:
        dp[i][j][k] = self.recurse(i+1, j, k+1, s1, s2, s3, dp)
      else:
        dp[i][j][k] = False
      return dp[i][j][k]

    interleavable = False
    if s1[i] == s3[k]:
      interleavable |= self.recurse(i+1, j, k+1, s1, s2, s3, dp)
    if s2[j] == s3[k]:
      interleavable |= self.recurse(i, j+1, k+1, s1, s2, s3, dp)
    dp[i][j][k] = interleavable

    return interleavable

