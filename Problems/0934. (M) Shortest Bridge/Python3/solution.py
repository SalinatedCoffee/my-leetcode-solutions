class Solution:
  def shortestBridge(self, grid: List[List[int]]) -> int:
    # identify island with DFS, find distance with BFS

    n = len(grid)
    # select any island
    src = (0, 0)
    for i in range(n):
      for j in range(n):
        if grid[i][j] == 1:
          src = (i, j)
          break
    
    # identify all land squares of selected island
    nodes = []
    nodes.append(src)
    bfs_nodes = deque()
    while nodes:
      x, y = nodes.pop()
      grid[x][y] = 2
      bfs_nodes.append((x, y, 0))
      adj = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
      for n_x, n_y in adj:
        if 0 <= n_x < n and 0 <= n_y < n and grid[n_x][n_y] == 1:
          nodes.append((n_x, n_y))
    
    # find shortest path to other island
    while bfs_nodes:
      x, y, d = bfs_nodes.popleft()
      adj = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
      for n_x, n_y in adj:
        if 0 <= n_x < n and 0 <= n_y < n:
          if grid[n_x][n_y] == 1:
            return d
          if not grid[n_x][n_y]:
            grid[n_x][n_y] = -1
            bfs_nodes.append((n_x, n_y, d+1))

    # this line will never run given problem constraints
    return -1

