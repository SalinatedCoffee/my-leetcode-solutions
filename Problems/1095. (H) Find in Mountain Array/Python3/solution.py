class Solution:
  def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
    # 3-pass binary search

    n = mountain_arr.length()
    peak = -1
    l, h = 0, n-1
    # find peak
    while l <= h:
      m = l + (h - l) // 2
      print(m)
      m0, m1, m2 = mountain_arr.get(m-1), mountain_arr.get(m), mountain_arr.get(m+1)
      if m0 < m1 > m2:
        peak = m
        break
      if m0 > m1:
        h = m
      else:
        l = m
    if m1 == target:
      return peak

    l, h = 0, peak
    # search left of peak
    while l <= h:
      m = l + (h - l) // 2
      m1 = mountain_arr.get(m)
      if m1 == target:
        return m
      elif m1 < target:
        l = m + 1
      else:
        h = m - 1

    l, h = peak, n-1
    # search right of peak
    while l <= h:
      m = l + (h - l) // 2
      m1 = mountain_arr.get(m)
      if m1 == target:
        return m
      elif m1 < target:
        h = m - 1
      else:
        l = m + 1
    
    # target does not exist
    return -1

