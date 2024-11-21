class Solution:
  def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    # brute force

    # 0 is unguarded, 1 is guarded, 2 is guard, and 3 is wall
    grid = [[0] * n for _ in range(m)]
    # place walls and guards on grid
    for i, j in walls:
      grid[i][j] = 3
    for i, j in guards:
      grid[i][j] = 2
    # mark guarded cells
    for i, j in guards:
      # fill row
      c = i - 1
      while c >= 0 and grid[c][j] not in [2, 3]:
        grid[c][j] = 1 if grid[c][j] == 0 else grid[c][j]
        c -= 1
      c = i + 1
      while c < m and grid[c][j] not in [2, 3]:
        grid[c][j] = 1 if grid[c][j] == 0 else grid[c][j]
        c += 1
      # fill column
      c = j - 1
      while c >= 0 and grid[i][c] not in [2, 3]:
        grid[i][c] = 1 if grid[i][c] == 0 else grid[i][c]
        c -= 1
      c = j + 1
      while c < n and grid[i][c] not in [2, 3]:
        grid[i][c] = 1 if grid[i][c] == 0 else grid[i][c]
        c += 1
    
    # count unguarded cells
    res = 0
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 0:
          res += 1

    return res

