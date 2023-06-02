class Solution {
  public int maximumDetonation(int[][] bombs) {
    // iterative DFS

    int n = bombs.length;
    List<Integer>[] adj = new ArrayList[n];
    for (int i = 0; i < n; i++) {
      adj[i] = new ArrayList();
      for (int j = 0; j < n; j++) {
        if (i == j)
          continue;
        double dy = Math.pow(bombs[i][0] - bombs[j][0], 2);
        double dx = Math.pow(bombs[i][1] - bombs[j][1], 2);
        double d = Math.sqrt(dy+dx);
        if (bombs[i][2] >= d)
          adj[i].add(j);
      }
    }

    int ret = -1;
    for (int i = 0; i < n; i++) {
      Deque<Integer> nodes = new ArrayDeque();
      nodes.push(i);
      Set<Integer> visited = new HashSet();
      visited.add(i);
      int count = 0;
      while (nodes.size() > 0) {
        int cur = nodes.pop();
        count++;
        for (int j = 0; j < adj[cur].size(); j++) {
          int nxt = adj[cur].get(j);
          if (!visited.contains(nxt)) {
            nodes.push(nxt);
            visited.add(nxt);
          }
        }
      }
      ret = Math.max(ret, count);
    }
    return ret;
  }
}
