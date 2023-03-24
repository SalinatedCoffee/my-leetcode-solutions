class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    # DFS, reverse source and destination

    n, m = len(heights), len(heights[0])
    # sanity check
    if not n:
      return []

    p = [[False for _ in range(m)] for _ in range(n)]
    a = [[False for _ in range(m)] for _ in range(n)]

    def dfs(y, x, ocean):
      nodes = []
      nodes.append((y,x))
      while nodes:
        u, v = nodes.pop()
        if ocean[u][v]:
          continue
        ocean[u][v] = True
        dest = [(u-1,v), (u,v-1), (u+1,v), (u,v+1)]
        for d_y, d_x in dest:
          if 0 <= d_y < n and 0 <= d_x < m and \
            heights[u][v] <= heights[d_y][d_x]:
            nodes.append((d_y,d_x))

    # traverse starting from shore squares
    for i in range(n):
      dfs(i, 0, p)
      dfs(i, m-1, a)
    for i in range(m):
      dfs(0, i, p)
      dfs(n-1, i, a)
    
    ret = []
    # get squares that flows to both oceans
    for i in range(n):
      for j in range(m):
        if p[i][j] and a[i][j]:
          ret.append([i,j])
    
    return ret

