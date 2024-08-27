class Solution:
  def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    # dijkstra's algorithm

    adj = [[] for _ in range(n)]
    for (u, v), p in zip(edges, succProb):
      adj[u].append((v, p))
      adj[v].append((u, p)) 

    probs = [0] * n
    probs[start] = 1
    # Python only supports min heaps, so negate values to use it as a max heap
    nodes = [(-1, start)]
    while nodes:
      p, cur = heappop(nodes)
      if cur == end:
        return -p
      for nxt, nxt_p in adj[cur]:
        if -p * nxt_p > probs[nxt]:
          probs[nxt] = -p * nxt_p
          heappush(nodes, (-p * nxt_p, nxt))

    return 0

