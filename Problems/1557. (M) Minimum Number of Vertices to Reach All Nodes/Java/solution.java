class Solution {
  public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
    // adjacency list

    List<Integer>[] adj = new List[n];
    for (int i = 0; i < n; i++)
      adj[i] = new ArrayList();
    for (List<Integer> edge: edges)
      adj[edge.get(1)].add(edge.get(0));
    
    List<Integer> ret = new ArrayList();
    for (int i = 0; i < n; i++) {
      if (adj[i].size() == 0)
        ret.add(i);
    }
    return ret;
  }
}
