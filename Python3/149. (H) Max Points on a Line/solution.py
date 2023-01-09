class Solution:
  def maxPoints(self, points: List[List[int]]) -> int:
    # points on same line have same slope and intercepts
    # for every point, translate all other points so point is at origin

    # one or two points are always on same line
    if len(points) in [1, 2]:
      return len(points)

    ret = 0
    for i in points:
      slopes = {}
      for j in points:
        # compute slope
        x = i[0] - j[0]
        y = i[1] - j[1]
        # reduce by gcd
        gcd = math.gcd(x, y)
        if gcd:
          # Python / returns float even when operands are int
          slope = (x//gcd, y//gcd)
        else:
          slope = (x, y)
        # update dictionary using reduced slope as key
        if slope in slopes:
          slopes[slope] += 1
        else:
          slopes[slope] = 2
      # update max number accordingly
      cur = max(slopes.values())
      if cur > ret:
        ret = cur
   
    return ret

