class Solution:
  # top-down dynamic programming (memoization)

  @cache
  def kInversePairs(self, n: int, k: int) -> int:
    if k == 0:
      return 1
    if n == 1 or k < 0:
      return 0

    return (self.kInversePairs(n, k-1) + self.kInversePairs(n-1, k) - self.kInversePairs(n-1, k-n)) % (10**9+7)

