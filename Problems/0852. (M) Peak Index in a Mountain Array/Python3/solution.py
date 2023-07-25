class Solution:
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
    # binary search

    l, h = 0, len(arr)-1
    while l <= h:
      m = (l + h) // 2
      if arr[m-1] < arr[m] > arr[m+1]:
        return m
      elif arr[m] > arr[m-1]:
        l = m
      else:
        h = m 
    
    return l

