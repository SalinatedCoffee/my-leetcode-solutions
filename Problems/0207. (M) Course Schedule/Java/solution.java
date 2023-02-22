class Solution {
  public boolean dfs(int node, int[] visited, List<Integer>[] adj) {
    int status = visited[node];
    if (status == 1)
      return true;
    if (status == -1)
      return false;
    visited[node] = -1;
    for (int i = 0; i < adj[node].size(); i++) {
      if (dfs(adj[node].get(i), visited, adj) == false)
        return false;
    }
    visited[node] = 1;
    return true;
  }

  public boolean canFinish(int numCourses, int[][] prerequisites) {
    // topological sort w/ DFS

    // array of ArrayLists
    List<Integer>[] adj = new ArrayList[numCourses];
    // instantiate each ArrayList manually
    for (int i = 0; i < numCourses; i++)
      adj[i] = new ArrayList<Integer>();
    // generate adjacency list
    for (int i = 0; i < prerequisites.length; i++) {
      int c = prerequisites[i][0];
      int req = prerequisites[i][1];
      adj[c].add(req);
    }

    // 0 means unvisited, -1 means temporarily visited,
    // 1 means permanently visited
    int[] visited = new int[numCourses];

    // graph may be disconnected, try all courses
    for (int i = 0; i < numCourses; i++) {
      if (dfs(i, visited, adj) == false)
        return false;
    }
    return true;
  }
}
