class Solution:
  def mySqrt(self, x: int) -> int:
    # 1 <= x <= 2**31-1, so we can just iterate
    rt = 1
    sq = 1
    while x >= sq:
      rt += 1
      sq = rt**2

    return rt-1

