class Solution:
  def numSimilarGroups(self, strs: List[str]) -> int:
    # iterative DFS

    # generate graph
    n = len(strs)
    m = len(strs[0])
    adj = [[] for _ in range(n)]
    for i in range(n):
      for j in range(i, n):
        diff = 0
        for k in range(m):
          if strs[i][k] != strs[j][k]:
            diff += 1
        if not diff or diff == 2:
          adj[i].append(j)
          adj[j].append(i)
    
    # count connected components
    visited = [False] * n
    ret = 0
    for i in range(n):
      if visited[i]:
        continue
      ret += 1
      nodes = []
      nodes.append(i)
      while nodes:
        cur = nodes.pop()
        if visited[cur]:
          continue
        visited[cur] = True
        for nxt in adj[cur]:
          if not visited[nxt]:
            nodes.append(nxt)
      
    return ret

