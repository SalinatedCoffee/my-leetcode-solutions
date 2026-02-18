class Solution:
  def hasAlternatingBits(self, n: int) -> bool:
    # brute force with bitwise operations

    exp = n & 1
    while n:
      if exp != n & 1:
        return False
      exp ^= 1
      n >>= 1

    return True

