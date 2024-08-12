class Solution:
  def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    # math

    # sequence of values around edge of valid grid
    SEQ = "2943816729438167"
    SEQ_REV = SEQ[::-1]
    # edge cells in order of which they should be traversed
    IDX = [0, 1, 2, 5, 8, 7, 6, 3]

    m, n = len(grid), len(grid[0])
    ret = 0
    for i in range(m-2):
      for j in range(n-2):
        edge = []
        # retrieve string representation of edge cell values
        for k in IDX:
          edge.append(str(grid[i + k // 3][j + (k % 3)]))
        edge = ''.join(edge)
        # determine whether current grid is valid
        if grid[i][j] % 2 == 0 and (edge in SEQ or edge in SEQ_REV) and grid[i+1][j+1] == 5:
          ret += 1

    return ret

