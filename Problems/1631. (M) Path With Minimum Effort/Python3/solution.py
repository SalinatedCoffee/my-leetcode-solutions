class Solution:
  def minimumEffortPath(self, heights: List[List[int]]) -> int:
    # modified Dijkstra's algorithm

    m, n = len(heights), len(heights[0])
    vectors = [(1,0), (0,1), (-1,0), (0,-1)]
    nodes = [(0,0,0)]
    dist = [[10**6] * n for _ in range(m)]
    dist[0][0] = 0

    while nodes:
      d, y, x = heappop(nodes)
      if y == m-1 and x == n-1:
        return dist[-1][-1]
      for dy, dx in vectors:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < m and 0 <= nx < n:
          nd = max(d, abs(heights[y][x] - heights[ny][nx]))
          if nd < dist[ny][nx]:
            dist[ny][nx] = nd
            heappush(nodes, (nd, ny, nx))
    
    return -1

