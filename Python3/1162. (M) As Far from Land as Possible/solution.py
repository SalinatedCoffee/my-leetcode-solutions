class Solution:
  def maxDistance(self, grid: List[List[int]]) -> int:
    # multisource BFS

    # size of one side and set of visited squares
    n = len(grid)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    
    nodes = deque()
    # get coords of land squares
    for i in range(n):
      for j in range(n):
        if grid[i][j]:
          nodes.append((i, j, 0))

    # sanity check
    if not len(nodes) or len(nodes) == n**2:
      return -1
    
    max_dist = -1
    # traverse
    while len(nodes):
      y, x, d = nodes.popleft()
      if visited[y][x]:
        continue
      visited[y][x] = 1
      max_dist = max(max_dist, d)
      d += 1
      adj = [(y-1,x),(y,x-1),(y+1,x),(y,x+1)]
      for c in adj:
        # queue node if valid coords and not visited
        if 0 <= c[0] < n and 0 <= c[1] < n and not visited[c[0]][c[1]]:
          nodes.append((c[0], c[1], d))

    return max_dist

