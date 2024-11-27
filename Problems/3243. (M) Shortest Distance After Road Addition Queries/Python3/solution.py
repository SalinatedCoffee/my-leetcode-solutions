class Solution:
  def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    # brute force using iterative BFS

    adj = [[i+1] for i in range(n-1)]
    adj.append([])

    # return length of shortest path between nodes 0 and n-1
    def BFS():
      nodes = deque([(0, 0)])
      visited = set([0])
      while nodes:
        cur, d = nodes.popleft()
        if cur == n-1:
          return d
        for nxt in adj[cur]:
          if nxt not in visited:
            visited.add(nxt)
            nodes.append((nxt, d+1))
    
    res = []
    # add query edge to graph and run BFS
    for u, v in queries:
      adj[u].append(v)
      res.append(BFS())

    return res

