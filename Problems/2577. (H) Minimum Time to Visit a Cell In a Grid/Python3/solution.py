class Solution:
  def minimumTime(self, grid: List[List[int]]) -> int:
    # dijkstra's algorithm

    if grid[0][1] > 1 and grid[1][0] > 1:
      return -1
    
    m, n = len(grid), len(grid[0])
    vec = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set([(0, 0)])
    nodes = [(grid[0][0], 0, 0)]
    while nodes:
      t, y, x = heappop(nodes)
      if (y, x) == (m-1, n-1):
        return t
      for dy, dx in vec:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < m and 0 <= nx < n and (ny, nx) not in visited:
          visited.add((ny, nx))
          # compute extra time required to wait until this cell becomes available
          dt = 0 if (grid[ny][nx] - t) % 2 else 1
          heappush(nodes, (max(grid[ny][nx] + dt, t + 1), ny, nx))

    return -1

