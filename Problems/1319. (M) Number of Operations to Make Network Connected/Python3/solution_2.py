class Solution:
  def makeConnected(self, n: int, connections: List[List[int]]) -> int:
    # DFS

    # sanity check
    if len(connections) < n-1:
      return -1

    adj = [[] for _ in range(n)]
    for u, v in connections:
      adj[u].append(v)
      adj[v].append(u)

    components = 0
    visited = set()
    for s in range(n):
      nodes = [s]
      valid = False
      while nodes:
        cur = nodes.pop()
        if cur in visited:
          continue
        valid = True
        visited.add(cur)
        for d in adj[cur]:
          nodes.append(d)
      # count component
      if valid:
        components += 1

    return components - 1

