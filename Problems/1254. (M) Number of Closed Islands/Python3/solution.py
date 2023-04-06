class Solution:
  def closedIsland(self, grid: List[List[int]]) -> int:
    # iterative DFS

    m = len(grid)
    n = len(grid[0])
    # shared across traversals
    visited = set()

    def dfs(y, x):
      # sanity check
      if (y, x) in visited:
        return False
      border = 0
      nodes = []
      nodes.append((y, x))
      while nodes:
        cur = nodes.pop()
        if cur in visited:
          continue
        visited.add(cur)
        c_y, c_x = cur
        # raise flag if land square on border
        if not c_y or c_y == m-1 or not c_x or c_x == n-1:
          border = 1
        nxt = [(c_y+1,c_x), (c_y,c_x+1), (c_y-1,c_x), (c_y,c_x-1)]
        for n_y, n_x in nxt:
          if 0 <= n_y < m and 0 <= n_x < n and not grid[n_y][n_x]:
            nodes.append((n_y,n_x))

      return True if not border else False
    
    ret = 0
    for i in range(m):
      for j in range(n):
        if not grid[i][j] and dfs(i, j):
          ret += 1
    
    return ret

