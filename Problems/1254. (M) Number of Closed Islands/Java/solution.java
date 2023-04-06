class Solution {
  // iterative DFS
  public int closedIsland(int[][] grid) {
    Set<Pair<Integer,Integer>> visited = new HashSet();
    int ret = 0;
    for (int i = 0; i < grid.length; i++) {
      for (int j = 0; j < grid[0].length; j++) {
        if (grid[i][j] == 0 && dfs(i, j, grid, visited))
          ret++;
      }
    }
    return ret;
  }
  private boolean dfs(int y, int x, int[][] grid, Set<Pair<Integer,Integer>> visited) {
    // sanity check
    if (visited.contains(new Pair<Integer,Integer>(y,x)))
      return false;
    boolean border = false;
    Deque<Pair<Integer,Integer>> nodes = new ArrayDeque();
    nodes.push(new Pair<Integer,Integer>(y,x));
    while (nodes.size() > 0) {
      Pair<Integer,Integer> cur = nodes.pop();
      if (visited.contains(cur))
        continue;
      visited.add(cur);
      int c_y = cur.getKey();
      int c_x = cur.getValue();
      // raise flag if land square is in border
      if (c_y == 0 || c_y == grid.length-1 || c_x == 0 || c_x == grid[0].length-1)
        border = true;
      int[][] next = {{c_y+1,c_x}, {c_y,c_x+1}, {c_y-1,c_x}, {c_y,c_x-1}};
      for (int[] coord: next) {
        int n_y = coord[0], n_x = coord[1];
        if (0 <= n_y && n_y < grid.length && 0 <= n_x && n_x < grid[0].length &&
          grid[n_y][n_x] == 0)
          nodes.push(new Pair<Integer,Integer>(coord[0],coord[1]));
      }
    }
    return !border;
  }
}
