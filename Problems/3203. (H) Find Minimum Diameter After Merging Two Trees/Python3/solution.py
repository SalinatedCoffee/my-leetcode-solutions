class Solution:
  def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
    # iterative BFS

    # return adjacency list built from list of edges edges
    def build_adjacency(edges):
      res = defaultdict(list)
      for u, v in edges:
        res[u].append(v)
        res[v].append(u)
      return res

    adj1, adj2 = build_adjacency(edges1), build_adjacency(edges2)

    # return farthest node from node
    # in the graph represented by adjacency list adj
    def farthest_node_of(node, adj):
      nodes = deque([(node, 0)])
      visited = set()
      res, res_d = node, 0
      while nodes:
        cur, d = nodes.popleft()
        visited.add(cur)
        if d > res_d:
          res, res_d = cur, d
        for nxt in adj[cur]:
          if nxt not in visited:
            nodes.append((nxt, d+1))

      return (res, res_d)

    # return diameter of graph represented by adjacency list adj
    def diameter_of(adj):
      a, _ = farthest_node_of(0, adj)
      _, b_d = farthest_node_of(a, adj)
      return b_d
    
    d1, d2 = diameter_of(adj1), diameter_of(adj2)

    return max(d1, d2, ceil(d1 / 2) + ceil(d2 / 2 + 1))

