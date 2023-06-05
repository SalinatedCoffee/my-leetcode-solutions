class Solution:
  def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    # cross product

    n = len(coordinates)
    o_x, o_y = coordinates[0]
    t_coords = [[v[0]-o_x, v[1]-o_y] for v in coordinates]

    for i in range(2, n):
      a, b = t_coords[i-1], t_coords[i]
      if a[0]*b[1] != a[1]*b[0]:
        return False
    
    return True

