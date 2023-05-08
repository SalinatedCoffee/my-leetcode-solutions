class Solution:
  def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
    # recursive DFS

    n = len(colors)
    # adj[i] contains nodes that have edges incoming from node i
    adj = [[] for i in range(n)]
    for u, v in edges:
      adj[u].append(v)
    # count[i][c] contains largest color value of color c starting at node i
    count = [[0]*26 for i in range(n)]
    visited = [False] * n
    in_stack = [False] * n

    def dfs(node):
      # node has already been traversed, cycle detected
      if in_stack[node]:
        return float('inf')
      c_idx = int(ord(colors[node]) - ord('a'))
      if visited[node]:
        return count[node][c_idx]
      visited[node] = True
      in_stack[node] = True
      for nxt in adj[node]:
        if dfs(nxt) == float('inf'):
          return float('inf')
        # update color frequency for current node
        for i in range(26):
          count[node][i] = max(count[nxt][i], count[node][i])
      # count color of current node
      count[node][c_idx] += 1
      in_stack[node] = False
      return count[node][c_idx]

    ret = 0
    for i in range(n):
      ret = max(ret, dfs(i))
    
    return ret if ret != float('inf') else -1

