class Solution:
  def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    # recursive DFS

    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    nodes = [source]
    visited = set()
    while nodes:
      cur = nodes.pop()
      if cur in visited:
        continue
      if cur == destination:
        return True
      visited.add(cur)
      for nxt in adj[cur]:
        nodes.append(nxt)

    return False

