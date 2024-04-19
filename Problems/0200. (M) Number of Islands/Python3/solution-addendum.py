class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    # union find without BFS
    
    m, n = len(grid), len(grid[0])
    # find all land cells
    p = {}
    for i in range(m):
      for j in range(n):
        if grid[i][j] == '1':
          p[(i, j)] = (i, j)

    def ufind(a):
      while p[a] != a:
        a = p[a]

      return a
    
    def uunion(a, b):
      p[ufind(b)] = ufind(a)
    
    # merge adjacent land cells
    for i in range(1, m):
      if grid[i][0] == grid[i-1][0] == '1':
        uunion((i, 0), (i-1, 0))
    
    for j in range(1, n):
      if grid[0][j] == grid[0][j-1] == '1':
        uunion((0, j), (0, j-1))
    
    for i in range(1, m):
      for j in range(1, n):
        if grid[i][j] == '1':
          if grid[i-1][j] == '1':
            uunion((i, j), (i-1, j))
          if grid[i][j-1] == '1':
            uunion((i, j), (i, j-1))    
    
    # return number of disjoint sets
    return len(set([ufind((i, j)) for (i, j) in p.keys()]))

