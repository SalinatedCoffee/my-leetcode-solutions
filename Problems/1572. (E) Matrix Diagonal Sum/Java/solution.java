class Solution {
  public int diagonalSum(int[][] mat) {
    // iteration

    int n = mat.length;
    int ret = 0;
    for (int r = 0; r < n / 2; r++)
      ret += mat[r][r] + mat[r][n-1-r] + mat[n-1-r][r] + mat[n-1-r][n-1-r];
    if (n % 2 == 1)
      ret += mat[n/2][n/2];
    return ret;
  }
}
