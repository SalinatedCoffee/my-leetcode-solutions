class Solution {
  // union find
  public int makeConnected(int n, int[][] connections) {
    // sanity check
    if (connections.length < n-1)
      return -1;

    int[] p = new int[n];
    for (int i = 0; i < n; i++)
      p[i] = i;

    for (int i = 0; i < connections.length; i++)
      uunion(connections[i][0], connections[i][1], p);
    
    // count number of disconnected components
    Set<Integer> components = new HashSet();
    for (int i: p)
      components.add(ufind(i, p));
    
    return components.size() - 1;
  }
  
  private int ufind(int a, int[] p) {
    int pa = p[a];
    while (pa != a) {
      a = pa;
      pa = p[a];
    }
    return pa;
  }

  private void uunion(int a, int b, int[] p) {
    int pa = ufind(a, p);
    int pb = ufind(b, p);
    if (pa > pb)
      p[pb] = pa;
    else
      p[pa] = pb;
  }
}
