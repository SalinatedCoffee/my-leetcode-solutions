class Solution:
  def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    # binary search
    
    n = len(bloomDay)
    # sanity check
    if k*m > n:
      return -1

    ret = -1
    # set initial search space for binary search on number of days to wait
    lo, hi = 1, max(bloomDay)
    while lo <= hi:
      mid = lo + (hi - lo) // 2
      # validate midpoint
      valid = False
      run, bouquets = 0, 0
      for day in bloomDay:
        if day <= mid:
          run += 1
        else:
          if run:
            bouquets += run // k
          if bouquets >= m:
            valid = True
            break
          run = 0
      valid = True if run // k + bouquets >= m else False
      # discard half of search space according to validity of midpoint
      if valid:
        ret = mid
        hi = mid - 1
      else:
        lo = mid + 1

    return ret

