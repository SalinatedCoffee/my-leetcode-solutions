class Solution {
  public int longestCycle(int[] edges) {
    // simple graph traversal

    // visited[i][0]: traversal source node
    // visited[i][1]: length of path to node i
    int[][] visited = new int[edges.length][2];
    int ret = -1;
    for (int i = 0; i < edges.length; i++) {
      int len = 1;
      int cur = i;
      while (cur != -1 && visited[cur][1] == 0) {
        visited[cur][0] = i;
        visited[cur][1] = len++;
        cur = edges[cur];
      }
      if (cur != -1 && visited[cur][0] == i)
        ret = Math.max(ret, len - visited[cur][1]);
    }
    return ret;
  }
}
