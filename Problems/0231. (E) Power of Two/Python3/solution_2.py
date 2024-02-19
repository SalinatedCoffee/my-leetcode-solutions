class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    # optimized bitwise operations

    return n > 0 and n & (n - 1) == 0

