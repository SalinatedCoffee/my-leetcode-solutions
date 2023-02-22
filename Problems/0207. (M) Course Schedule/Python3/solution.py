class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # topological sort w/ DFS

    # sanity check
    if numCourses == 0:
      return True

    # generate adjacency list
    adj = [[] for _ in range(numCourses)]
    for c, req in prerequisites:
      adj[c].append(req)

    # 0 means unvisited, -1 means temporarily visited,
    # 1 means permanently visited
    visited = [0 for _ in range(numCourses)]

    def dfs(node):
      status = visited[node]
      if status == 1:
        return True
      if status == -1:
        return False
      visited[node] = -1
      for pre in adj[node]:
        if not dfs(pre):
          return False
      visited[node] = 1
      return True

    # graph may be disconnected, try all courses
    for i in range(numCourses):
      if not dfs(i):
        return False

    return True

