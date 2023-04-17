class Solution:
  def numWays(self, words: List[str], target: str) -> int:
    # bottom-up dynamic programming (tabulation)

    alphabet = 26
    mod = 10**9 + 7
    n = len(target)
    m = len(words[0])
    # letter frequency of each column of words
    cnt = [[0] * m for _ in range(alphabet)]
    for j in range(m):
      for word in words:
        cnt[ord(word[j])-ord('a')][j] += 1
    
    # dp[i][j] contains number of ways to construct target[:i]
    # with j left-most columns, given words
    dp = [[0] * (m+1) for _ in range(n+1)]
    # only one way to construct empty string with no columns
    dp[0][0] = 1
    for i in range(n+1):
      for j in range(m):
        if i < n:
          dp[i+1][j+1] += (cnt[ord(target[i])-ord('a')][j]*dp[i][j])
          dp[i+1][j+1] %= mod
        dp[i][j+1] += dp[i][j]
        dp[i][j+1] %= mod
    
    return dp[n][m]

