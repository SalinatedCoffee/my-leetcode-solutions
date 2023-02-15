class Solution:
  def maxSubarraySumCircular(self, nums: List[int]) -> int:
    # either array wraps around end or it does not
    # compute max of 'normal' and wraparound subarray
    # return whichever is larger

    # compute rhs max sums
    dp = [0] * len(nums)
    dp[-1] = nums[-1]
    current_sum = nums[-1]
    for i in range(len(nums)-2, -1, -1):
      current_sum += nums[i]
      dp[i] = max(dp[i+1], current_sum)

    # max sum of 'normal' subarrays
    normal_max = float('-inf')
    # max sum of wraparound subarrays
    wrap_max = float('-inf')
    # max sum of lhs subarray
    interval_max = float('-inf')
    current_sum = 0
    current_max = 0
    for i in range(len(nums)-1):
      current_sum += nums[i]
      current_max = max(nums[i], current_max+nums[i])
      normal_max = max(normal_max, current_max)
      interval_max = max(interval_max, current_sum)
      wrap_max = max(wrap_max, interval_max+dp[i+1])
    # compute last index
    current_max = max(nums[-1], current_max+nums[-1])
    normal_max = max(normal_max, current_max)

    return max(normal_max, wrap_max)

