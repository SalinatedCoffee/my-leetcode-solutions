class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    # 2-pass binary search

    n = len(nums)
    # search for first position
    f = -1
    l, r = 0, n - 1
    while l <= r:
      m = l + (r - l) // 2
      if nums[m] >= target:
        f = m if nums[m] == target else f
        r = m - 1
      else:
        l = m + 1

    # search for last position
    s = -1
    l, r = 0, n - 1
    while l <= r:
      m = l + (r - l) // 2
      if nums[m] <= target:
        s = m if nums[m] == target else s
        l = m + 1
      else:
        r = m - 1
    
    return [-1, -1] if f > s else [f, s]

