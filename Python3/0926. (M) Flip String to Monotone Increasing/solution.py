class Solution:
  def minFlipsMonoIncr(self, s: str) -> int:
    # if a string is monotonically increasing
    # its prefixes are also monotonically increasing, by induction
    # compute minimum flip count at current based on previous values
    # dynamic programming

    # sanity check
    if len(s) == 1:
      return 0

    # number of 1s in prefix
    ones = 0
    dp = [0 for _ in range(len(s))]
    # count at index 0
    if s[0] == '1':
      ones = 1

    for i in range(1, len(s)):
      if s[i] == '0':
        dp[i] = min(ones, dp[i-1]+1)
      else:
        dp[i] = dp[i-1]
        ones += 1
    
    # results are stored in last index of dp list
    return dp[-1]

