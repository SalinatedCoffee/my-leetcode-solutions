class Solution:
  def myPow(self, x: float, n: int) -> float:
    # binary exponentiation(/search)
    
    # sanity check
    if not n:
      return 1
    
    # use reciprocal of x if exponent is negative
    if n < 0:
      x = 1 / x
      n = -n
      
    ret = 1
    while n:
      if n % 2:
        ret *= x
        n -= 1
      x *= x
      n //= 2
    
    return ret

