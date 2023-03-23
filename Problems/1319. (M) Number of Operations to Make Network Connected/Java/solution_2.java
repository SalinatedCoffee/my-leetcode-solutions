class Solution {
  public int makeConnected(int n, int[][] connections) {
    // DFS

    // sanity check
    if (connections.length < n-1)
      return -1;

    ArrayList<Integer>[] adj = new ArrayList[n];
    for (int i = 0; i < n; i++)
      adj[i] = new ArrayList();
    for (int[] cable: connections) {
      adj[cable[0]].add(cable[1]);
      adj[cable[1]].add(cable[0]);
    }

    int components = 0;
    Set<Integer> visited = new HashSet();
    for (int i = 0; i < n; i++) {
      Deque<Integer> nodes = new ArrayDeque();
      boolean valid = false;
      nodes.push(i);
      while (nodes.size() > 0) {
        int cur = nodes.pop();
        if (visited.contains(cur))
          continue;
        valid = true;
        visited.add(cur);
        for (int d: adj[cur])
          nodes.push(d);
      }
      // count component
      if (valid)
        components++;
    }
    return components - 1;
  }
}
