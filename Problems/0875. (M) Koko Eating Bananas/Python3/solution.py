class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # binary search on eating rate

    lo, hi = 1, max(piles)
    prev = 0
    while(lo <= hi):
      mid = (lo + hi) // 2
      mid_hours = 0
      for pile in piles:
        mid_hours += math.ceil(pile / mid)
      if mid_hours > h:
        lo = mid + 1
      else:
        prev = mid
        hi = mid - 1
    
    return prev

