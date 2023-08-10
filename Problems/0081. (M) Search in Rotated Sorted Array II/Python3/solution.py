class Solution:
  def search(self, nums: List[int], target: int) -> bool:
    # binary search

    l, h = 0, len(nums)-1
    while l <= h:
      m = l + (h - l) // 2
      if nums[m] == target:
        return True
      if nums[l] <= nums[m]:
        if nums[l] <= target < nums[m]:
          h -= 1
        else:
          l += 1
      else:
        if nums[m] < target <= nums[h]:
          l += 1
        else:
          h -= 1
    
    return False

