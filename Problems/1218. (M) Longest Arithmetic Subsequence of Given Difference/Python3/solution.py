class Solution:
  def longestSubsequence(self, arr: List[int], difference: int) -> int:
    # bottom-up dynamic programming (tabulation) using a dicionary

    # dp[i] is length of longest arithmetic subsequence ending with value i
    dp = Counter()
    for i in arr:
      prev = i - difference
      if prev in dp:
        dp[i] = dp[prev] + 1
      else:
        dp[i] = 1

    return max(dp.values())
    
