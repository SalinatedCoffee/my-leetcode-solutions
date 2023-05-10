class Solution {
  public int[][] generateMatrix(int n) {
    // process edges and shrink

    int[][] ret = new int[n][n];
    int l = 0;
    int h = n-1;
    int c = 1;
    while (l < h) {
      for (int i = l; i < h; i++) {
        ret[l][i] = c;
        c++;
      }
      for (int i = l; i < h; i++) {
        ret[i][h] = c;
        c++;
      }
      for (int i = h; i > l-1; i--) {
        ret[h][i] = c;
        c++;
      }
      for (int i = h-1; i > l; i--) {
        ret[i][l] = c;
        c++;
      }
      l++;
      h--;
    }

    if (n % 2 == 1)
      ret[l][l] = c;

    return ret;
  }
}
