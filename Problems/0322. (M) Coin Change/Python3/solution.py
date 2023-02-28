class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    # bottom-up dynamic programming

    # trivial case
    if not amount:
      return 0

    # value of dp[i] is min number of coins that adds up to i
    dp = [float('inf')] * (amount+1)
    dp[0] = 0

    for i in range(1, amount+1):
      for denom in coins:
        if i >= denom:
          dp[i] = min(dp[i], dp[i-denom]+1)

    return dp[-1] if dp[-1] != float('inf') else -1

