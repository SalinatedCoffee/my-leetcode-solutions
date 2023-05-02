class Solution {
  public int numSimilarGroups(String[] strs) {
    // iterative DFS

    // generate graph
    int n = strs.length;
    int m = strs[0].length();
    List<Integer>[] adj = new ArrayList[n];
    for (int i = 0; i < n; i++)
      adj[i] = new ArrayList();
    for (int i = 0; i < n; i++) {
      for (int j = i; j < n; j++) {
        int diff = 0;
        for (int k = 0; k < m; k++) {
          if (strs[i].charAt(k) != strs[j].charAt(k))
            diff++;
        }
        if (diff == 0 || diff == 2) {
          adj[i].add(j);
          adj[j].add(i);
        }
      }
    }

    // count connected components
    boolean[] visited = new boolean[n];
    int ret = 0;
    Deque<Integer> nodes = new ArrayDeque();
    for (int i = 0; i < n; i++) {
      if (visited[i])
        continue;
      ret++;
      nodes.push(i);
      while (nodes.size() > 0) {
        int cur = nodes.pop();
        if (visited[cur])
          continue;
        visited[cur] = true;
        for (int nxt: adj[cur]) {
          if (!visited[nxt])
            nodes.push(nxt);
        }
      }
    }
    return ret;
  }
}
