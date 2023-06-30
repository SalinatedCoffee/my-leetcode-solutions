class Solution:
  def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
    # union find

    dim = row * col
    # uf[0] and uf[-1] are top and bottom sentinels, respectively
    uf = list(range(dim+2))
    usize = [1] * (dim+2)
    turnstile = [[1] * col for _ in range(row)]

    def ufind(a):
      p = uf[a]
      while p != a:
        a = p
        p = uf[a]
      return p

    def uunion(a, b):
      pa, pb = ufind(a), ufind(b)
      if pa == pb:
        return
      # union by size
      if usize[pa] < usize[pb]:
        uf[pa] = pb
        usize[pb] += usize[pa]
      else:
        uf[pb] = pa
        usize[pa] += usize[pb]
    
    n = len(cells)
    vectors = [(1,0), (0,1), (-1,0), (0,-1)]
    for i in range(len(cells)-1, -1, -1):
      r, c = cells[i][0]-1, cells[i][1]-1
      s = col * r + c + 1
      turnstile[r][c] = 0
      for dy, dx in vectors:
        ny = r + dy
        nx = c + dx
        if 0 <= ny < row and 0 <= nx < col and not turnstile[ny][nx]:
          uunion(s, col * ny + nx + 1)
      if not r:
        uunion(s, 0)
      elif r == row - 1:
        uunion(s, dim+1)
      if ufind(0) == ufind(dim+1):
        return i

    # according to problem description, this line will never run
    return -1

