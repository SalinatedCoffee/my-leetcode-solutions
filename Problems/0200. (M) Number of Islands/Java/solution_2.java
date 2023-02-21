class Solution {
  // Java doesn't support nested methods
  public void fill(int m, int n, char[][] grid) {
    // recursively fill adjacent 1s with 0s

    // holy shit java this is incredibly ugly
    if ((0 <= m && m < grid.length) &&
        (0 <= n && n < grid[0].length) &&
        (grid[m][n] == '1')) {
      grid[m][n] = '0';
      int[][] next_coords = {{m+1,n},{m,n+1},{m-1,n},{m,n-1}};
      for (int i = 0; i < 4; i++)
        fill(next_coords[i][0], next_coords[i][1], grid);
    }
  }

  public int numIslands(char[][] grid) {
    // flood fill based solution

    // don't modify input
    char[][] visited = new char[grid.length][];
    // no fancy copy.deepcopy() or list comprehensions for you
    // do it manually
    for (int i = 0; i < grid.length; i++)
      visited[i] = Arrays.copyOf(grid[i], grid[0].length);
    
    int islands = 0;
    // iterate across grid, call fill() if current square is land
    for (int i = 0; i < visited.length; i++) {
      for (int j = 0; j < visited[0].length; j++) {
        if (visited[i][j] == '1') {
          islands += 1;
          fill(i, j, visited);
        }
      }
    }

    return islands;
  }
}
