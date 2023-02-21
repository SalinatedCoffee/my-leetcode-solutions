class Solution:
  def singleNonDuplicate(self, nums: List[int]) -> int:
    # modified binary search

    lo, hi = 0, len(nums)-1
    while lo < hi:
      mid = (hi-lo) // 2
      # ensure left half has even length
      mid = mid if mid % 2 else mid+1
      mid += lo
      # if last item in left is same as first in right
      if nums[mid] == nums[mid+1]:
        # take left half
        hi = mid-1
      else:
        lo = mid+1
      
    return nums[lo]

