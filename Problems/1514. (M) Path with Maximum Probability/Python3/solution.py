class Solution:
  def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    # dijkstra

    adj = [[] for _ in range(n)]
    for i in range(len(edges)):
      u, v = edges[i]
      adj[u].append((v, succProb[i]))
      adj[v].append((u, succProb[i]))

    probs = [0] * n
    probs[start] = 1
    # hack to make min heap a max heap
    nodes = [(-1, start)]
    while nodes:
      p, cur = heappop(nodes)
      if cur == end:
        return -p
      for nxt, nxt_p in adj[cur]:
        new_p = -p * nxt_p
        if new_p > probs[nxt]:
          probs[nxt] = new_p
          heappush(nodes, (-probs[nxt], nxt))

    return 0

