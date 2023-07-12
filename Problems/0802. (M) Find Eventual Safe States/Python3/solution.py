class Solution:
  # recursive DFS

  def dfs(self, node, visited, cur_visited, graph):
      if cur_visited[node]:
        return True
      if visited[node]:
        return False
      visited[node] = True
      cur_visited[node] = True
      for nxt in graph[node]:
        if self.dfs(nxt, visited, cur_visited, graph):
          return True
      cur_visited[node] = False

      return False
      
  def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    n = len(graph)
    visited = [False] * n
    cur_visited = [False] * n

    ret = []
    for i in range(n):
      if not self.dfs(i, visited, cur_visited, graph):
        ret.append(i)
    
    return ret

