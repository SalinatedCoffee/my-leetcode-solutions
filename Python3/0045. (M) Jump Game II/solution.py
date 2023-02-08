class Solution:
  def jump(self, nums: List[int]) -> int:
    # naive solution

    # sanity check
    if len(nums) == 1:
      return 0

    # dp[i] is minimum number of jumps to reach i
    dp = [float('inf')] * len(nums)
    dp[0] = 0

    for i in range(len(nums)):
      # exit as soon as nums[n-1] can be reached
      if i+nums[i] >= len(nums)-1:
        return dp[i]+1
      # update min. jumps for all reachable indicies
      for j in range(1, nums[i]+1):
        dp[i+j] = dp[i]+1 if dp[i]+1 < dp[i+j] else dp[i+j]

    return dp[-1] if dp[-1] != float('inf') else 0

