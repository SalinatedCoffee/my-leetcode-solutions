class Solution:
  def climbStairs(self, n: int) -> int:
    # math

    ret = 0
    for i in range(n // 2 + 1):
      ret += comb(n - i, i)

    return ret

