class Solution:
  def longestArithSeqLength(self, nums: List[int]) -> int:
    # dictionaries with optimized LIS
    # bottom-up dynamic programming (tabulation)

    n = len(nums)
    # dp[i][j] is length of LAS that ends in i-th number in increments of j
    dp = [{} for _ in range(n)]
    for r in range(n):
      for l in range(r):
        diff = nums[r] - nums[l]
        if diff not in dp[l]:
          dp[r][diff] = 2
        else:
          dp[r][diff] = dp[l][diff] + 1
    
    ret = 0
    for i in range(n):
      c_max = max(dp[i].values()) if dp[i] else 0
      ret = max(ret, c_max)

    return ret

