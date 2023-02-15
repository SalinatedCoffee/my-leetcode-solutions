class Solution:
  def countOdds(self, low: int, high: int) -> int:
    ret = (high - low) // 2

    # only add 1 if either bound is odd
    if low % 2 or high % 2:
      ret += 1

    return ret

