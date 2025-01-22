class Solution:
  def trapRainWater(self, heightMap: List[List[int]]) -> int:
    # multisource iterative BFS with priority queue

    m, n = len(heightMap), len(heightMap[0])
    # sanity check
    if m < 3 or n < 3:
      return 0

    VEC = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # value of visited[i][j] is False if heightMap[i][j] has been visited
    visited = [[False]*n for _ in range(m)]
    # min heap of cells to be visited, using height as the key
    boundary = []
    # add cells on the edge of the grid to boundary
    for i in range(m):
      boundary.append((heightMap[i][0], (i, 0)))
      boundary.append((heightMap[i][-1], (i, n-1)))
      visited[i][0] = True
      visited[i][-1] = True
    for j in range(1, n-1):
      boundary.append((heightMap[0][j], (0, j)))
      boundary.append((heightMap[-1][j], (m-1, j)))
      visited[0][j] = True
      visited[-1][j] = True
    
    res = 0
    # determine volume using multisource iterative BFS
    heapify(boundary)
    while boundary:
      h, (y, x) = heappop(boundary)
      for dy, dx in VEC:
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and visited[ny][nx] is False:
          # compute volume of water on top of neighboring cell
          # before visiting it and marking it as boundary
          if heightMap[ny][nx] < h:
            res += h - heightMap[ny][nx]
          heappush(boundary, (max(h, heightMap[ny][nx]), (ny, nx)))
          visited[ny][nx] = True
    
    return res

