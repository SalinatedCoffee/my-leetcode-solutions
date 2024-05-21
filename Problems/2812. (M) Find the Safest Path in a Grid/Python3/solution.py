class Solution:
  def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
    # multi-source BFS with binary search

    n = len(grid)
    VEC = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    nodes = deque()
    for i in range(n):
      for j in range(n):
        # if cell contains a thief, add it to the BFS queue and mark cell with a distance of 0
        if grid[i][j]:
          nodes.append((i, j))
          grid[i][j] = 0
        # otherwise, mark cell as unvisited by assigning distance of -1
        else:
          grid[i][j] = -1
    
    # perform multi-source BFS, marking each non-thief cell with its safeness factor
    while nodes:
      cy, cx = nodes.popleft()
      for dy, dx in VEC:
        ny, nx = cy+dy, cx+dx
        # get safeness factor of the current cell
        v = grid[cy][cx]
        if 0 <= ny < n and 0 <= nx < n and grid[ny][nx] == -1:
          grid[ny][nx] = v + 1
          nodes.append((ny, nx))
    
    l, h, ret = 0, 0, -1
    # find upper bound for initial search space
    for i in range(n):
      for j in range(n):
        h = max(h, grid[i][j])
    
    # perform binary search
    while l <= h:
      m = l + (h - l) // 2
      # run BFS to determine whether a path with a safeness factor higher than the midpoint exists
      safe = False
      if grid[0][0] >= m and grid[n-1][n-1] >= m:
        nodes = deque([(0, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        safe = False
        while nodes:
          cy, cx = nodes.popleft()
          if cy == n - 1 and cx == n - 1:
            safe = True
          for dy, dx in VEC:
            ny, nx = cy+dy, cx+dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and grid[ny][nx] >= m:
              visited[ny][nx] = True
              nodes.append((ny, nx))
      # midpoint is safe, discard lower half and update maximum safeness factor
      if safe:
        ret = m
        l = m + 1
      else:
        h = m - 1
    
    return ret

