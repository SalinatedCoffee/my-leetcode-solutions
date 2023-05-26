class Solution:
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    # iterative BFS
    
    adj = {}
    for i, edge in enumerate(equations):
      if edge[0] not in adj:
        adj[edge[0]] = []
      if edge[1] not in adj:
        adj[edge[1]] = []
      adj[edge[0]].append((edge[1], values[i]))
      adj[edge[1]].append((edge[0], 1/values[i]))
    
    ret = []
    for u, v in queries:
      ans = -1
      if u in adj and v in adj: 
        nodes = deque()
        nodes.append((u, 1))
        visited = set()
        while nodes:
          cur, f = nodes.popleft()
          if cur in visited or cur not in adj:
            continue
          if cur == v:
            ans = f
            break
          visited.add(cur)
          for nxt, n_f in adj[cur]:
            nodes.append((nxt, f*n_f))
      ret.append(ans)
    
    return ret

