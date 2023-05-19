class Solution {
  public boolean isBipartite(int[][] graph) {
    // iterative DFS

    int n = graph.length;
    int[] coloring = new int[n];
    Arrays.fill(coloring, -1);
    for (int i = 0; i < n; i++) {
      if (coloring[i] != -1)
        continue;
      
      Deque<Pair<Integer,Integer>> nodes = new ArrayDeque();
      nodes.push(new Pair(i,1));
      while (nodes.size() > 0) {
        Pair<Integer,Integer> node = nodes.pop();
        int cur = node.getKey();
        int color = node.getValue();
        if (coloring[cur] != -1) {
          if (coloring[cur] != color)
            return false;
          continue;
        }
        coloring[cur] = color;

        color ^= 1;
        for (int nxt: graph[cur])
          nodes.push(new Pair(nxt, color));
      }
    }
    return true;
  }
}
