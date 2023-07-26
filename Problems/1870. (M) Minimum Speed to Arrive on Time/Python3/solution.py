class Solution:
  def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
    # binary search

    # sanity check
    if ceil(hour) < len(dist):
      return -1

    ret = -1

    # use entire range of answers as intial search space
    l, h = 1, 10**7
    while l <= h:
      m = (l + h) // 2
      if sum([ceil(x/m) for x in dist[:-1]]) + dist[-1]/m <= hour:
        ret = m
        h = m - 1
      else:
        l = m + 1
    
    return ret

