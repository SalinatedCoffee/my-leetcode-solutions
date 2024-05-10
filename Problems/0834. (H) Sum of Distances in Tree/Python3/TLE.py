class Solution:
  def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    # brute force using DFS

    # convert list of edges to adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    ret = [0] * n
    # traverse tree using each node as root
    for i in range(n):
      nodes = [(i, 0, -i)]
      while nodes:
        cur, d, prev = nodes.pop()
        ret[i] += d
        for nxt in adj[cur]:
          if nxt != prev:
            nodes.append((nxt, d+1, cur))

    return ret

