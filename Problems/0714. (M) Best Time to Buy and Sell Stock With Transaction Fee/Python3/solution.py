class Solution:
  def maxProfit(self, prices: List[int], fee: int) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(prices)
    # dp[i][t] is the maximum profit for i-th day, where:
    # if t == 0, holding stock. otherwise, no stock in posession
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = -prices[0]
    
    for i in range(1, n):
      dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
      dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
    
    return dp[-1][1]

