class Solution:
  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    # sliding window

    n = len(nums)
    ret = 0
    # sum of window, starting position of window, number of zeros in window prefix
    w_sum, l, zeros = 0, 0, 0
    for i in range(n):
      w_sum += nums[i]
      while l < i and (nums[l] == 0 or w_sum > goal):
        # count number of leading zeros
        if nums[l] == 1:
          zeros = 0
        else:
          zeros += 1
        w_sum -= nums[l]
        l += 1
      if w_sum == goal:
        ret += 1 + zeros
    
    return ret

