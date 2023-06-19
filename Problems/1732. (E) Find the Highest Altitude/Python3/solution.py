class Solution:
  def largestAltitude(self, gain: List[int]) -> int:
    # prefix sums

    ret = 0
    alt = 0
    for d in gain:
      alt += d
      ret = max(ret, alt)
    
    return ret

