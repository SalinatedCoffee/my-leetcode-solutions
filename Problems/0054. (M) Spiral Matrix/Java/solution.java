class Solution {
  public List<Integer> spiralOrder(int[][] matrix) {
    // walk edges and shrink

    List<Integer> ret = new ArrayList();
    int m = matrix[0].length;
    int n = matrix.length;
    int l = 0;
    int u = 0;
    int r = m;
    int d = n;
    while (l < r-1 && u < d-1) {
      for (int i = l; i < r; i++)
        ret.add(matrix[u][i]);
      for (int i = u+1; i < d; i++)
        ret.add(matrix[i][r-1]);
      for (int i = r-2; i > l-1; i--)
        ret.add(matrix[d-1][i]);
      for (int i = d-2; i > u; i--)
        ret.add(matrix[i][l]);
      l++;
      r--;
      u++;
      d--;
    }
    if (ret.size() < m*n) {
      if (n > m) {
        for (int i = u; i < d; i++)
          ret.add(matrix[i][l]);
      }
      else {
        for (int i = l; i < r; i++)
          ret.add(matrix[u][i]);
      }
    }
    return ret;
  }
}
