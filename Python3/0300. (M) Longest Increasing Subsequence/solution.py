class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    # memoize subsequence length

    # dp[i] is length of longest subseq. in nums[0:i] ending at nums[i]
    dp = [1] * len(nums)

    for i in range(len(nums)):
      for j in range(i):
        # if subseq. is increasing and memoized number of subseq.
        # is larger than previous, update count
        if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
          dp[i] = dp[j] + 1
    
    return max(dp)

