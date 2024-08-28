class Solution:
  def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    # iterative dfs with visited set

    VEC = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    m, n = len(grid1), len(grid1[0])
    visited = set()
    ret = 0

    # returns True if the landmass in grid2 containing square (r, c) is an island
    def verify(r, c):
      stack = [(r, c)]
      res = True
      while stack:
        cy, cx = stack.pop()
        visited.add((cy, cx))
        res &= grid1[cy][cx] == 1
        for dy, dx in VEC:
          ny, nx = cy + dy, cx + dx
          if 0 <= ny < m and 0 <= nx < n and (ny, nx) not in visited and grid2[ny][nx]:
            stack.append((ny, nx))
      
      return res

    for i in range(m):
      for j in range(n):
        if grid2[i][j] and (i, j) not in visited:
          ret += 1 if verify(i, j) else 0

    return ret

