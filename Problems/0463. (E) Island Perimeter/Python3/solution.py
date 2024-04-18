class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    # iterative DFS with visited set

    m, n = len(grid), len(grid[0])
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # find starting cell
    y, x = 0, 0
    for i in range(m):
      for j in range(n):
        if grid[i][j]:
          y, x = i, j
          break
    
    # traverse island using DFS, count number of land cells and adjacent edges
    land, connections = 0, 0
    visited = set()
    nodes = [(y, x)]
    while nodes:
      cy, cx = nodes.pop()
      if (cy, cx) in visited:
        continue
      visited.add((cy, cx))
      land += 1
      for dy, dx in deltas:
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] and (ny, nx) not in visited:
          nodes.append((ny, nx))
          connections += 1

    # each cell has 4 edges, each adjacency removes 2 edges
    return land * 4 - connections * 2

