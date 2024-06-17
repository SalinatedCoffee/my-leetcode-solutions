class Solution:
  def judgeSquareSum(self, c: int) -> bool:
    # math

    for a in range(int(sqrt(c))+1):
      if sqrt(c - a**2) % 1 == 0:
        return True
      a += 1

    return False

