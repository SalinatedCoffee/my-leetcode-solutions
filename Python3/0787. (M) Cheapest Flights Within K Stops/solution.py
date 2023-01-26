class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # BFS, with memoized minimum prices to nodes

    # generate adjacency list
    adj = [[] for _ in range(n)]
    for flight in flights:
      f, t, p = flight
      adj[f].append((t, p))

    # cheapest prices to nodes
    min_prices = [float('inf') for _ in range(n)]

    visit = deque()
    #(total price, node, stops)
    visit.append((0, src, -1))
    while visit:
      p, c, s = visit.popleft()
      # update min. price for node c as necessary
      min_prices[c] = p if p < min_prices[c] else min_prices[c]
      # current expenditure exceeds cheapest price to current
      if p > min_prices[c]:
        continue
      for nxt in adj[c]:
        # next leg would exceed stop limit
        if s == k:
          break
        visit.append((p+nxt[1], nxt[0], s+1))

    return min_prices[dst] if min_prices[dst] != float('inf') else -1

