class Graph:
  def __init__(self, n: int, edges: List[List[int]]):
    self._adj = [[] for _ in range(n)]
    self._n = n
    for u, v, w in edges:
      self._adj[u].append((v, w))

  def addEdge(self, edge: List[int]) -> None:
    u, v, w = edge
    self._adj[u].append((v, w))

  def shortestPath(self, node1: int, node2: int) -> int:
    # dijkstra's algorithm with priority queue

    d = [float('inf')] * self._n
    d[node1] = 0
    nodes = [(0, node1)]
    while nodes:
      cur_d, cur = heappop(nodes)
      for v, w in self._adj[cur]:
        new_d = d[cur] + w
        if new_d < d[v]:
          d[v] = new_d
          heappush(nodes, (new_d, v))
    
    return d[node2] if d[node2] != float('inf') else -1

