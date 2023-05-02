class Solution {
  // union find

  public int maxNumEdgesToRemove(int n, int[][] edges) {
    UnionFind alice = new UnionFind(n);
    UnionFind bob = new UnionFind(n);
    int req_edges = 0;
    int idx = 0;
    // sort 2d array by first element in descending order
    Arrays.sort(edges, (a, b) -> Integer.compare(b[0], a[0]));
    while (idx < edges.length && edges[idx][0] == 3) {
      boolean a_e = alice.uunion(edges[idx][1], edges[idx][2]);
      boolean b_e = bob.uunion(edges[idx][1], edges[idx][2]);
      if (a_e || b_e)
        req_edges++;
      idx++;
    }
    while (idx < edges.length && edges[idx][0] == 2) {
      if (bob.uunion(edges[idx][1], edges[idx][2]))
        req_edges++;
      idx++;
    }
    while (idx < edges.length && edges[idx][0] == 1) {
      if (alice.uunion(edges[idx][1], edges[idx][2]))
        req_edges++;
      idx++;
    }
    if (alice.components() == 1 && bob.components() == 1)
      return edges.length - req_edges;
    return -1;
  }

  class UnionFind {
    private int[] parents;
    private int components;
    private int size;

    public UnionFind(int n) {
      parents = new int[n+1];
      for (int i = 0; i < n+1; i++)
        parents[i] = i;
      components = n;
      size = n;
    }

    public boolean uunion(int a, int b) {
      int p_a = ufind(a);
      int p_b = ufind(b);
      if (p_a == -1 || p_b == -1 || p_a == p_b)
        return false;
      if (p_a > p_b)
        parents[p_b] = p_a;
      else
        parents[p_a] = p_b;
      components--;
      return true;
    }

    private int ufind(int a) {
      if (a > size)
        return -1;
      int prev = a;
      int cur = parents[a];
      while (cur != prev) {
        prev = cur;
        cur = parents[cur];
      }
      return cur;
    }

    public int components() {
      return components;
    }
  }
}
