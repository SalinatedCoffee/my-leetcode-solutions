class Solution:
  def shortestPathLength(self, graph: List[List[int]]) -> int:
    # iterative bfs

    n = len(graph)
    full = (1 << n) - 1
    nodes = deque([(0, 1 << i, i) for i in range(n)])
    visited = set((1 << i, i) for i in range(n))
    while nodes:
      d, bits, cur = nodes.popleft()
      if bits == full:
        return d
      for nxt in graph[cur]:
        nxt_v = bits | (1 << nxt)
        if (nxt_v, nxt) not in visited:
          visited.add((nxt_v, nxt))
          nodes.append((d+1, nxt_v, nxt))
    
    return -1

