class Solution {
  public int minScore(int n, int[][] roads) {
    // iterative DFS

    List<Pair<Integer,Integer>>[] adj = new ArrayList[n+1];
    for (int i = 0; i < n+1; i++)
      adj[i] = new ArrayList();
    for (int[] road: roads) {
      adj[road[0]].add(new Pair(road[1], road[2]));
      adj[road[1]].add(new Pair(road[0], road[2]));
    }

    int ret = Integer.MAX_VALUE;
    Deque<Pair<Integer,Integer>> nodes = new ArrayDeque();
    nodes.push(new Pair(1, Integer.MAX_VALUE));
    Set<Integer> visited = new HashSet();
    while (nodes.size() > 0) {
      Pair<Integer,Integer> cur = nodes.pop();
      int node = cur.getKey();
      int d = cur.getValue();
      // update min edge before checking if visited
      ret = Math.min(ret, d);
      if (visited.contains(node))
        continue;
      visited.add(node);
      for (Pair<Integer,Integer> next: adj[node])
        nodes.push(next);
    }
    return ret;
  }
}
