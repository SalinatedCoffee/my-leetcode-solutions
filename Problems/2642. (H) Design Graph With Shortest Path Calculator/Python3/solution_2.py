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
    # optimized dijkstra's algorithm with priority queue

    nodes = [(0, node1)]
    d = [float('inf')] * self._n
    d[node1] = 0

    while nodes:
      cur_d, cur = heappop(nodes)
      if cur_d > d[cur]:
        continue
      if cur == node2:
        return cur_d
      for v, w in self._adj[cur]:
        new_d = cur_d + w
        if new_d < d[v]:
          d[v] = new_d
          heappush(nodes, (new_d, v))
    
    return -1

