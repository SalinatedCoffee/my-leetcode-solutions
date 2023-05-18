class Solution {
  // top-down dynamic programming (memoization)
  public int maxUncrossedLines(int[] nums1, int[] nums2) {
    int n = nums1.length;
    int m = nums2.length;
    // dp[i][j] is value of recurse(i, j)
    int[][] dp = new int[n][m];
    for (int i = 0; i < n; i++)
      Arrays.fill(dp[i], -1);

    return recurse(n-1, m-1, dp, nums1, nums2);
  }

  private int recurse(int i, int j, int[][] dp, int[] nums1, int[] nums2) {
    // returns max. number of lines between nums1[:i+1] and nums2[:j+1]
    if (i < 0 || j < 0)
      return 0;
    
    if (dp[i][j] != -1)
      return dp[i][j];

    if (nums1[i] == nums2[j])
      dp[i][j] = 1 + recurse(i-1, j-1, dp, nums1, nums2);
    else
      dp[i][j] = Math.max(recurse(i-1, j, dp, nums1, nums2), recurse(i, j-1, dp, nums1, nums2));
    
    return dp[i][j];
  }
}
