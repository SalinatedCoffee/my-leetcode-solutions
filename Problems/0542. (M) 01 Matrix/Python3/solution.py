class Solution:
  def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    # iterative BFS

    m, n = len(mat), len(mat[0])
    ret = [[0]*n for _ in range(m)]
    vectors = [(1,0), (0,1), (-1,0), (0,-1)]
    # treat 0 cells as sources
    nodes = deque()
    for i in range(m):
      for j in range(n):
        if not mat[i][j]:
          nodes.append((i,j,0))
    
    visited = set()
    while nodes:
      y, x, d = nodes.popleft()
      if (y,x) in visited:
        continue
      if mat[y][x]:
        ret[y][x] = d
        visited.add((y,x))
      for dy, dx in vectors:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < m and 0 <= nx < n and mat[ny][nx]:
          nodes.append((ny,nx,d+1))
    
    return ret

