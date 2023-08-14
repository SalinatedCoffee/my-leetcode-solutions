class Solution:
  # top-down dynamic programming (memoization)

  def validPartition(self, nums: List[int]) -> bool:
    # dp[i] is partitionability of sublist nums[:i+1]
    dp = {-1: True, 0: False}

    return self.recurse(len(nums)-1, dp, nums)
  

  def recurse(self, i, dp, nums):
    if i in dp:
      return dp[i]
    partitionable = nums[i] == nums[i-1] and self.recurse(i-2, dp, nums)
    if i >= 2:
      if nums[i] == nums[i-1] == nums[i-2] or \
        nums[i] == nums[i-1]+1 == nums[i-2]+2:
        partitionable |= self.recurse(i-3, dp, nums)
    dp[i] = partitionable

    return dp[i]

