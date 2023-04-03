class Solution:
  def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    # sort, then binary search

    potions.sort()
    ret = []
    for s in spells:
      lo, hi = 0, len(potions)-1
      mid = -1
      while lo <= hi:
        mid = (lo + hi) // 2
        if potions[mid] * s < success:
          lo = mid + 1
        else:
          hi = mid - 1
      if mid != -1:
        ret.append(len(potions) - lo)
    
    return ret

