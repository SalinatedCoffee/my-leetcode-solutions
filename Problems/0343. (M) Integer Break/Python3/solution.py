class Solution:
  # top-down dynamic programming (memoization)

  def integerBreak(self, n: int) -> int:
    
    return self.recurse(n) if n > 3 else n - 1

  @cache
  def recurse(self, rem):
    # returns the largest product of splitting rem
    
    if rem <= 3:
      return rem
    ret = rem
    for i in range(2, rem+1):
      ret = max(ret, i * self.recurse(rem - i))
    
    return ret

