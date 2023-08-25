class Solution:
  # top-down dynamic programming (memoization)

  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    self.n = len(s3)
    self.a, self.b = len(s1), len(s2)
    # sanity check
    if self.a + self.b != self.n:
      return False
    # dp[i][j] is interleavability of s3[i+j:] with s1[i:] and s2[j:] remaining
    dp = [[None]*(self.b+1) for _ in range(self.a+1)]
    dp[-1][-1] = True

    return self.recurse(0, 0, s1, s2, s3, dp)
  
  def recurse(self, i, j, s1, s2, s3, dp):
    # return interleavability of s3[i+j:] given s1[i:] and s2[j:]

    if dp[i][j] is not None:
      return dp[i][j]
    # base cases
    if i == self.a:
      if s2[j] == s3[i+j]:
        dp[i][j] = self.recurse(i, j+1, s1, s2, s3, dp)
      else:
        dp[i][j] = False
      return dp[i][j]
    if j == self.b:
      if s1[i] == s3[i+j]:
        dp[i][j] = self.recurse(i+1, j, s1, s2, s3, dp)
      else:
        dp[i][j] = False
      return dp[i][j]

    interleavable = False
    if s1[i] == s3[i+j]:
      interleavable |= self.recurse(i+1, j, s1, s2, s3, dp)
    if s2[j] == s3[i+j]:
      interleavable |= self.recurse(i, j+1, s1, s2, s3, dp)
    dp[i][j] = interleavable

    return interleavable

