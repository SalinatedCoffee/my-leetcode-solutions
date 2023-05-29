class Solution {
  public String stoneGameIII(int[] stoneValue) {
    // bottom-up dynamic programming (tabulation)

    int n = stoneValue.length;
    // dp[i] is score difference of game with stoneValue[-i:]
    int[] dp = new int[n+1];

    for (int i = n-1; i >= 0; i--) {
      dp[i] = stoneValue[i] - dp[i+1];
      if (i + 2 <= n)
        dp[i] = Math.max(dp[i], stoneValue[i] + stoneValue[i+1] - dp[i+2]);
      if (i + 3 <= n)
        dp[i] = Math.max(dp[i], stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3]);
    }
    if (dp[0] > 0)
      return "Alice";
    else if (dp[0] == 0)
      return "Tie";
    else
      return "Bob";
  }
}
