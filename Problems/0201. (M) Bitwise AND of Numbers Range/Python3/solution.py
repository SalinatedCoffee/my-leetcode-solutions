class Solution:
  def rangeBitwiseAnd(self, left: int, right: int) -> int:
    # bit manipulation
    
    n = 0
    while left != right:
      right >>= 1
      left >>= 1
      n += 1

    return left << n

