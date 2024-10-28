class Solution:
  def longestSquareStreak(self, nums: List[int]) -> int:
    # brute force using set
    
    n = len(nums)
    nums_set = set(nums)
    res = 0
    for num in nums:
      l = 0
      cur = num
      while cur in nums_set:
        l += 1
        cur *= cur
      res = max(res, l)

    return res if res > 1 else -1

