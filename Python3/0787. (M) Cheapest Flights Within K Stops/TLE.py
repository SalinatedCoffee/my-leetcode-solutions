class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # queue by stops, init array of prices where len is k
    # if destination, update minimum prices accordingly

    # generate adjacency list
    adj = [[] for _ in range(n)]
    for flight in flights:
      f, t, p = flight
      adj[f].append((t, p))

    min_price = float('inf')

    visit = deque()
    #(total price, node, stops, visited)
    visit.append((0, src, -1, set()))
    while visit:
      p, c, s, seen = visit.popleft()
      if s > k:
        break
      if c == dst and p < min_price:
        min_price = p
      elif p > min_price:
        continue
      elif c not in seen:
        seen.add(c)
        for nxt in adj[c]:
          if nxt[0] in seen:
            continue
          visit.append((p+nxt[1], nxt[0], s+1, set(seen)))

    return min_price if min_price != float('inf') else -1

