class Solution:
  def partition(self, s: str) -> List[List[str]]:
    # memoize whether substring is palindrome

    dp = [[False for _ in range(len(s))] for _ in range(len(s))]

    self.ret = []
    self.cur = []

    def recurse(start):
      # at end of string, current partition is valid
      if start >= len(s):
        self.ret.append(self.cur[:])
        return
      for i in range(start, len(s)):
        # first and last chars are equal
        if s[start] == s[i]:
          # check if inner substring is palindrome
          if i - start <= 2 or dp[start+1][i-1]:
            dp[start][i] = True
            self.cur.append(s[start:i+1])
            recurse(i+1)
            self.cur.pop()

    recurse(0)
      
    return self.ret

