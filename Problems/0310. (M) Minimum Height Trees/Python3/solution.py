class Solution:
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    # DFS

    # convert list of edges to adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    def dfs_furthest(source):
      # returns label of furthest node from source

      furthest, f_d = source, 0
      visited = set()
      nodes = [(source, 0)]
      while nodes:
        cur, d = nodes.pop()
        if cur in visited:
          continue
        visited.add(cur)
        if d > f_d:
          f_d = d
          furthest = cur
        for nxt in adj[cur]:
          nodes.append((nxt, d+1))
      
      return furthest
    
    # find source and destination of 'diameter path' of graph
    source = dfs_furthest(0)
    dest = dfs_furthest(source)

    # get ordered list of nodes comprising 'diameter path'
    path = []
    visited = set()
    def dfs(cur):
      if cur == dest:
        path.append(cur)
        return True
      if cur in visited:
        return False
      path.append(cur)
      visited.add(cur)
      for nxt in adj[cur]:
        if dfs(nxt):
          return True
      path.pop()

      return False
    
    dfs(source)
    tgt = len(path) // 2

    # return MHT root(s) using 'diameter path'
    return [path[tgt]] if len(path) % 2 else [path[tgt - 1], path[tgt]]

