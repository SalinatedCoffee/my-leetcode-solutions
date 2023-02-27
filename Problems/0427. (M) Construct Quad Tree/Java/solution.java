class Solution {
  public Node recurse(Pair<Integer,Integer> s_coord, int size, int[][] grid) {
    int y = s_coord.getKey();
    int x = s_coord.getValue();
    int total = 0;

    // count number of 1s in square
    for (int i = y; i < y+size; i++) {
      // no builtin in Java, compute sum of subarray manually
      for (int j = x; j < x+size; j++)
        total += grid[i][j];
    }
    // verify if square is leaf
    if (total == (int) Math.pow(size, 2))
      return new Node(true, true);
    else if (total == 0)
      return new Node(false, true);
    // get params for subsquares
    int new_size = size / 2;
    Node tl = recurse(new Pair<Integer,Integer>(y, x), new_size, grid);
    Node tr = recurse(new Pair<Integer,Integer>(y, x+new_size), new_size, grid);
    Node bl = recurse(new Pair<Integer,Integer>(y+new_size, x), new_size, grid);
    Node br = recurse(new Pair<Integer,Integer>(y+new_size, x+new_size), new_size, grid);
    return new Node(true, false, tl, tr, bl, br);
  }

  public Node construct(int[][] grid) {
    // recursion, recurse on quads if square is not uniform

    return recurse(new Pair<Integer,Integer>(0, 0), grid.length, grid);
  }
}
