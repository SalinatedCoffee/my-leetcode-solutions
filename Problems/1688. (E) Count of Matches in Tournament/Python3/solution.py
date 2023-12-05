class Solution:
  def numberOfMatches(self, n: int) -> int:
    # simulation
    
    ret = 0
    while n > 1:
      c = n % 2
      n //= 2
      ret += n
      n += c
    
    return ret

