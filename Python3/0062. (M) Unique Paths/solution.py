import math
class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    # direct computation
    # path length is m-1 + n-1
    # from that path we need to choose when to move right (or wlog, down)
    # compute nCr where n = m+n-2 and r = m-1 (or n-1)
    return math.factorial(m+n-2) // math.factorial(m-1) // math.factorial(n-1)

