class Solution:
  def minimumObstacles(self, grid: List[List[int]]) -> int:
    # iterative BFS

    m, n = len(grid), len(grid[0])
    vec = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    costs = [[float('inf')] * n for _ in range(m)]
    costs[0][0] = 0
    nodes = deque([(0, 0, 0)])
    while nodes:
      y, x, d = nodes.popleft()
      for dy, dx in vec:
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and costs[ny][nx] == float('inf'):
          # prioritize empty cells during traversal
          if grid[ny][nx] == 0:
            costs[ny][nx] = d
            nodes.appendleft((ny, nx, d))
          else:
            costs[ny][nx] = d + 1
            nodes.append((ny, nx, d + 1))

    return costs[-1][-1]

