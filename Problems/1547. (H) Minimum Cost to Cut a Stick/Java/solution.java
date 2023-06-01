class Solution {
  public int minCost(int n, int[] cuts) {
    // bottom-up dynamic programming (tabulation)

    int m = cuts.length;
    Arrays.sort(cuts);
    int[] cuts_new = new int[m+2];
    for (int i = 0; i < m+2; i++) {
      if (i == 0)
        cuts_new[i] = 0;
      else if (i == m+1)
        cuts_new[i] = n;
      else
        cuts_new[i] = cuts[i-1];
    }
    int[][] dp = new int[m+2][m+2];

    for (int i = 2; i < m+2; i++) {
      for (int l = 0; l < m+2-i; l++) {
        int r = l + i;
        int ans = Integer.MAX_VALUE;
        for (int j = l+1; j < r; j++)
          ans = Math.min(ans, dp[l][j]+dp[j][r]+cuts_new[r]-cuts_new[l]);
        dp[l][r] = ans;
      }
    }
    return dp[0][m+1];
  }
}
