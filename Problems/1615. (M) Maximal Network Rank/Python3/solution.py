class Solution:
  def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
    # brute force
    
    adj = [set() for _ in range(n)]
    for u, v in roads:
      adj[u].add(v)
      adj[v].add(u)

    ret = 0
    for i in range(n):
      for j in range(n):
        if i != j:
          rank = len(adj[i]) + len(adj[j])
          if i in adj[j]:
            rank -= 1
          ret = max(ret, rank)

    return ret

