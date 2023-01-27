class Solution:
  def mySqrt(self, x: int) -> int:
    # Newton's method
    r = x
    if not x:
      return 0
    for i in range(20):
      r = (r+x/r) / 2
    
    return int(r // 1)

