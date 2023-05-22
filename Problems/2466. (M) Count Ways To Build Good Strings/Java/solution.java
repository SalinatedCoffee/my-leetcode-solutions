class Solution {
  public int countGoodStrings(int low, int high, int zero, int one) {
    // bottom-up dynamic programming (tabulation)

    int[] dp = new int[high+1];
    dp[0] = 1;
    int mod = 1000000007;

    for (int i = 1; i < high+1; i++) {
      if (i >= zero)
        dp[i] += dp[i-zero];
      if (i >= one)
        dp[i] += dp[i-one];
      dp[i] %= mod;
    }
    int ret = 0;
    for (int i = low; i <= high; i++) {
      ret += dp[i];
      ret %= mod;
    }
    return ret;
  }
}
