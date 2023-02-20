class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    # binary search

    lo, hi = 0, len(nums)-1
    while lo <= hi:
      mid = (hi-lo) // 2 + lo
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        lo = mid+1
      else:
        hi = mid-1
    
    # want the insertion index if target is missing
    return lo

