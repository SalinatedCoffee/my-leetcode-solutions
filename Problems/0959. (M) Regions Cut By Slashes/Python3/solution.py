class Solution:
  def regionsBySlashes(self, grid: List[str]) -> int:
    # union find

    n = len(grid)

    # initialize nodes
    # p[i][j][k] represents parent of node grid[i][j] pointing to k
    # where k can be thought of as the index in list [up, right, down, left]
    p = [[[None]*4 for _ in range(n)] for _ in range(n)]
    for i in range(n):
      for j in range(n):
        for k in range(4):
          p[i][j][k] = (i, j, k)

    # each square is subdivided into 4 sections    
    self.components = 4*n*n

    # find parent node of a
    def ufind(a):
      pa = p[a[0]][a[1]][a[2]]
      while pa != a:
        temp = p[pa[0]][pa[1]][pa[2]]
        a = pa
        pa = temp

      return pa
    
    # merge nodes a and b, updating the number of components when necessary
    def uunion(a, b):
      pa, pb = ufind(a), ufind(b)
      if pa != pb:
        self.components -= 1
        p[pa[0]][pa[1]][pa[2]] = pb
    
    # iterate over all squares
    for i in range(n):
      for j in range(n):
        # connections to neighboring squares always happen
        if i > 1:
          uunion((i, j, 0), (i-1, j, 2))
        if j < n-1:
          uunion((i, j, 1), (i, j+1, 3))
        if i < n-1:
          uunion((i, j, 2), (i+1, j, 0))
        if j > 1:
          uunion((i, j, 3), (i, j-1, 1))
        # connect subdivided squares depending on the slash
        match grid[i][j]:
          case '/':
            uunion((i, j, 0), (i, j, 3))
            uunion((i, j, 1), (i, j, 2))
          case '\\':
            uunion((i, j, 0), (i, j, 1))
            uunion((i, j, 2), (i, j, 3))
          case _:
            uunion((i, j, 0), (i, j, 3))
            uunion((i, j, 1), (i, j, 2))
            uunion((i, j, 0), (i, j, 1))

    return self.components

