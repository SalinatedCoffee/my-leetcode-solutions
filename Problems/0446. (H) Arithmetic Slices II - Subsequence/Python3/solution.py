class Solution:
  def numberOfArithmeticSlices(self, nums: List[int]) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(nums)
    ret = 0
    # dp[i][j] is number of 'equidistant' subsequences with stride j
    # ending with nums[i]
    dp = [defaultdict(int) for _ in range(n)]

    for i in range(1, n):
      for j in range(i):
        stride = nums[i] - nums[j]
        dp[i][stride] += 1
        if stride in dp[j]:
          dp[i][stride] += dp[j][stride]
          ret += dp[j][stride]

    return ret

