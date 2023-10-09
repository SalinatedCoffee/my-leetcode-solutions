class Solution:
  # top-down dynamic programming (memoization)

  def numOfArrays(self, n: int, m: int, k: int) -> int:
    self.n = n
    self.m = m
    self.mod = 10**9+7

    return self.recurse(0, 0, k)

  @cache
  def recurse(self, i, mx, r):
    # return number of valid arrays where mx is the maximum value in arr[i:]
    # with r remaining comparisons

    if i == self.n:
      return 1 if r == 0 else 0
    if r < 0:
      return 0
    ret = mx * self.recurse(i+1, mx, r)
    for n_mx in range(mx+1, self.m+1):
      ret += self.recurse(i+1, n_mx, r-1)
    
    return ret % self.mod

