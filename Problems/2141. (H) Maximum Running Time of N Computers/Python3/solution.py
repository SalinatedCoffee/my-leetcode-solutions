class Solution:
  def maxRunTime(self, n: int, batteries: List[int]) -> int:
    # binary search

    ret = 0
    l, h = 1, sum(batteries) // n
    while l <= h:
      m = (l + h) // 2
      if sum([min(x, m) for x in batteries]) >= n * m:
        ret = m
        l = m + 1
      else:
        h = m - 1
    
    return ret

