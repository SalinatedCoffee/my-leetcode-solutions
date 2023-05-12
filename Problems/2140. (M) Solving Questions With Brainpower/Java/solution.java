class Solution {
  public long mostPoints(int[][] questions) {
    // bottom-up dynamic programming (tabulation)

    int n = questions.length;
    // dp[i] is maximum score solving problems in questions[i:]
    long[] dp = new long[n];
    dp[n-1] = questions[n-1][0];

    for (int i = n-2; i >= 0; i--) {
      dp[i] = questions[i][0];
      int c_s = questions[i][1];
      if (i + c_s + 1 < n)
        dp[i] += dp[i + c_s + 1];
      dp[i] = Math.max(dp[i], dp[i+1]);
    }
    return dp[0];
  }
}
