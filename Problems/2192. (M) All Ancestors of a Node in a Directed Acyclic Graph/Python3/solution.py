class Solution:
  def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    # iterative DFS on transposed graph

    ret = []
    # convert list of edges to adjacency list while reversing them
    adj = defaultdict(list)
    for u, v in edges:
      adj[v].append(u)

    # start DFS at each node to find their ancestors
    for i in range(n):
      nodes = [i]
      visited = set()
      while nodes:
        cur = nodes.pop()
        visited.add(cur)
        # if we already know the ancestors of this node...
        if cur < len(ret) and len(ret[cur]) > 0:
          # ...use that instead of traversing it and its ancestors again
          visited.update(ret[cur])
          continue
        for nxt in adj[cur]:
          if nxt not in visited:
            nodes.append(nxt)
      # a node cannot be an ancestor of itself
      visited.remove(i)
      # sort list of ancestors and add it to the return list
      ret.append(sorted(list(visited)))
    
    return ret

