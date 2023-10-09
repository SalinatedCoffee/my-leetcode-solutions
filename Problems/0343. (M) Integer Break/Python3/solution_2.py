class Solution:
  def integerBreak(self, n: int) -> int:
    # math
    
    if n < 3:
      return 1
    if n == 3:
      return 2

    a = n // 3
    b = n % 3
    if b == 0:
      return 3**a
    if b == 1:
      return 4*3**(a-1)
    return 2*3**a

