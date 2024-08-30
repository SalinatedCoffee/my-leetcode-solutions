class Solution:
  def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
    # dijkstra's algorithm with min heap

    INF = int(2e9)
    # construct graph from list of edges, ignoring those with negative weight
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
      if w != -1:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # returns total weight of shortest path from source to destination
    def shortest_path():
      dist = [float('inf')] * n
      dist[source] = 0
      heap = [(0, source)]
      while heap:
        w, cur = heappop(heap)
        if w > dist[cur]:
          continue
        for nxt, nxt_w in adj[cur]:
          if nxt_w + w < dist[nxt]:
            dist[nxt] = nxt_w + w
            heappush(heap, (nxt_w + w, nxt))
      
      return dist[destination]
    
    init_d = shortest_path()
    if init_d < target:
      return []
    elif init_d == target:
      # set weights of negative weighted edges to arbitrarily large value
      for edge in edges:
        if edge[2] == -1:
          edge[2] = INF
      return edges
    
    for i, (u, v, w) in enumerate(edges):
      if w != -1:
        continue
      # try setting weight of current modifiable edge to 1
      edges[i][2] = 1
      adj[u].append((v, 1))
      adj[v].append((u, 1))

      cur_d = shortest_path()
      # sum of shortest path in current version of modified graph is less than target
      if cur_d <= target:
        # change edge weight to bring sum of path to target
        edges[i][2] += target - cur_d
        # set weights of all other modifiable edges to arbitrarily large value
        for j in range(i+1, len(edges)):
          if edges[j][2] == -1:
            edges[j][2] = INF
        return edges

    return []

