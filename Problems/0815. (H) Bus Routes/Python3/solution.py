class Solution:
  def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    # BFS with dictionaries

    n = len(routes)
    # adj[i] is list of buses that stops at stop i
    adj = defaultdict(list)
    for i in range(n):
      for stop in routes[i]:
        adj[stop].append(i)

    nodes = deque([(source, 0)])
    visited = set()
    while nodes:
      cur, d = nodes.popleft()
      if cur == target:
        return d
      for bus in adj[cur]:
        if bus not in visited:
          for stop in routes[bus]:
            if stop != cur:
              nodes.append((stop, d+1))
          visited.add(bus)
    
    return -1

