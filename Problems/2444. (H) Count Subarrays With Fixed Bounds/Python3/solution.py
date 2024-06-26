class Solution:
  def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
    # sliding window with multiple pointers

    ret = 0
    # indices of most recently seen min/max and out-of-bounds values
    min_idx = max_idx = l = -1

    for i in range(len(nums)):
      # number at index i is in range
      if minK <= nums[i] <= maxK:
        # min and max may be equal, so test for both
        if nums[i] == minK:
          min_idx = i
        if nums[i] == maxK:
          max_idx = i
      else:
        l = i
      ret += max(0, min(min_idx, max_idx) - l)
    
    return ret

