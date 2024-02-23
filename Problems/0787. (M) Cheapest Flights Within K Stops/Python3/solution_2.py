class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # Dijkstra's algorithm with priority queue

    adj = [[] for _ in range(n)]
    for s, d, w in flights:
      adj[s].append((d, w))

    dist = [-1]*n
    # (sum of weights, number of hops, current vertex)
    nodes = [(0, 0, src)]
    while nodes:
      d, h, cur = heappop(nodes)
      if h > k+1:
        continue
      if cur == dst:
        return d
      if dist[cur] == h:
        continue
      dist[cur] = h
      for nxt, w in adj[cur]:
        if dist[nxt] == -1 or dist[nxt] > h:
          heappush(nodes, (d+w, h+1, nxt))
    
    return -1

