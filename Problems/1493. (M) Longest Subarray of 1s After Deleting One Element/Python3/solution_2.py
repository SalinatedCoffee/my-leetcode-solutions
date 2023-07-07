class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    # sliding window

    n = len(nums)
    ret, zeros, l = 0, 0, 0
    for i in range(n):
      if not nums[i]:
        zeros += 1
      while zeros > 1:
        if not nums[l]:
          zeros -= 1
        l += 1
      ret = max(ret, i - l)
    
    return ret

