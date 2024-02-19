class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    # bitwise operations

    if n <= 0:
      return False

    while True:
      if n & 1:
        return n >> 1 == 0
      n >>= 1

    # this line will never run
    return False

