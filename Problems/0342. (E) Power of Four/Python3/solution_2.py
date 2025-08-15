class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    # bit manipulation

    while n > 1:
      if n & 3 != 0:
        return False
      n >>= 2

    return False if n != 1 else True

