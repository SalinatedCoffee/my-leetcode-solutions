class Solution {
  public List<List<Integer>> pacificAtlantic(int[][] heights) {
    // DFS, reverse source and destination

    int n = heights.length;
    int m = heights[0].length;
    // sanity check
    if (n == 0)
      return new ArrayList<List<Integer>>();
    
    boolean[][] p = new boolean[n][m];
    boolean[][] a = new boolean[n][m];

    // traverse starting from shore squares
    for (int i = 0; i < n; i++) {
      dfs(i, 0, p, n, m, heights);
      dfs(i, m-1, a, n, m, heights);
    }
    for (int i = 0; i < m; i++) {
      dfs(0, i, p, n, m, heights);
      dfs(n-1, i, a, n, m, heights);
    }

    List<List<Integer>> ret = new ArrayList();
    // get squares that flows to both oceans
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (p[i][j] && a[i][j])
          ret.add((List<Integer>) Arrays.asList(new Integer[]{i,j}));
      }
    }
    return ret;
  }

  private void dfs(int y, int x, boolean[][] ocean, int n, int m, int[][] h) {
    Deque<Pair<Integer,Integer>> nodes = new ArrayDeque();
    nodes.push(new Pair(y,x));
    while (nodes.size() > 0) {
      Pair<Integer,Integer> cur = nodes.pop();
      int u = cur.getKey();
      int v = cur.getValue();
      if (ocean[u][v])
        continue;
      ocean[u][v] = true;
      int[][] dest = {{u-1,v}, {u,v-1}, {u+1,v}, {u,v+1}};
      for (int[] coord: dest) {
        if (0 <= coord[0] && coord[0] < n &&
            0 <= coord[1] && coord[1] < m &&
            h[u][v] <= h[coord[0]][coord[1]])
          nodes.push(new Pair(coord[0], coord[1]));
      }
    }
  }
}
