class Solution {
  public int countNegatives(int[][] grid) {
    // simple iteration

    int m = grid.length;
    int n = grid[0].length;
    int c = n-1;
    int ret = 0;
    for (int i = 0; i < m; i++) {
      while (c >= 0) {
        if (grid[i][c] < 0) {
          c--;
          continue;
        }
        else
          break;
      }
      ret += c != -1 ? n-1-c : n;
    }
    return ret;
  }
}
