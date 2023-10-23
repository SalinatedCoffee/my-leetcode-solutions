class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    # divide by 4 in loops
    # if at any point remainder is not 0, not power of four

    if n < 0:
      return False
    if n in [0, 1]:
      return n != 0
    
    while n > 1:
      n, r = n // 4, n % 4
      if r != 0:
        return False

    return True

