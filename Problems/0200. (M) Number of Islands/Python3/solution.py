class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    # crude union find based solution
    # if adjacent squares are both land, merge two squares in u-f

    m, n = len(grid), len(grid[0])
    p = [[(i,j) for j in range(n)] for i in range(m)]

    def ufind(a):
      p_a = p[a[0]][a[1]]
      if p_a != a:
        return ufind(p_a)
      return a
    
    # rank based on python tuple comparison
    def uunion(a, b):
      p_a, p_b = ufind(a), ufind(b)
      if p_a > p_b:
        p[p_b[0]][p_b[1]] = p_a
      else:
        p[p_a[0]][p_a[1]] = p_b

    nodes = deque()
    nodes.append(((0,0),(0,0)))
    visited = set()
    # BFS
    while nodes:
      coord, prev = nodes.popleft()
      if (grid[coord[0]][coord[1]] == '1') and (grid[prev[0]][prev[1]] == '1'):
        uunion(coord, prev)
      if coord in visited:
        continue
      visited.add(coord) 
      i, j = coord
      if i < m-1:
        nodes.append(((i+1, j), coord))
      if j < n-1:
        nodes.append(((i, j+1), coord))
    
    # count islands
    islands = set()
    for i in range(m):
      for j in range(n):
        if grid[i][j] == '1':
          islands.add(ufind((i,j)))
    
    return len(islands)

