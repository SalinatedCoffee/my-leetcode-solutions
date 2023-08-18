class Solution:
  def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
    # brute force with lists instead of sets

    adj = [[0]*(n+1) for _ in range(n)]
    for u, v in roads:
      adj[u][v] = 1
      adj[u][-1] += 1
      adj[v][u] = 1
      adj[v][-1] += 1

    ret = 0
    for i in range(n):
      for j in range(n):
        if i != j:
          rank = adj[i][-1] + adj[j][-1]
          if adj[i][j]:
            rank -= 1
          ret = max(ret, rank)

    return ret

