class Solution {
  public int numberOfArrays(String s, int k) {
    // bottom-up dynamic programming (tabulation)

    int n = s.length();
    int mod = (int) Math.pow(10, 9) + 7;
    int[] dp = new int[n+1];
    dp[0] = 1;

    for (int i = 0; i < n; i++) {
      if (s.charAt(i) == '0')
        continue;
      for (int j = i; j < n; j++) {
        // k is int, but substring may not fit in int
        // we break immediately when substr is larger than k
        // so just parse as long and compare
        if (Long.parseLong(s.substring(i,j+1)) > k)
          break;
        dp[j+1] += dp[i];
        dp[j+1] %= mod;
      }
    }
    return dp[n];
  }
}
