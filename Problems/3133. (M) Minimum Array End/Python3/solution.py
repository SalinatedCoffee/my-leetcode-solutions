class Solution:
  def minEnd(self, n: int, x: int) -> int:
    # bit manipulation
    
    n -= 1
    res = x
    mask = 1
    while n:
      # if current bit in x is unset
      if (x & mask) == 0:
        # raise current bit if corresponding bit of n is also raised
        res |= (n & 1) * mask
        n >>= 1
      mask <<= 1

    return res

