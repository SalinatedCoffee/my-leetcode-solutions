class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    # top-down dynamic programming (memoization)

    self.text1 = text1
    self.text2 = text2
    self.m, self.n = len(text1), len(text2)
    
    return self.recurse(0, 0)

  @cache
  def recurse(self, a, b):
    if a == self.m or b == self.n:
      return 0
    ret = []
    if self.text1[a] == self.text2[b]:
      ret.append(self.recurse(a+1, b+1) + 1)
    ret.append(self.recurse(a+1, b))
    ret.append(self.recurse(a, b+1))

    return max(ret)

