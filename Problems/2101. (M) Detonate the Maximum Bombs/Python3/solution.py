class Solution:
  def maximumDetonation(self, bombs: List[List[int]]) -> int:
    # iterative DFS

    n = len(bombs)
    adj = [[] for _ in range(n)]
    for i in range(n):
      for j in range(n):
        if i == j:
          continue
        d = sqrt((bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2)
        if bombs[i][2] >= d:
          adj[i].append(j)

    ret = -1
    for i in range(n):
      nodes = [i]
      visited = set()
      visited.add(i)
      count = 0
      while nodes:
        cur = nodes.pop()
        count += 1
        for nxt in adj[cur]:
          if nxt not in visited:
            nodes.append(nxt)
            visited.add(nxt)
      ret = max(ret, count)
    
    return ret

