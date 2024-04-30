class Solution:
  def longestIdealString(self, s: str, k: int) -> int:
    # top-down dynamic programming (memoization)

    n = len(s)
    # preprocess s, converting it into list of 'indices' of the alphabet
    s_int = [ord(c) - ord('a') for c in s]

    # dp[i][j] returns length of LIS of s[:i]
    # where j-th letter in alphabet was last included
    self.dp = [[-1]*26 for _ in range(n)]
    def recurse(idx, c):
      # returns value of dp[idx][c]
      if self.dp[idx][c] != -1:
        return self.dp[idx][c]
      ret = 1 if c == s_int[idx] else 0
      if idx:
        ret = recurse(idx-1, c)
        if c == s_int[idx]:
          for p in range(26):
            if abs(c - p) <= k:
              ret = max(ret, recurse(idx-1, p) + 1)
      self.dp[idx][c] = ret

      return ret
    
    ans = 0
    # find longest length among all possible letters
    for c in range(26):
      ans = max(ans, recurse(n-1, c))

    return ans

