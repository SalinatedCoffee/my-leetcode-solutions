class Solution {
  // iterative BFS

  static int[] d_row = {1, 0, -1, 0, 1, 1, -1, -1};
  static int[] d_col = {0, 1, 0, -1, 1, -1, 1, -1};

  public int shortestPathBinaryMatrix(int[][] grid) {
    // sanity check
    if (grid[0][0] == 1)
      return -1;

    int n = grid.length;
    Deque<int[]> nodes = new ArrayDeque();
    boolean[][] visited = new boolean[n][n];
    nodes.add(new int[] {0,0,1});
    visited[0][0] = true;
    while (nodes.size() > 0) {
      int[] cur = nodes.removeFirst();
      int y = cur[0];
      int x = cur[1];
      if (y == n-1 && x == n-1)
        return cur[2];
      for (int i = 0; i < 8; i++) {
        int n_y = y + d_row[i];
        int n_x = x + d_col[i];
        if (0 <= n_y && n_y < n && 0 <= n_x && n_x < n) {
          if (grid[n_y][n_x] == 0) {
            grid[n_y][n_x] = 1;
            nodes.add(new int[] {n_y,n_x,cur[2]+1});
          }
        }
      }
    }
    return -1;
  }
}
