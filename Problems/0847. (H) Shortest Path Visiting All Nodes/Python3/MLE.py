class Solution:
  def shortestPathLength(self, graph: List[List[int]]) -> int:
    # brute force BFS

    n = len(graph)
    full = (1 << n) - 1
    nodes = deque([(0, 1 << i, i) for i in range(n)])
    while nodes:
      d, visited, cur = nodes.popleft()
      if visited == full:
        return d
      for nxt in graph[cur]:
        nodes.append((d+1, visited | (1 << nxt), nxt))
    
    return -1

