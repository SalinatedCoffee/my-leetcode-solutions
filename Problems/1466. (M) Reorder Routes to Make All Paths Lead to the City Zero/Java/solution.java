class Solution {
  public int minReorder(int n, int[][] connections) {
    // BFS

    // build adjacency list and set of directed edges
    ArrayList<Integer>[] adj = new ArrayList[n];
    for (int i = 0; i < n; i++)
      adj[i] = new ArrayList();
    Set<Pair<Integer,Integer>> edges = new HashSet();
    for (int i = 0; i < connections.length; i++) {
      int u = connections[i][0];
      int v = connections[i][1];
      adj[u].add(v);
      adj[v].add(u);
      // template type can be omitted as edges was already declared as
      // a set of pairs of integers
      edges.add(new Pair(u,v));
    }

    int ret = 0;
    Deque<Pair<Integer,Integer>> nodes = new ArrayDeque();
    nodes.add(new Pair(-1,0));
    Set<Integer> visited = new HashSet();
    while (nodes.size() > 0) {
      Pair<Integer,Integer> cur = nodes.pop();
      if (visited.contains(cur.getValue()))
        continue;
      visited.add(cur.getValue());
      // count reversed edges
      if (edges.contains(cur))
        ret++;
      for (int d: adj[cur.getValue()])
        nodes.add(new Pair(cur.getValue(), d));
    }
    return ret;
  }
}
