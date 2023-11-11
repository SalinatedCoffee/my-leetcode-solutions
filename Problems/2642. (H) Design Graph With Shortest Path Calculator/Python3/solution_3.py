class Graph:
  # floyd-warshall algorithm
  
  def __init__(self, n: int, edges: List[List[int]]):
    self._adj = [[float('inf')]*n for _ in range(n)]
    self._n = n
    for u, v, w in edges:
      self._adj[u][v] = w
    for i in range(n):
      self._adj[i][i] = 0
    for k in range(self._n):
      for i in range(self._n):
        for j in range(self._n):
          self._adj[i][j] = min(self._adj[i][j], self._adj[i][k] + self._adj[k][j])

  def addEdge(self, edge: List[int]) -> None:
    u, v, w = edge
    for i in range(self._n):
      for j in range(self._n):
        self._adj[i][j] = min(self._adj[i][j], self._adj[i][u] + self._adj[v][j] + w)

  def shortestPath(self, node1: int, node2: int) -> int:
    return self._adj[node1][node2] if self._adj[node1][node2] != float('inf') else -1

