class Solution:
  def minCost(self, grid: List[List[int]]) -> int:
    # iterative BFS (modified Dijkstra's algorithm)

    VEC = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    m, n = len(grid), len(grid[0])
    # convert grid into weighted directed graph
    adj = defaultdict(list)
    for i in range(m):
      for j in range(n):
        for k in range(len(VEC)):
          dy, dx = VEC[k]
          ny, nx = i + dy, j + dx
          if 0 <= ny < m and 0 <= nx < n:
            adj[(i, j)].append((ny, nx, 0 if k+1 == grid[i][j] else 1))

    # find minimum cost of path using BFS
    dist = [[float('inf')]*n for _ in range(m)]
    dist[0][0] = 0
    nodes = deque([(0, 0)])
    while nodes:
      y, x = nodes.popleft()
      for ny, nx, nd in adj[(y, x)]:
        if dist[ny][nx] > dist[y][x] + nd:
          dist[ny][nx] = dist[y][x] + nd
          if nd == 1:
            nodes.append((ny, nx))
          else:
            nodes.appendleft((ny, nx))
      
    return dist[-1][-1]

