class Solution {
  public int minDistance(String word1, String word2) {
    // bottom-up dynamic programming

    int m = word1.length();
    int n = word2.length();
    // dp[i][j] stores the minimum edit distance between
    // word1[:j+1] and word2[:i+1] (Python slices)
    int[][] dp = new int[n+1][m+1];
    // initialize cases where either string is empty
    for (int i = 0; i <= m; i++)
      dp[0][i] = i;
    for (int i = 0; i <= n; i++)
      dp[i][0] = i;
    
    // fill dp towards bottom right
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        if (word1.charAt(j-1) == word2.charAt(i-1))
          dp[i][j] = dp[i-1][j-1];
        else
          dp[i][j] = Math.min(Math.min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
      }
    }
    // return desired value
    return dp[n][m];
  }
}
