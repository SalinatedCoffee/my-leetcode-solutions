class Solution:
  def combinationSum4(self, nums: List[int], target: int) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(nums)
    dp = [0] * (target+1)
    for num in nums:
      if num <= target:
        dp[num] = 1

    for i in range(1, target+1):
      for num in nums:
        dp[i] += dp[i-num] if i-num >= 0 else 0
    
    return dp[-1]

