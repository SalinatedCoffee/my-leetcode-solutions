class Solution {
  public long countPairs(int n, int[][] edges) {
    // iterative DFS

    // sanity check
    if (edges.length == 0)
      return (long) n*(n-1)/2;
    
    ArrayList<Integer>[] adj = new ArrayList[n];
    for (int i = 0; i < n; i++)
      adj[i] = new ArrayList();
    for (int i = 0; i < edges.length; i++) {
      adj[edges[i][0]].add(edges[i][1]);
      adj[edges[i][1]].add(edges[i][0]);
    }

    ArrayList<Long> counts = new ArrayList();
    Set<Integer> visited = new HashSet();
    // perform DFS starting at each node
    for (int i = 0; i < n; i++) {
      if (visited.contains(i))
        continue;
      Deque<Integer> nodes = new ArrayDeque();
      nodes.push(i);
      long count = 0;
      while (nodes.size() > 0) {
        int cur = nodes.pop();
        if (visited.contains(cur))
          continue;
        visited.add(cur);
        count++;
        for (int nxt: adj[cur])
          nodes.push(nxt);
      }
      // record size if disconnected component
      if (count != 0)
        counts.add(count);
    }

    // nC2, all possible pairs of nodes
    long total = (long) n*(n-1)/2;
    // subtract connected pairs
    for (long count: counts)
      total -= count*(count-1)/2;
    return total;
  }
}
