class Solution:
  def stoneGameIII(self, stoneValue: List[int]) -> str:
    # bottom-up dynamic programming (tabulation)

    n = len(stoneValue)
    # dp[i] is score difference of game with stoneValue[-i:]
    dp = [0] * (n+1)

    for i in range(n-1, -1, -1):
      dp[i] = stoneValue[i] - dp[i+1]
      if i + 2 <= n:
        dp[i] = max(dp[i], stoneValue[i] + stoneValue[i+1] - dp[i+2])
      if i + 3 <= n:
        dp[i] = max(dp[i], stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3])
    
    if dp[0] > 0:
      return "Alice"
    elif not dp[0]:
      return "Tie"
    else:
      return "Bob"

