class Solution:
  def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    # rerooting dynamic programming with DFS

    # dp1[i] is sum of distances to all nodes not in the subtree rooted at node i
    # dp2[i] is sum of distances to all nodes in the subtree rooted at node i
    # sub[i] is the size of the subtree rooted at node i
    dp1, dp2, sub = [0] * n, [0] * n, [0] * n
    # convert list of edges to adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    def dfs1(node, prev):
      for nxt in adj[node]:
        # avoid retreading previously traversed path
        if nxt != prev:
          dfs1(nxt, node)
          dp1[node] += dp1[nxt] + sub[nxt]
          sub[node] += sub[nxt]
      sub[node] += 1

    def dfs2(node, prev):
      # for (arbitrary) root, value of dp1 equals that of dp2
      if prev == -1:
        dp2[node] = dp1[node]
      # otherwise, compute value of dp2
      else:
        dp2[node] = (dp2[prev] - sub[node]) + (n - sub[node])
      for nxt in adj[node]:
        # avoid retreading previously traversed path
        if nxt != prev:
          dfs2(nxt, node)
    
    dfs1(0, -1)
    dfs2(0, -1)

    return dp2

