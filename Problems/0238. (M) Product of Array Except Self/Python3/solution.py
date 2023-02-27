class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    # dynamic programming, precompute product in one direction

    # compute product of prefix in normal direction
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(dp)):
      dp[i] = nums[i] * dp[i-1]

    res = [0] * len(nums)
    # compute product of prefix in reverse direction while computing desired value
    rev_prod = 1
    for i in range(len(nums)-1, 0, -1):
      res[i] = dp[i-1] * rev_prod
      rev_prod *= nums[i]
    res[0] = rev_prod

    return res

