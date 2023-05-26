class Solution {
  public double new21Game(int n, int k, int maxPts) {
    // bottom-up dynamic programming (tabulation)

    // dp[i] is probability of obtaining score i
    double[] dp = new double[n+1];
    dp[0] = 1;
    double s = k == 0 ? 0 : 1;

    for (int i = 1; i < n + 1; i++) {
      dp[i] = s / maxPts;
      if (i < k)
        s += dp[i];
      if (i - maxPts >= 0 && i - maxPts < k)
        s -= dp[i - maxPts];
    }
    return Arrays.stream(dp, k, n+1).sum();
  }
}
