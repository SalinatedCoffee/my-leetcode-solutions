class Solution:
  def longestPalindrome(self, s: str) -> str:
    # dynamic programming

    n = len(s)

    @cache
    def recurse(i, j):
      if i < 0 or j >= n:
        return None
      if s[i] != s[j]:
        return None
      ret = recurse(i-1, j+1)
      if ret is None:
        return (i, j)
      return ret

    ans = (0, 0)
    for i in range(1, n):
      rec = recurse(i,i)
      if rec is not None:
        ans = rec if rec[1] - rec[0] > ans[1] - ans[0] else ans
      rec = recurse(i-1,i)
      if rec is not None:
        ans = rec if rec[1] - rec[0] > ans[1] - ans[0] else ans

    return s[ans[0]:ans[1]+1]

