class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    # 2-pass binary search with built-ins

    l, r = bisect_left(nums, target), bisect_right(nums, target)-1
    
    return [l, r] if l <= r else [-1, -1]

