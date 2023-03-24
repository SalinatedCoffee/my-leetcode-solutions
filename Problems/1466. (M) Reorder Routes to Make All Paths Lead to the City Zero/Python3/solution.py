oclass Solution:
  def minReorder(self, n: int, connections: List[List[int]]) -> int:
    # BFS

    # build adjacency list and set of directed edges
    adj = [[] for _ in range(n)]
    edges = set()
    for edge in connections:
      adj[edge[0]].append(edge[1])
      adj[edge[1]].append(edge[0])
      edges.add((edge[0], edge[1]))
    
    ret = 0
    nodes = deque()
    nodes.append((None, 0))
    visited = set()
    while nodes:
      prev, cur = nodes.popleft()
      if cur in visited:
        continue
      visited.add(cur)
      # count reversed edges
      if (prev, cur) in edges:
        ret += 1
      for d in adj[cur]:
        nodes.append((cur, d))
    
    return ret

