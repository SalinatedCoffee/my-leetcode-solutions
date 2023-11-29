class Solution:
  def hammingWeight(self, n: int) -> int:
    # bit manipulation
    
    ret = 0
    while n:
      ret += n & 1
      n >>= 1
    
    return ret

