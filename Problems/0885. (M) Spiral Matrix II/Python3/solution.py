class Solution:
  def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    # simulation
    
    # list of directions
    VEC = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # total distance to move in current direction
    reach = 1
    ret = []
    # coordinates of current position, current direction, current distance
    y, x, v, d = rStart, cStart, 0, 0
    while True:
      # current position is in bounds
      if 0 <= y < rows and 0 <= x < cols:
        ret.append([y, x])
      # all cells of matrix traversed
      if len(ret) == rows*cols:
        break
      # advance to next position
      y += VEC[v][0]
      x += VEC[v][1]
      d += 1
      # reached last position of current direction
      if d == reach:
        v = (v+1) % len(VEC)
        # total distance should increase every 2 direction changes
        if v == 0 or v == 2:
          reach += 1
        d = 0

    return ret

