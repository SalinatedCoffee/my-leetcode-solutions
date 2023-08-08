class Solution:
  def search(self, nums: List[int], target: int) -> int:
    # binary search

    # first pass, find index of pivot
    n = len(nums)
    l, h = 0, n - 1
    while l <= h:
      m = l + (h - l) // 2
      if nums[m] > nums[-1]:
        l = m + 1
      else:
        h = m - 1
    pivot = l

    # second pass, find target given pivot
    shift = n - pivot
    l, h = 0, n - 1
    while l <= h:
      m = l + (h - l) // 2
      if nums[(m - shift + n) % n] == target:
        return (m - shift) % n
      elif nums[(m - shift + n) % n] > target:
        h = m - 1
      else:
        l = m + 1
    
    return -1

