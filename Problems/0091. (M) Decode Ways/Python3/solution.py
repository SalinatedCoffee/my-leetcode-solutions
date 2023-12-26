class Solution:
  def numDecodings(self, s: str) -> int:
    # top-down dynamic programming (memoization)

    n = len(s)

    @cache
    # return value of recurse(i) is number of ways that s[i:] can be decoded
    def recurse(i):
      if i >= n:
        return 1
      if s[i] == '0':
        return 0
      ret = 0
      if n - i >= 2:
        ret += recurse(i+1)
      if int(s[i:i+2]) <= 26:
        ret += recurse(i+2)

      return ret

    return recurse(0)

