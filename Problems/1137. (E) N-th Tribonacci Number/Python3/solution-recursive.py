class Solution:
  @cache
  def tribonacci(self, n: int) -> int:
    # memoization with recursion

    # base case
    if n <= 2:
      return 0 if not n else 1

    return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)

