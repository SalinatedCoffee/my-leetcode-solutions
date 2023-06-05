class Solution {
  public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
    // iterative DFS

    List<Integer>[] adj = new List[n];
    for (int i = 0; i < n; i++)
      adj[i] = new ArrayList();
    for (int i = 0; i < n; i++) {
      if (manager[i] != -1)
        adj[manager[i]].add(i);
    }

    int ret = -1;
    Deque<Pair<Integer,Integer>> nodes = new ArrayDeque();
    nodes.push(new Pair(headID, 0));
    while (nodes.size() > 0) {
      Pair<Integer,Integer> cur = nodes.pop();
      if (adj[cur.getKey()].size() == 0)
        ret = Math.max(ret, cur.getValue());
      else {
        for (int nxt: adj[cur.getKey()])
          nodes.push(new Pair(nxt, cur.getValue()+informTime[cur.getKey()]));
      }
    }
    return ret;
  }
}
