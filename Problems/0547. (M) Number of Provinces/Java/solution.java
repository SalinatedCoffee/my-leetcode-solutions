class Solution {
  public int findCircleNum(int[][] isConnected) {
    // iterative DFS

    int n = isConnected.length;

    int ret = 0;
    boolean[] visited = new boolean[n];
    for (int i = 0; i < n; i++) {
      if (!visited[i]) {
        Deque<Integer> nodes = new ArrayDeque();
        nodes.push(i);
        while (nodes.size() > 0) {
          int cur = nodes.pop();
          for (int j = 0; j < n; j++) {
            if (isConnected[cur][j] == 1 && !visited[j]) {
              nodes.push(j);
              visited[j] = true;
            }
          }
        }
        ret++;
      }
    }
    return ret;
  }
}
