class Solution:
  def findMaxFish(self, grid: List[List[int]]) -> int:
    # union-find

    m, n = len(grid), len(grid[0])
    VEC = [(-1, 0), (0, -1)]
    # value of p[i] is label of set containing i
    p = [i for i in range(m*n)]
    
    # utility function that returns label of set containing a
    def ufind(a):
      p_a = p[a]
      while p_a != a:
        a = p_a
        p_a = p[a]
      return a
    
    # utility function that merges set containing a with set containing b
    def uunion(a, b):
      p_a, p_b = ufind(a), ufind(b)
      if p_a > p_b:
        p[p_a] = p_b
      else:
        p[p_b] = p_a
    
    # group bodies of water
    for i in range(m):
      for j in range(n):
        if grid[i][j] > 0:
          for dy, dx in VEC:
            ny, nx = i + dy, j + dx
            if 0 <= ny and 0 <= nx and grid[ny][nx] > 0:
              uunion(i*n+j, ny*n+nx)

    # compute number of fish for each body of water
    sums = defaultdict(int)
    sums[-1] = 0
    for i in range(m):
      for j in range(n):
        if grid[i][j] > 0:
          sums[ufind(i*n+j)] += grid[i][j]

    return max(sums.values())

