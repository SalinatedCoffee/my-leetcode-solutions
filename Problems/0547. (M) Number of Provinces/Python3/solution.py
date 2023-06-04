class Solution:
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    # iterative DFS

    n = len(isConnected)

    ret = 0
    visited = [False] * n
    for i in range(n):
      if not visited[i]:
        nodes = [i]
        while nodes:
          cur = nodes.pop()
          for nxt, c in enumerate(isConnected[cur]):
            if c and not visited[nxt]:
              nodes.append(nxt)
              visited[nxt] = True
        ret += 1
    
    return ret

