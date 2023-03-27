class Solution:
  def countPairs(self, n: int, edges: List[List[int]]) -> int:
    # iterative DFS

    # sanity check
    if not edges:
      return n*(n-1)//2

    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)
    
    counts = []
    visited = set()
    # perform DFS starting at each node
    for i in range(n):
      if i in visited:
        continue
      nodes = []
      nodes.append(i)
      count = 0
      while nodes:
        cur = nodes.pop()
        if cur in visited:
          continue
        visited.add(cur)
        count += 1
        for nxt in adj[cur]:
          nodes.append(nxt)
      # record size if disconnected component
      if count:
        counts.append(count)
    
    # nC2, all possible pairs of nodes
    total = n*(n-1)//2
    # subtract connected pairs
    for count in counts:
      total -= count*(count-1)//2
    
    return total

