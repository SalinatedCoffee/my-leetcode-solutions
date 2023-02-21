class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    # flood fill based solution

    # don't modify input
    visited = deepcopy(grid)

    # recursively fill adjacent 1s with 0s
    def fill(m, n):
      if 0 <= m < len(visited) and 0 <= n < len(visited[0]) and visited[m][n] == '1':
        visited[m][n] = '0'
        next_coords = [(m-1,n),(m,n-1),(m+1,n),(m,n+1)]
        for n_m, n_n in next_coords:
          fill(n_m,n_n)

    islands = 0
    # iterate across grid, call fill() if current square is land
    for i in range(len(visited)):
      for j in range(len(visited[0])):
        if visited[i][j] == '1':
          islands += 1
          fill(i, j)
    
    return islands

