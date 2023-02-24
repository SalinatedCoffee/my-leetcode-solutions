class Solution:
  def rob(self, nums: List[int]) -> int:
    # dynamic programming

    # sanity check
    if not nums:
      return 0
    
    # dp[i] = maximum stolen up to nums[i-1]
    dp = [0] * (len(nums)+1)
    dp[1] = nums[0]

    for i in range(1, len(nums)):
      # either steal from current or skip
      dp[i+1] = max(dp[i-1]+nums[i], dp[i])
    
    return dp[-1]

