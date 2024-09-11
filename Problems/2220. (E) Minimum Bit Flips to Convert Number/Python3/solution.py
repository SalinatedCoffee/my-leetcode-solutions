class Solution:
  def minBitFlips(self, start: int, goal: int) -> int:
    # bit manipulation

    diff = start ^ goal
    res = 0
    while diff:
      res += diff & 1
      diff >>= 1

    return res

