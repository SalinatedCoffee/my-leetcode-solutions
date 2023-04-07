class Solution:
  def numEnclaves(self, grid: List[List[int]]) -> int:
    # iterative DFS
    m = len(grid)
    n = len(grid[0])
    visited = set()

    def dfs(y, x):
      ret = 0
      border = False
      nodes = []
      nodes.append((y,x))
      while nodes:
        cur = nodes.pop()
        if cur in visited:
          continue
        visited.add(cur)
        ret += 1
        c_y, c_x = cur
        if not border and not c_y or c_y == m-1 or not c_x or c_x == n-1:
          border = True
        nxt = [(c_y+1,c_x), (c_y,c_x+1), (c_y-1,c_x), (c_y,c_x-1)]
        for n_y, n_x in nxt:
          if 0 <= n_y < m and 0 <= n_x < n and grid[n_y][n_x]:
            nodes.append((n_y, n_x))
      return ret if not border else 0
    
    total = 0
    for i in range(m):
      for j in range(n):
        total += dfs(i, j) if grid[i][j] and (i,j) not in visited else 0
    
    return total

