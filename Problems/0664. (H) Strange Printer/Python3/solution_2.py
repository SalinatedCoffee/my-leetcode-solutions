class Solution:
  def strangePrinter(self, s: str) -> int:
    # top-down dynamic programming (memoization)

    n = len(s)
    # preprocess string by leaving 1 letter of each consecutive section
    # ex. aaabbb -> ab, abcccddfe -> abcdfe
    trunc_s = s[0]
    for i in range(1, n):
      if s[i] != s[i-1]:
        trunc_s += s[i]
    
    m = len(trunc_s)

    @cache
    # return number of steps required to type trunc_s[l:r+1]
    def recurse(l, r):
      if l > r:
        return 0
      ret = 1 + recurse(l+1, r)
      for i in range(l+1, r+1):
        if trunc_s[i] == trunc_s[l]:
          ret = min(ret, recurse(l, i-1) + recurse(i+1, r))

      return ret

    return recurse(0, m-1)

