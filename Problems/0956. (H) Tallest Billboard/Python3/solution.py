class Solution:
  def tallestBillboard(self, rods: List[int]) -> int:
    # dynamic programming
    
    dp = {}
    dp[0] = 0

    for r in rods:
      new_dp = dp.copy()
      for d, t in dp.items():
        s = t - d
        new_dp[d+r] = max(new_dp.get(d+r, 0), t+r)
        new_d = abs(s + r - t)
        new_t = max(s + r, t)
        new_dp[new_d] = max(new_dp.get(new_d, 0), new_t)
      dp = new_dp
    
    return dp.get(0, 0)

