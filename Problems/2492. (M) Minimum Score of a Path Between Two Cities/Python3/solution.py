class Solution:
  def minScore(self, n: int, roads: List[List[int]]) -> int:
    # iterative DFS

    adj = [[] for _ in range(n+1)]
    for u, v, d in roads:
      adj[u].append((v,d))
      adj[v].append((u,d))
    
    ret = float('inf')
    nodes = []
    nodes.append((1, float('inf')))
    visited = set()
    while nodes:
      cur, d = nodes.pop()
      # update min edge before checking if visited
      ret = min(ret, d)
      if cur in visited:
        continue
      visited.add(cur)
      for n_n, n_d in adj[cur]:
        nodes.append((n_n, n_d))
    
    return ret
    
