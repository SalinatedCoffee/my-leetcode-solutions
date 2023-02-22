class Solution:
  def shipWithinDays(self, weights: List[int], days: int) -> int:
    # binary search on capacity

    # check whether packages can be shipped with capacity cap
    def valid(cap):
      cargo = 0
      day = 1
      for i in range(len(weights)):
        if cargo+weights[i] > cap:
          day += 1
          cargo = weights[i]
        else:
          cargo += weights[i]
      return day <= days

    # initial range of [max(weights), sum(weights)]
    lo = float('-inf')
    hi = 0
    for i in weights:
      hi += i
      lo = max(lo, i)
    
    # binary search
    prev_mid = 0
    while lo <= hi:
      mid = (hi-lo)//2+lo
      if valid(mid):
        prev_mid = mid
        hi = mid-1
      else:
        lo = mid+1
    
    return prev_mid

