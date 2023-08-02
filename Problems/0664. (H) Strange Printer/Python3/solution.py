class Solution:
  # top-down dynamic programming (memoization)

  def strangePrinter(self, s: str) -> int:
    self.n = len(s)
    self.s = s
    # dp[i][j] is return value of self.recurse(i, j)
    self.dp = [[-1] * self.n for _ in range(self.n)]

    return self.recurse(0, self.n-1) + 1
  

  def recurse(self, l, r):
    # for some string t where t = s[r] * (r-l+1), returns the minimum number of
    # operations it takes to convert t into s[l:r+1]

    if self.dp[l][r] != -1:
      return self.dp[l][r]

    # set number of operations for current state as theoretical maximum
    self.dp[l][r] = self.n
    j = -1
    for i in range(l, r):
      # if current char is not s[r] remember index
      if self.s[i] != self.s[r] and j == -1:
        j = i
      # if mismatching char found recurse on substring s[j:r+1]
      if j != -1:
        self.dp[l][r] = min(self.dp[l][r], 1 + self.recurse(j,i) + self.recurse(i+1,r))

    # t was identical to s[r] * (r-l+1)
    if j == -1:
      self.dp[l][r] = 0

    return self.dp[l][r]

