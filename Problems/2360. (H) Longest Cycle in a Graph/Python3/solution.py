class Solution:
  def longestCycle(self, edges: List[int]) -> int:
    # simple graph traversal

    # visited[i][0]: traversal source node
    # visited[i][1]: length of path to node i
    visited = [(0,0) for _ in range(len(edges))]
    ret = -1
    for i in range(len(edges)):
      length = 1
      cur = i
      while cur != -1 and visited[cur][1] == 0:
        visited[cur] = (i, length)
        length += 1
        cur = edges[cur]
      if cur != -1 and visited[cur][0] == i:
        ret = max(ret, length - visited[cur][1])

    return ret

