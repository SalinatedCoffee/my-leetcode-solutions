class Solution {
  // top-down dynamic programming (memoization)

  public int minInsertions(String s) {
    int n = s.length();
    // dp[i][j] is the length of the LCSs between s[:i+1] and s_rev[:j+1]
    int[][] dp = new int[n+1][n+1];
    for (int[] i: dp)
      Arrays.fill(i, -1);
    StringBuffer sbr = new StringBuffer(s);
    sbr.reverse();
    String s_rev = sbr.toString();

    return n - recurse(s, s_rev, n, n, dp);
  }

  public int recurse(String s1, String s2, int l1, int l2, int[][] dp) {
    if (l1 == 0 || l2 == 0)
      return 0;
    if (dp[l1][l2] != -1)
      return dp[l1][l2];
    if (s1.charAt(l1-1) == s2.charAt(l2-1))
      return dp[l1][l2] = 1 + recurse(s1, s2, l1-1, l2-1, dp);
    else
      return dp[l1][l2] = Math.max(recurse(s1, s2, l1-1, l2, dp), recurse(s1, s2, l1, l2-1, dp));
  }
}
