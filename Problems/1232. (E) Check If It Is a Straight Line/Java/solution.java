class Solution {
  public boolean checkStraightLine(int[][] coordinates) {
    // cross product

    int n = coordinates.length;
    int o_x = coordinates[0][0];
    int o_y = coordinates[0][1];
    int[][] t_coords = new int[n][2];
    for (int i = 0; i < n; i++) {
      t_coords[i][0] = coordinates[i][0] - o_x;
      t_coords[i][1] = coordinates[i][1] - o_y;
    }
    
    for (int i = 2; i < n; i++) {
      int[] a = t_coords[i-1];
      int[] b = t_coords[i];
      if (a[0]*b[1] != a[1]*b[0])
        return false;
    }
    return true;
  }
}
