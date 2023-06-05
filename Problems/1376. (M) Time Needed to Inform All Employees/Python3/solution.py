class Solution:
  def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    # iterative DFS

    adj = [[] for _ in range(n)]
    for i, p in enumerate(manager):
      if p != -1:
        adj[p].append(i)
    
    ret = -1
    nodes = [(headID, 0)]
    while nodes:
      cur, t = nodes.pop()
      if not adj[cur]:
        ret = max(ret, t)
      else:
        for nxt in adj[cur]:
          nodes.append((nxt, t+informTime[cur]))

    return ret

