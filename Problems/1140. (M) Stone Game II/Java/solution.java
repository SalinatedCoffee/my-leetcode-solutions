class Solution {
  // top-down dynamic programming (memoization)
  
  // dp[i][j][k] is max number of stones for game with parameters:
  //  player i (0 == Alice, 1 == Bob)
  //  piles[j:] set of piles
  //  M = k
  int[][][] dp;
  int n;

  public int stoneGameII(int[] piles) {
    this.n = piles.length;
    this.dp = new int[2][n+1][n+1];
    for (int[][] i: this.dp) {
      for (int[] j: i)
        Arrays.fill(j, -1);
    }

    return recurse(0, 0, 1, piles);
  }

  private int recurse(int p, int i, int m, int[] piles) {
    if (i == this.n)
      return 0;
    if (this.dp[p][i][m] != -1)
      return this.dp[p][i][m];
    int ret = p == 1 ? Integer.MAX_VALUE : -1;
    int s = 0;
    for (int j = 1; j < Math.min(2*m, this.n-i)+1; j++) {
      s += piles[i+j-1];
      if (p == 1)
        ret = Math.min(ret, recurse(0, i+j, Math.max(m, j), piles));
      else
        ret = Math.max(ret, s+recurse(1, i+j, Math.max(m, j), piles));
    }
    return dp[p][i][m] = ret;
  }
}
