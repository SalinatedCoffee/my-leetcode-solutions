class Solution:
  def numberOfArrays(self, s: str, k: int) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(s)
    mod = 10**9 + 7
    # dp[i] is number of ways that s[:i] can be split into valid integers
    dp = [1] + [0] * n

    for i in range(n):
      if s[i] == '0':
        continue
      for j in range(i, n):
        if int(s[i:j+1]) > k:
          break
        dp[j+1] += dp[i]
        dp[j+1] %= mod
    
    return dp[-1]

