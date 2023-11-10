class Solution:
  def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
    # iterative DFS

    adj = defaultdict(list)
    for u, v in adjacentPairs:
      adj[u].append(v)
      adj[v].append(u)

    def dfs(s, e):
      # start traversing at node s while ignoring node e
      ret = []
      nodes = [s]
      visited = set([e])
      while nodes:
        cur = nodes.pop()
        visited.add(cur)
        for nxt in adj[cur]:
          if nxt not in visited:
            nodes.append(nxt)
        ret.append(cur)

      return ret

    i, j = adjacentPairs[0]
    a, b = dfs(i, j)[::-1], dfs(j, i)
    a.extend(b)

    return a

