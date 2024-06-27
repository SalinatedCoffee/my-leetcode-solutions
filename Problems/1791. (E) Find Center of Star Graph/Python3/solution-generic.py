class Solution:
  def findCenter(self, edges: List[List[int]]) -> int:
    # iterative DFS

    adj = defaultdict(list)

    # convert list of edges to adjacency list
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)
  
    # start at arbitrary leaf node
    for node, deg in adj.items():
      if len(deg) == 1:
        origin = node
        break

    # determine diameter of graph
    d = 2
    cur = adj[origin][0]
    visited = set([origin])
    while len(adj[cur]) > 1:
      visited.add(cur)
      d += 1
      for nxt in adj[cur]:
        if nxt not in visited:
          cur = nxt
          break

    # find center node
    tgt = d // 2
    visited = set()
    cur = origin
    while tgt:
      tgt -= 1
      visited.add(cur)
      for nxt in adj[cur]:
        if nxt not in visited:
          cur = nxt
          break

    return cur

